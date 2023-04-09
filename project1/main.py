from time import sleep
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import networkx as nx
from math import log
from random import uniform
import matplotlib.pyplot as plt

from bellmanford import BellmanFord


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
            # g.add_edge(i, j, a)
            # g.add_edge(j, i, b)
            g.add_edge(currency[i], currency[j], weight=a)
            g.add_edge(currency[j], currency[i], weight=b)
    return g

g = init_g()

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn = QPushButton('start', self)
        self.btn.move(210, 220)
        self.btn.clicked.connect(self.start)

        self.btn.setCheckable(True)
        self.btn.setChecked(False)

        self.resize(500, 500)
        self.center()
        self.setWindowTitle('Arbitration')
        self.show()
        
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def iteration(self, budget, g):
        budget = float(budget)
        start_budget = budget
        res = BellmanFord(g, 'RUB')
        if len(res) == 0:
            print("empty")
            return
        
        options = {
                    'node_color': 'green',
                    'node_size': 3500,
                    'width': 1,
                    'arrowstyle': '-|>',
                    'arrowsize': 18,
                    'edge_color':'black',
                }
        pos = nx.circular_layout(g)
        weight = nx.get_edge_attributes(g,'weight')
        nx.draw(g,pos=pos,  with_labels = True , **options, connectionstyle='arc3, rad = 0.3')
        nx.draw_networkx_edge_labels(g, pos=pos, edge_labels=weight, label_pos=0.2)
        plt.show()

        for i in range(len(res) - 1):
            v1 = res[i]
            v2 = res[i + 1]
            budget *= transfer[v1 + '/' + v2] ** 2
        budget *= transfer[res[-1] + '/' + res[0]] ** 2
        return (float(format(budget, '.3f')), str(format((budget - start_budget) / start_budget * 100, '.3f')) + '%')

    def start(self):
        budget, ok = QInputDialog.getText(self, 'Input Dialog',
                                          'Enter amount for bidding:')
        if ok:
            while self.btn.isChecked:
                g = init_g()
                print(*self.iteration(budget, g))
                sleep(5)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
