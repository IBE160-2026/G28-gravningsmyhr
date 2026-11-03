"""Explicit local administration; there is no public role-change endpoint."""
import argparse
from storage import transaction

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('email')
    args = parser.parse_args()
    with transaction() as db:
        user = next((u for u in db['users'].values() if u['email'] == args.email.lower()), None)
        if not user:
            raise SystemExit('Registrer kontoen i appen først.')
        user['role'] = 'teacher'
    print('Lærerrolle tildelt.')
