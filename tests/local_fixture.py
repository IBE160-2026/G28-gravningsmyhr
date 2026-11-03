"""Create disposable local UI identities. Refuses production or cloud databases."""
import os
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from api.index import dispatch
from storage import transaction

if os.environ.get('VERCEL') or os.environ.get('DATABASE_URL'):
    raise SystemExit('Kun lokal testdatabase er tillatt.')
os.environ['BEER_DB']='qa-local.sqlite3'
with transaction() as db:
    for email,role in [('student@example.test','student'),('teacher@example.test','teacher'),('otherteacher@example.test','teacher')]:
        if not any(u['email']==email for u in db['users'].values()):
            dispatch(db,'register',dict(email=email,password='local-fixture-password'), '')
        user=next(u for u in db['users'].values() if u['email']==email)
        user['role']=role
print('Lokale testidentiteter klare. Ingen produksjonsdata er endret.')
