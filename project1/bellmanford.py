from typing import List

currency = ['EUR', 'USD', 'AMD', 'GBP', 'KZT', 'RUB', 'CNY']


def BellmanFord(G, src) -> List[float]:
    dist = {}
    prev = {}
    for cur in currency:
        prev[cur] = ''
        if cur != src:
            dist[cur] = float('inf')
        else:
            dist[src] = 0
    neg_cyc = []

    for i in range(6):
        for u, v in G.edges:
            if dist[u] != float('inf') and dist[u] + G.get_edge_data(u, v)['weight'] < dist[v]:
                dist[v] = dist[u] + G.get_edge_data(u, v)['weight']
                prev[v] = u

    for u, v in G.edges:
        if dist[u] != float('inf') and dist[u] + G.get_edge_data(u, v)['weight'] < dist[v]:
            ver = prev[v]
            for i in range(6):
                ver = prev[ver]
            neg_cyc.append(ver)
            ver = prev[ver]
            while ver != neg_cyc[0]:
                neg_cyc.append(ver)
                ver = prev[ver]
            break
    return neg_cyc
