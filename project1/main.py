from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import networkx as nx
from math import log, pow
from random import uniform

from bellmanford import Graph

currency = ['EUR', 'USD', 'AMD', 'GBP', 'KZT', 'RUB', 'CNY']
len_cur = len(currency)

transfer = {}
g = Graph(21)

for i in range(len_cur):
    for j in range(i + 1, len_cur):
        transfer[currency[i] + '/' + currency[j]] = float(format(uniform(1, 7), '.2f'))
        g.add_edge(i, j, log(transfer[currency[i] + '/' + currency[j]], 2))
        g.add_edge(j, i, log(1 / transfer[currency[i] + '/' + currency[j]], 2))


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn = QPushButton('start', self)
        self.btn.move(210, 220)
        self.btn.clicked.connect(self.start)

        self.resize(500, 500)
        self.center()
        self.setWindowTitle('Arbitration')
        self.show()

    '''def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()'''

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def start(self):
        budget, ok = QInputDialog.getText(self, 'Input Dialog',
                                        'Enter amount for bidding:')
        if ok:
            budget = float(budget)
            start_budget = budget
            res = g.BellmanFord(0)
            for i in range(len(res) - 1):
                v1 = res[i]
                v2 = res[i+1]
                budget *= pow(transfer[currency[i] + '/' + currency[i + 1]], 10)
            budget *= pow(transfer[currency[res[-1]] + '/' + currency[res[0]]], 10)
            print(budget, start_budget)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

#print(transfer)
