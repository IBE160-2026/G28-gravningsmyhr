"""Black-box HTTP checks against an isolated local database."""
import concurrent.futures
import http.cookiejar
import json
import os
from pathlib import Path
import secrets
import threading
import unittest
from unittest.mock import patch
from urllib.error import HTTPError
from urllib.request import Request, build_opener, HTTPCookieProcessor, urlopen
from http.server import ThreadingHTTPServer
from api.index import handler


class HTTPTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.path = Path('http-test-'+secrets.token_hex(8)+'.sqlite3')
        cls.env = patch.dict(os.environ, {'BEER_DB':str(cls.path), 'DATABASE_URL':'', 'VERCEL':''})
        cls.env.start()
        cls.server = ThreadingHTTPServer(('127.0.0.1',0), handler)
        cls.url = 'http://127.0.0.1:'+str(cls.server.server_port)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()
        cls.env.stop()
        cls.path.unlink(missing_ok=True)

    def client(self):
        return build_opener(HTTPCookieProcessor(http.cookiejar.CookieJar()))

    def call(self, client, action, data, headers=True):
        request = Request(self.url+'/api/'+action, data=json.dumps(data).encode(),
                          headers={'Content-Type':'application/json', **({'X-Beer-Request':'1'} if headers else {})})
        try:
            with client.open(request) as response:
                return response.status, json.load(response)
        except HTTPError as response:
            with response:
                return response.code, json.load(response)

    def account(self):
        client=self.client()
        status,_=self.call(client,'register',dict(email=secrets.token_hex(6)+'@example.test',password='local-http-test-password'))
        self.assertEqual(status,200)
        return client

    def test_static_and_traversal(self):
        for path in ['/', '/app.js', '/style.css']:
            with urlopen(self.url+path) as response:self.assertEqual(response.status,200)
        with self.assertRaises(HTTPError) as cm:urlopen(self.url+'/../storage.py')
        self.assertEqual(cm.exception.code,404)
        cm.exception.close()

    def test_csrf_and_anonymous(self):
        c=self.client()
        self.assertEqual(self.call(c,'me',{},False)[0],403)
        self.assertEqual(self.call(c,'new',dict(role=0))[0],403)

    def test_lost_response_retry_and_conflict(self):
        c=self.account()
        gid=self.call(c,'new',dict(role=0))[1]['id']
        command=dict(id=gid,quantity=4,version=0,command='same-request')
        self.assertEqual(self.call(c,'turn',command)[0],200)
        self.assertEqual(self.call(c,'turn',command)[1]['period'],1)
        self.assertEqual(self.call(c,'turn',{**command,'quantity':5})[0],400)
        self.assertEqual(self.call(c,'turn',{**command,'command':'another-request'})[0],400)

    def test_concurrent_tabs(self):
        c=self.account()
        gid=self.call(c,'new',dict(role=0))[1]['id']
        # CookieJar is read only during these requests; no session mutation is performed.
        def turn(i):return self.call(c,'turn',dict(id=gid,quantity=4,version=0,command='concurrent-'+str(i)))[0]
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
            self.assertEqual(sorted(pool.map(turn,[1,2])),[200,400])
        self.assertEqual(self.call(c,'game',dict(id=gid))[1]['period'],1)

    def test_other_account_and_invalid_orders(self):
        a,b=self.account(),self.account()
        gid=self.call(a,'new',dict(role=0))[1]['id']
        self.assertEqual(self.call(b,'game',dict(id=gid))[0],403)
        for q in [-1,101,0.5,'5',True]:
            self.assertEqual(self.call(a,'turn',dict(id=gid,quantity=q,version=0,command='invalid-order'))[0],400)
        self.assertEqual(self.call(a,'game',dict(id=gid))[1]['period'],0)


if __name__ == '__main__':unittest.main()
