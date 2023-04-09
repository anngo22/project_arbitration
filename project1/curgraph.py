import networkx as nx
from math import log
from random import uniform


currency = ['EUR', 'USD', 'AMD', 'GBP', 'KZT', 'RUB', 'CNY']

len_cur = len(currency)

transfer = {}


def init_g():
    g = nx.DiGraph()

    for i in range(len_cur):
        for j in range(i + 1, len_cur):
            if currency[i] == 'EUR':
                if j == 1:
                    transfer[currency[i] + '/' + currency[j]
                             ] = float(format(uniform(1, 1.5), '.3f'))
                    transfer[currency[j] + '/' + currency[i]] = float(
                        format(1 / transfer[currency[i] + '/' + currency[j]], '.3f'))
                elif j == 2:
                    transfer[currency[i] + '/' + currency[j]
                             ] = float(format(uniform(410, 430), '.3f'))
                    transfer[currency[j] + '/' + currency[i]] = float(
                        format(1 / transfer[currency[i] + '/' + currency[j]], '.3f'))
                elif j == 3:
                    transfer[currency[i] + '/' + currency[j]
                             ] = float(format(uniform(0.8, 0.9), '.3f'))
                    transfer[currency[j] + '/' + currency[i]] = float(
                        format(1 / transfer[currency[i] + '/' + currency[j]], '.3f'))
                elif j == 4:
                    transfer[currency[i] + '/' + currency[j]
                             ] = float(format(uniform(450, 495), '.3f'))
                    transfer[currency[j] + '/' + currency[i]] = float(
                        format(1 / transfer[currency[i] + '/' + currency[j]], '.3f'))
                elif j == 5:
                    transfer[currency[i] + '/' + currency[j]
                             ] = float(format(uniform(79, 91), '.3f'))
                    transfer[currency[j] + '/' + currency[i]] = float(
                        format(1 / transfer[currency[i] + '/' + currency[j]], '.3f'))
                elif j == 6:
                    transfer[currency[i] + '/' + currency[j]
                             ] = float(format(uniform(7.29, 7.53), '.3f'))
                    transfer[currency[j] + '/' + currency[i]] = float(
                        format(1 / transfer[currency[i] + '/' + currency[j]], '.3f'))
            elif currency[i] == 'USD':
                if j == 2:
                    transfer[currency[i] + '/' + currency[j]
                             ] = float(format(uniform(387, 392), '.3f'))
                    transfer[currency[j] + '/' + currency[i]] = float(
                        format(1 / transfer[currency[i] + '/' + currency[j]], '.3f'))
                elif j == 3:
                    transfer[currency[i] + '/' + currency[j]
                             ] = float(format(uniform(0.8, 0.85), '.3f'))
                    transfer[currency[j] + '/' + currency[i]] = float(
                        format(1 / transfer[currency[i] + '/' + currency[j]], '.3f'))
                elif j == 4:
                    transfer[currency[i] + '/' + currency[j]
                             ] = float(format(uniform(430, 466), '.3f'))
                    transfer[currency[j] + '/' + currency[i]] = float(
                        format(1 / transfer[currency[i] + '/' + currency[j]], '.3f'))
                elif j == 5:
                    transfer[currency[i] + '/' + currency[j]
                             ] = float(format(uniform(75, 83), '.3f'))
                    transfer[currency[j] + '/' + currency[i]] = float(
                        format(1 / transfer[currency[i] + '/' + currency[j]], '.3f'))
                elif j == 6:
                    transfer[currency[i] + '/' + currency[j]
                             ] = float(format(uniform(6.5, 7), '.3f'))
                    transfer[currency[j] + '/' + currency[i]] = float(
                        format(1 / transfer[currency[i] + '/' + currency[j]], '.3f'))
            elif currency[i] == 'AMD':
                if j == 3:
                    transfer[currency[i] + '/' + currency[j]
                             ] = float(format(uniform(0.002, 0.004), '.3f'))
                    transfer[currency[j] + '/' + currency[i]] = float(
                        format(1 / transfer[currency[i] + '/' + currency[j]], '.3f'))
                elif j == 4:
                    transfer[currency[i] + '/' + currency[j]
                             ] = float(format(uniform(1.1, 1.5), '.3f'))
                    transfer[currency[j] + '/' + currency[i]] = float(
                        format(1 / transfer[currency[i] + '/' + currency[j]], '.3f'))
                elif j == 5:
                    transfer[currency[i] + '/' + currency[j]
                             ] = float(format(uniform(0.15, 0.21), '.3f'))
                    transfer[currency[j] + '/' + currency[i]] = float(
                        format(1 / transfer[currency[i] + '/' + currency[j]], '.3f'))
                elif j == 6:
                    transfer[currency[i] + '/' + currency[j]
                         ] = float(format(uniform(0.015, 0.02), '.3f'))
                    transfer[currency[j] + '/' + currency[i]] = float(
                        format(1 / transfer[currency[i] + '/' + currency[j]], '.3f'))
            elif currency[i] == 'GBP':
                if j == 4:
                    transfer[currency[i] + '/' + currency[j]
                            ] = float(format(uniform(516, 570), '.3f'))
                    transfer[currency[j] + '/' + currency[i]] = float(
                        format(1 / transfer[currency[i] + '/' + currency[j]], '.3f'))
                elif j == 5:
                    transfer[currency[i] + '/' + currency[j]
                            ] = float(format(uniform(90, 105), '.3f'))
                    transfer[currency[j] + '/' + currency[i]] = float(
                        format(1 / transfer[currency[i] + '/' + currency[j]], '.3f'))
                elif j == 6:
                    transfer[currency[i] + '/' + currency[j]
                            ] = float(format(uniform(8.2, 9), '.3f'))
                    transfer[currency[j] + '/' + currency[i]] = float(
                        format(1 / transfer[currency[i] + '/' + currency[j]], '.3f'))
            elif currency[i] == 'KZT':
                if j == 5:
                    transfer[currency[i] + '/' + currency[j]
                            ] = float(format(uniform(0.15, 0.2), '.3f'))
                    transfer[currency[j] + '/' + currency[i]] = float(
                        format(1 / transfer[currency[i] + '/' + currency[j]], '.3f'))
                elif j == 6:
                    transfer[currency[i] + '/' + currency[j]
                            ] = float(format(uniform(0.015, 0.02), '.3f'))
                    transfer[currency[j] + '/' + currency[i]] = float(
                        format(1 / transfer[currency[i] + '/' + currency[j]], '.3f'))
            elif currency[i] == 'RUB':
                if j == 6:
                    transfer[currency[i] + '/' + currency[j]
                            ] = float(format(uniform(0.07, 0.1), '.3f'))
                    transfer[currency[j] + '/' + currency[i]] = float(
                        format(1 / transfer[currency[i] + '/' + currency[j]], '.3f'))
            a = float(
                format(log(transfer[currency[i] + '/' + currency[j]], 2), '.1f'))
            b = float(
                format(log(1 / transfer[currency[i] + '/' + currency[j]], 2), '.1f'))
            g.add_edge(currency[i], currency[j], weight=a)
            g.add_edge(currency[j], currency[i], weight=b)
    return g
