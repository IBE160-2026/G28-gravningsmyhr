"""Deterministic teaching variant. Values in hundredths of cost units."""
from copy import deepcopy

ROLES = ['Detaljist', 'Grossist', 'Distributør', 'Fabrikk']


def new_game(role):
    if type(role) is not int or role not in range(4):
        raise ValueError('Velg en gyldig rolle.')
    return dict(role=role, period=0, rules='g28-v1', history=[], commands={},
                stock=[12]*4, backlog=[0]*4, cost=[0]*4, orders=[], shipments=[])


def prepare(state):
    s = deepcopy(state)
    if s['period'] >= 20:
        raise ValueError('Spillet er avsluttet.')
    t = s['period'] + 1
    incoming = [sum(x['q'] for x in s['shipments'] if x['due'] == t and x['to'] == r) for r in range(4)]
    demand = [4 if t <= 4 else 8] + [sum(x['q'] for x in s['orders'] if x['due'] == t and x['to'] == r) for r in range(1, 4)]
    s['shipments'] = [x for x in s['shipments'] if x['due'] > t]
    s['orders'] = [x for x in s['orders'] if x['due'] > t]
    sent, costs = [], []
    for r in range(4):
        available = s['stock'][r] + incoming[r]
        required = s['backlog'][r] + demand[r]
        q = min(available, required)
        sent.append(q)
        s['stock'][r], s['backlog'][r] = available-q, required-q
        c = (available-q)*50 + (required-q)*100
        costs.append(c)
        s['cost'][r] += c
        if r > 0:
            s['shipments'].append(dict(to=r-1, due=t+2, q=q))
    pipeline = [sum(x['q'] for x in s['shipments'] if x['to'] == r) for r in range(4)]
    row = dict(period=t, incoming=incoming, demand=demand, sent=sent,
               stock=s['stock'][:], backlog=s['backlog'][:], cost=costs, pipeline=pipeline)
    return s, row


def advance(state, quantity, version, command):
    if type(quantity) is not int or not 0 <= quantity <= 100:
        raise ValueError('Bestilling må være et heltall fra 0 til 100.')
    if not isinstance(command, str) or not 8 <= len(command) <= 80:
        raise ValueError('Ugyldig forespørsels-ID.')
    prior = state['commands'].get(command)
    if prior:
        if prior != [version, quantity]:
            raise ValueError('Forespørsels-ID er allerede brukt med annet innhold.')
        return deepcopy(state)
    if type(version) is not int or version != state['period']:
        raise ValueError('Spillet er oppdatert i en annen fane. Last inn på nytt.')
    s, row = prepare(state)
    t = row['period']
    decisions = [min(100, max(0, row['demand'][r]+12-(s['stock'][r]+row['pipeline'][r]-s['backlog'][r]))) for r in range(4)]
    decisions[s['role']] = quantity
    for r, q in enumerate(decisions):
        target = s['shipments'] if r == 3 else s['orders']
        target.append(dict(to=3 if r == 3 else r+1, due=t+2 if r == 3 else t+1, q=q))
    row['decisions'] = decisions
    s['period'] = t
    s['history'].append(row)
    s['commands'][command] = [version, quantity]
    return s


def visible(state, full=False):
    r = state['role']
    base = dict(role=r, period=state['period'], done=state['period'] == 20,
                cost=state['cost'][r], rules=state['rules'])
    if base['done'] or full:
        base.update(history=state['history'], costs=state['cost'])
    else:
        _, row = prepare(state)
        base['current'] = {k: v[r] for k, v in row.items() if isinstance(v, list)}
        base['history'] = [{k: (v[r] if isinstance(v, list) else v) for k, v in x.items()} for x in state['history']]
    return base


def summary(state):
    r = state['role']
    peak = max(state['history'], key=lambda x: x['backlog'][r])
    return (f"Du fullførte 20 perioder som {ROLES[r].lower()}. Din kostnad var {state['cost'][r]/100:.2f} "
            f"kostnadsenheter. Høyeste restordre var {peak['backlog'][r]} i periode {peak['period']}. "
            "Sammenlign bestillinger med kundeetterspørsel i grafen. Leveringstid og bestillingsvalg kan bidra "
            "til svingninger. Tallene alene beviser ikke at du har lært mer eller at én beslutning forårsaket resultatet.")
