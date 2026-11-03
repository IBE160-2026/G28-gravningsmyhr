"""Vercel function and local HTTP handler. No framework dependency locally."""
import hashlib
import hmac
import json
import os
from pathlib import Path
import secrets
import time
from http.cookies import SimpleCookie
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

from game import ROLES, advance, new_game, summary, visible
from storage import transaction
from reflection import generate

ROOT = Path(__file__).resolve().parents[1]


def password_hash(password, salt):
    return hashlib.pbkdf2_hmac('sha256', password.encode(), bytes.fromhex(salt), 300000).hex()


def dispatch(db, action, data, token):
    now = time.time()
    db['sessions'] = {k: v for k, v in db['sessions'].items() if v['expires'] > now}
    session = db['sessions'].get(hashlib.sha256(token.encode()).hexdigest())
    uid = session['uid'] if session else None
    user = db['users'].get(uid)
    if action in ('register', 'login'):
        email = str(data.get('email', '')).strip().lower()
        password = data.get('password', '')
        if not isinstance(password, str) or len(password) < 10 or len(password) > 200 or '@' not in email or len(email) > 200:
            raise ValueError('Bruk en e-postadresse og et passord på 10–200 tegn.')
        rate = db['attempts'].get(email, {'n': 0, 'until': now+600})
        if rate['until'] < now:
            rate = {'n': 0, 'until': now+600}
        if rate['n'] >= 10:
            return {'error': 'For mange forsøk. Vent ti minutter.'}, None
        rate['n'] += 1
        db['attempts'][email] = rate
        found = next((k for k, u in db['users'].items() if u['email'] == email), None)
        if action == 'register':
            if found:
                return {'error': 'Kontoen kan ikke opprettes. Prøv innlogging.'}, None
            found, salt = secrets.token_hex(16), secrets.token_hex(16)
            db['users'][found] = dict(email=email, salt=salt, password=password_hash(password, salt), role='student')
        u = db['users'].get(found)
        salt = u['salt'] if u else '00'*16
        actual = password_hash(password, salt)
        if not u or not hmac.compare_digest(actual, u['password']):
            return {'error': 'Feil e-postadresse eller passord.'}, None
        raw = secrets.token_urlsafe(32)
        db['sessions'][hashlib.sha256(raw.encode()).hexdigest()] = dict(uid=found, expires=now+86400)
        return {'ok': True}, raw
    if action == 'me':
        return {'user': {'email': user['email'], 'role': user['role']} if user else None}, None
    if not user:
        raise PermissionError('Logg inn først.')
    if action == 'logout':
        db['sessions'].pop(hashlib.sha256(token.encode()).hexdigest(), None)
        return {'ok': True}, ''
    if action == 'list':
        games = [dict(id=k, role=g['state']['role'], period=g['state']['period'], cost=sum(g['state']['cost'])) for k, g in db['games'].items() if g['owner'] == uid]
        classes = [dict(id=k, **v) for k, v in db['classes'].items() if v['teacher'] == uid]
        students = [dict(id=k, role=g['state']['role'], period=g['state']['period'], cost=sum(g['state']['cost']), student=db['users'][g['owner']]['email'], classroom=g['classroom']) for k, g in db['games'].items() if g['classroom'] in [c['id'] for c in classes]]
        return dict(games=games, classes=classes, students=students), None
    if action == 'class':
        if user['role'] != 'teacher':
            raise PermissionError('Bare lærer kan opprette klasse.')
        name = str(data.get('name', '')).strip()
        if not 1 <= len(name) <= 80:
            raise ValueError('Skriv et klassenavn på 1–80 tegn.')
        cid = secrets.token_hex(12)
        db['classes'][cid] = dict(name=name, teacher=uid, code=secrets.token_hex(6))
        return {'ok': True}, None
    if action == 'new':
        code = str(data.get('code', '')).strip()
        cid = next((k for k, c in db['classes'].items() if c['code'] == code), None) if code else None
        if code and not cid:
            raise ValueError('Ugyldig klassekode.')
        gid = secrets.token_hex(16)
        db['games'][gid] = dict(owner=uid, classroom=cid, state=new_game(data.get('role')))
        return {'id': gid}, None
    g = db['games'].get(data.get('id'))
    if not g:
        raise PermissionError('Spillet er ikke tilgjengelig.')
    owner = g['owner'] == uid
    classroom = db['classes'].get(g['classroom'])
    teacher = classroom and classroom['teacher'] == uid and user['role'] == 'teacher'
    if not owner and not teacher:
        raise PermissionError('Spillet er ikke tilgjengelig.')
    if action == 'reflect':
        if not owner or g['state']['period'] != 20:
            raise PermissionError('Bare eieren av et avsluttet spill kan be om refleksjon.')
        if not g.get('reflection_attempted'):
            g['reflection_attempted'] = True
            g['reflection'] = generate(g['state'])
    elif action == 'turn':
        if not owner:
            raise PermissionError('Bare spilleren kan bestille.')
        g['state'] = advance(g['state'], data.get('quantity'), data.get('version'), data.get('command'))
    elif action != 'game':
        raise ValueError('Ukjent handling.')
    result = visible(g['state'])
    if not owner and not result['done']:
        result = dict(period=g['state']['period'], role=g['state']['role'], cost=sum(g['state']['cost']), done=False, teacher=True)
    if result['done']:
        result['summary'] = summary(g['state'])
        result['reflection'] = g.get('reflection')
        result['can_reflect'] = owner and not g.get('reflection_attempted') and bool(os.environ.get('ANTHROPIC_API_KEY') and os.environ.get('ANTHROPIC_MODEL'))
    return result, None


