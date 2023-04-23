from math import log
from random import uniform
import networkx as nx

CURRENCY = ['EUR', 'USD', 'AMD', 'GBP', 'KZT', 'RUB', 'CNY']

TRANSFER = {}


def currency_transfer(i, j, start, end):
    TRANSFER[CURRENCY[i] + '/' + CURRENCY[j]
             ] = float(format(uniform(start, end), '.3f'))
    TRANSFER[CURRENCY[j] + '/' + CURRENCY[i]
             ] = float(format(1 / TRANSFER[CURRENCY[i] + '/' + CURRENCY[j]], '.3f'))


def init_graph():
    graph = nx.DiGraph()
    currency_len = len(CURRENCY)

    for i in range(currency_len):
        for j in range(i + 1, currency_len):
            if CURRENCY[i] == 'EUR':
                if j == 1:
                    currency_transfer(i, j, 1, 1.5)
                elif j == 2:
                    currency_transfer(i, j, 410, 430)
                elif j == 3:
                    currency_transfer(i, j, 0.8, 0.9)
                elif j == 4:
                    currency_transfer(i, j, 450, 495)
                elif j == 5:
                    currency_transfer(i, j, 79, 91)
                elif j == 6:
                    currency_transfer(i, j, 7.29, 7.53)
            elif CURRENCY[i] == 'USD':
                if j == 2:
                    currency_transfer(i, j, 387, 392)
                elif j == 3:
                    currency_transfer(i, j, 0.8, 0.85)
                elif j == 4:
                    currency_transfer(i, j, 430, 466)
                elif j == 5:
                    currency_transfer(i, j, 75, 83)
                elif j == 6:
                    currency_transfer(i, j, 6.5, 7)
            elif CURRENCY[i] == 'AMD':
                if j == 3:
                    currency_transfer(i, j, 0.002, 0.004)
                elif j == 4:
                    currency_transfer(i, j, 1.1, 1.5)
                elif j == 5:
                    currency_transfer(i, j, 0.15, 0.21)
                elif j == 6:
                    currency_transfer(i, j, 0.015, 0.02)
            elif CURRENCY[i] == 'GBP':
                if j == 4:
                    currency_transfer(i, j, 516, 570)
                elif j == 5:
                    currency_transfer(i, j, 90, 105)
                elif j == 6:
                    currency_transfer(i, j, 8.2, 9)
            elif CURRENCY[i] == 'KZT':
                if j == 5:
                    currency_transfer(i, j, 0.15, 0.2)
                elif j == 6:
                    currency_transfer(i, j, 0.015, 0.02)
            elif CURRENCY[i] == 'RUB':
                if j == 6:
                    currency_transfer(i, j, 0.07, 0.1)
            a = float(
                format(log(TRANSFER[CURRENCY[i] + '/' + CURRENCY[j]], 2), '.1f'))
            b = float(
                format(log(1 / TRANSFER[CURRENCY[i] + '/' + CURRENCY[j]], 2), '.1f'))
            graph.add_edge(CURRENCY[i], CURRENCY[j], weight=a)
            graph.add_edge(CURRENCY[j], CURRENCY[i], weight=b)
    return graph
