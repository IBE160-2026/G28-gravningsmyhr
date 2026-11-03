"""Optional, bounded server-side model call; no identities are sent."""
import json
import os
from urllib.request import Request, urlopen


def generate(state):
    key, model = os.environ.get('ANTHROPIC_API_KEY'), os.environ.get('ANTHROPIC_MODEL')
    if not key or not model:
        return None
    payload = dict(model=model, max_tokens=500,
                   system='Skriv en kort norsk refleksjon om et Beer Game. Bruk kun de oppgitte tallene. Skill observasjon fra mulig forklaring. Ikke påstå læring eller sikker årsak. Ikke gi karakter.',
                   messages=[dict(role='user', content=json.dumps(dict(role=state['role'], costs=state['cost'], history=state['history'])))])
    request = Request('https://api.anthropic.com/v1/messages', data=json.dumps(payload).encode(),
                      headers={'Content-Type': 'application/json', 'x-api-key': key, 'anthropic-version': '2023-06-01'})
    try:
        with urlopen(request, timeout=15) as response:
            result = json.loads(response.read(32000))
        text = '\n'.join(x['text'] for x in result.get('content', []) if x.get('type') == 'text').strip()
        return text[:5000] if text else None
    except Exception:
        return None