class handler(BaseHTTPRequestHandler):
    def route(self):
        url = urlparse(self.path)
        return '/' + parse_qs(url.query)['route'][0].lstrip('/') if 'route' in parse_qs(url.query) else url.path

    def reply(self, code, content, kind='application/json; charset=utf-8', cookie=None):
        body = json.dumps(content, ensure_ascii=False).encode() if kind.startswith('application/json') else content
        self.send_response(code)
        self.send_header('Content-Type', kind)
        self.send_header('Cache-Control', 'no-store')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('Content-Security-Policy', "default-src 'self'; script-src 'self'; style-src 'self'; object-src 'none'; frame-ancestors 'none'; base-uri 'self'")
        if cookie is not None:
            self.send_header('Set-Cookie', f'beer_session={cookie}; Path=/; HttpOnly; SameSite=Strict; Max-Age={86400 if cookie else 0}' + ('; Secure' if os.environ.get('VERCEL') else ''))
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        target = self.route()
        files = {'/': ('index.html', 'text/html'), '/app.js': ('app.js', 'text/javascript'), '/style.css': ('style.css', 'text/css')}
        if target not in files:
            self.reply(404, {'error': 'Ikke funnet.'})
            return
        name, kind = files[target]
        self.reply(200, (ROOT/'public'/name).read_bytes(), kind+'; charset=utf-8')

    def do_POST(self):
        try:
            # A required non-simple header prevents cross-origin form CSRF; no CORS is enabled.
            if self.headers.get('X-Beer-Request') != '1':
                raise PermissionError('Ugyldig forespørsel.')
            size = int(self.headers.get('Content-Length', 0))
            if not 0 < size <= 4096:
                raise ValueError('Ugyldig forespørselstørrelse.')
            data = json.loads(self.rfile.read(size))
            if not isinstance(data, dict):
                raise ValueError('Ugyldig innhold.')
            cookies = SimpleCookie(self.headers.get('Cookie', ''))
            token = cookies['beer_session'].value if 'beer_session' in cookies else ''
            with transaction() as db:
                result, cookie = dispatch(db, self.route().rsplit('/', 1)[-1], data, token)
            self.reply(400 if 'error' in result else 200, result, cookie=cookie)
        except PermissionError as exc:
            self.reply(403, {'error': str(exc)})
        except (ValueError, TypeError, KeyError):
            self.reply(400, {'error': 'Handlingen kunne ikke utføres. Kontroller inndata eller last spillet på nytt.'})
        except Exception:
            self.reply(503, {'error': 'Tjenesten er midlertidig utilgjengelig. Kontroller databaseoppsettet eller prøv igjen.'})

    def log_message(self, *args):
        pass  # No request data or session tokens in logs.
