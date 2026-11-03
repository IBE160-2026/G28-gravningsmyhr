import copy
import json
import os
import tempfile
from pathlib import Path
import secrets
import unittest
from unittest.mock import patch, Mock
from game import advance, new_game, prepare, visible
from api.index import dispatch
from storage import transaction
from reflection import generate


class MotorTests(unittest.TestCase):
    def test_hand_calculated_zero_order_chain(self):
        # Student is retailer, always zero; computer orders are calculated independently.
        # P1: demand 4,0,0,0; remaining 8,12,12,12; all orders zero.
        # P2: retailer remaining 4; P3: zero; P4: backlog 4; P5: backlog 12.
        s = new_game(0)
        expected = [(8,0,400),(4,0,200),(0,0,0),(0,4,400),(0,12,1200)]
        for t,(stock,backlog,cost) in enumerate(expected):
            s = advance(s,0,t,f'command-{t}')
            row=s['history'][-1]
            self.assertEqual(row['stock'],[stock,12,12,12])
            self.assertEqual(row['backlog'],[backlog,0,0,0])
            self.assertEqual(row['decisions'],[0,0,0,0])
            self.assertEqual(row['cost'],[cost,600,600,600])

    def test_transport_and_order_delay(self):
        s=advance(new_game(0),4,0,'command-0')
        s=advance(s,0,1,'command-1')
        self.assertEqual(s['history'][1]['demand'],[4,4,0,0])
        self.assertEqual(s['history'][1]['sent'],[4,4,0,0])
        s=advance(s,0,2,'command-2')
        self.assertEqual(s['history'][2]['incoming'][0],0)
        s=advance(s,0,3,'command-3')
        self.assertEqual(s['history'][3]['incoming'][0],4)

    def test_factory_production(self):
        s=advance(new_game(3),7,0,'command-0')
        s=advance(s,0,1,'command-1')
        self.assertEqual(s['history'][1]['incoming'][3],0)
        s=advance(s,0,2,'command-2')
        self.assertEqual(s['history'][2]['incoming'][3],7)

    def test_all_roles_and_invariants(self):
        for role in range(4):
            s=new_game(role)
            for t in range(20):
                original=copy.deepcopy(s)
                prepare(s)
                self.assertEqual(s,original)
                s=advance(s,(t*7)%101,t,f'command-{t}')
                for a,b in zip(s['stock'],s['backlog']):
                    self.assertGreaterEqual(a,0)
                    self.assertGreaterEqual(b,0)
                    self.assertEqual(a*b,0)
            self.assertTrue(visible(s)['done'])
            self.assertEqual(s['cost'],[sum(x['cost'][r] for x in s['history']) for r in range(4)])
            with self.assertRaises(ValueError):advance(s,0,20,'finished')

    def test_replay_conflicts_and_validation(self):
        s=advance(new_game(0),4,0,'command-0')
        self.assertEqual(advance(s,4,0,'command-0'),s)
        for q,v,c in [(5,0,'command-0'),(4,0,'command-1'),(-1,1,'command-1'),(101,1,'command-1'),(True,1,'command-1'),(1.5,1,'command-1')]:
            with self.assertRaises(ValueError):advance(s,q,v,c)

    def test_hidden_information(self):
        view=visible(new_game(0))
        self.assertNotIn('shipments',view)
        self.assertNotIn('orders',view)
        self.assertNotIn('costs',view)
        self.assertIsInstance(view['current']['stock'],int)


class ServiceTests(unittest.TestCase):
    def setUp(self):
        self.db=dict(users={},sessions={},games={},classes={},attempts={})
        self.tokens=[]
        for i in range(4):
            _,token=dispatch(self.db,'register',dict(email=f'u{i}@example.test',password='testing-password'), '')
            self.tokens.append(token)

    def call(self,action,data=None,n=0):
        return dispatch(self.db,action,data or {},self.tokens[n])[0]

    def test_owner_and_teacher_access(self):
        users=list(self.db['users'])
        self.db['users'][users[2]]['role']='teacher'
        self.db['users'][users[3]]['role']='teacher'
        self.call('class',dict(name='Logistikk'),2)
        code=self.call('list',n=2)['classes'][0]['code']
        gid=self.call('new',dict(role=0,code=code))['id']
        for n in [1,3]:
            with self.assertRaises(PermissionError):self.call('game',dict(id=gid),n)
        self.assertTrue(self.call('game',dict(id=gid),2)['teacher'])
        with self.assertRaises(PermissionError):self.call('turn',dict(id=gid,quantity=4,version=0,command='command-0'),2)
        with self.assertRaises(PermissionError):self.call('class',dict(name='No'),1)

    def test_auth_and_logout(self):
        self.assertIsNotNone(self.call('me')['user'])
        self.call('logout')
        self.assertIsNone(self.call('me')['user'])
        with self.assertRaises(PermissionError):self.call('new',dict(role=0))

    def test_database_rollback_and_resume(self):
        path=Path('test-'+secrets.token_hex(8)+'.sqlite3')
        try:
            with patch.dict(os.environ,{'BEER_DB':str(path)}):
                with transaction() as db:db.update(self.db)
                with self.assertRaises(ValueError):
                    with transaction() as db:
                        db['users']={}
                        raise ValueError('test rollback')
                with transaction() as db:self.assertEqual(db['users'],self.db['users'])
        finally:
            path.unlink(missing_ok=True)

    def test_production_requires_database(self):
        with patch.dict(os.environ,{'VERCEL':'1','DATABASE_URL':''}):
            with self.assertRaises(RuntimeError):
                with transaction():pass

    def test_database_closes_when_initialization_fails(self):
        db=Mock()
        db.execute.side_effect=RuntimeError('simulated schema failure')
        with patch.dict(os.environ,{'DATABASE_URL':'','VERCEL':''}),patch('storage.sqlite3.connect',return_value=db):
            with self.assertRaises(RuntimeError):
                with transaction():pass
        db.close.assert_called_once()

    def test_model_timeout_fallback(self):
        with patch.dict(os.environ,{'ANTHROPIC_API_KEY':'fake','ANTHROPIC_MODEL':'test'}),patch('reflection.urlopen',side_effect=TimeoutError):
            self.assertIsNone(generate(new_game(0)))

    def test_failed_login_rate_limit(self):
        for _ in range(10):
            result,_=dispatch(self.db,'login',dict(email='missing@example.test',password='bad-password'), '')
            self.assertIn('error',result)
        result,_=dispatch(self.db,'login',dict(email='missing@example.test',password='bad-password'), '')
        self.assertIn('mange',result['error'])


if __name__=='__main__':unittest.main()
