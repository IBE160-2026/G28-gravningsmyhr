"""Separate ledger calculator for cross-checking g28-v1, without importing game.py.

The ledger uses fixed-period arrival matrices rather than mutable event queues.
This is an automated second calculation, not human validation of course rules.
"""
ORDERS = [4, 0, 10, 3, 8, 2, 12, 0]


def reference(role):
    arrivals = [[0]*4 for _ in range(24)]
    requests = [[0]*4 for _ in range(24)]
    inventory, shortage = [12]*4, [0]*4
    rows = []
    for t, choice in enumerate(ORDERS, 1):
        requests[t][0] = 4 if t <= 4 else 8
        sent, fee = [], []
        for r in range(4):
            net = inventory[r] + arrivals[t][r] - shortage[r] - requests[t][r]
            delivered = inventory[r] + arrivals[t][r] - max(net, 0)
            inventory[r], shortage[r] = max(net, 0), max(-net, 0)
            sent.append(delivered)
            fee.append(50*inventory[r]+100*shortage[r])
            if r:
                arrivals[t+2][r-1] += delivered
        outstanding = [sum(arrivals[k][r] for k in range(t+1, 24)) for r in range(4)]
        decisions = [max(0, min(100, requests[t][r]+12-inventory[r]-outstanding[r]+shortage[r])) for r in range(4)]
        decisions[role] = choice
        rows.append(dict(period=t, incoming=arrivals[t][:], demand=requests[t][:],
                         sent=sent, stock=inventory[:], backlog=shortage[:],
                         cost=fee, pipeline=outstanding, decisions=decisions))
        for r, amount in enumerate(decisions):
            if r == 3:
                arrivals[t+2][3] += amount
            else:
                requests[t+1][r+1] += amount
    return rows
