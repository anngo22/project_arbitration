class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, weight):
        self.graph.append([u, v, weight])

    #def print_arr(self, prev):
        #for i in range(len(prev)):
            #print(i, prev[i])

    def BellmanFord(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0
        neg_cyc = []
        prev = [0] * self.V

        for i in range(self.V - 1):
            for u, v, weight in self.graph:
                if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    prev[v] = u

        for u, v, weight in self.graph:
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                ver = prev[v]
                for i in range(self.V - 1):
                    ver = prev[ver]
                neg_cyc.append(ver)
                ver = prev[ver]
                while ver != neg_cyc[0]:
                    neg_cyc.append(ver)
                    ver = prev[ver]
                if src in neg_cyc:
                    break
                else:
                    neg_cyc = []
        return neg_cyc
        #self.print_arr(neg_cyc)


'''g = Graph(5)
g.add_edge(0, 1, -1)
g.add_edge(1, 2, -3)
g.add_edge(2, 0, -4)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(3, 4, -1)
g.add_edge(4, 3, -3)

g.BellmanFord(3)
from math import log
from random import uniform
currency = ['EUR', 'USD', 'AMD', 'GBP', 'KZT', 'RUB', 'CNY']
len_cur = len(currency)

transfer = {}
g = Graph(0)

for i in range(len_cur):
    for j in range(i + 1, len_cur):
        transfer[currency[i] + '/' + currency[j]] = float(format(uniform(1, 7), '.2f'))
        g.add_edge(i, j, log(transfer[currency[i] + '/' + currency[j]], 2))
        g.add_edge(j, i, log(1 / transfer[currency[i] + '/' + currency[j]], 2))

print(g.BellmanFord(0))'''