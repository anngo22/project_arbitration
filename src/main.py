import sys

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import networkx as nx

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from bellmanford import bellman_ford
from curgraph import init_graph, TRANSFER

g = init_graph()


class App(QWidget):
    NUM_BUTTONS = ['next', 'stop']

    def __init__(self):
        super(App, self).__init__()
        self.budget = 10.0
        self.initUI()
        font = QFont()
        font.setPointSize(16)

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.center()
        self.setWindowTitle('S Plot')

        grid = QGridLayout()
        self.setLayout(grid)
        self.createVerticalGroupBox()

        buttonLayout = QVBoxLayout()
        buttonLayout.addWidget(self.verticalGroupBox)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        grid.addWidget(self.canvas, 0, 1, 9, 9)
        grid.addLayout(buttonLayout, 0, 0)
        self.btn = QPushButton('start', self)
        self.btn.move(450, 370)
        self.btn.clicked.connect(self.start)
        self.resize(900, 900)
        self.center()
        self.setWindowTitle('Arbitration')
        self.show()

    def createVerticalGroupBox(self):
        self.verticalGroupBox = QGroupBox()

        layout = QVBoxLayout()
        for i in self.NUM_BUTTONS:
            button = QPushButton(i)
            button.setObjectName(i)
            layout.addWidget(button)
            layout.setSpacing(10)
            self.verticalGroupBox.setLayout(layout)
            button.clicked.connect(self.submitCommand)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def stop(self, btn):
        self.figure.clf()
        self.close()

    def submitCommand(self):
        if str(self.sender().objectName()) != 'next':
            eval('self.' + str(self.sender().objectName()) + '(self.btn)')
        else:
            eval('self.' + str(self.sender().objectName()) + '()')

    def iteration(self, budget, g):
        budget = float(budget)
        start_budget = budget
        res = bellman_ford(g, 'RUB')
        if len(res) == 0:
            print("empty")
            return

        for i in range(len(res) - 1):
            v1 = res[i]
            v2 = res[i + 1]
            budget *= TRANSFER[v1 + '/' + v2] ** 2
        budget *= TRANSFER[res[-1] + '/' + res[0]] ** 2
        return (float(format(budget, '.3f')), str(format((budget - start_budget) / start_budget * 100, '.3f')) + '%')

    def drawingGraph(self):
        g = init_graph()
        res = bellman_ford(g, 'RUB')
        pos = nx.circular_layout(g)
        weight = nx.get_edge_attributes(g, 'weight')
        options = {
            'node_color': 'green',
            'node_size': 3500,
            'width': 1,
            'arrowstyle': '-|>',
            'arrowsize': 18,
            'edge_color': 'black',
        }
        nx.draw(g, pos=pos, with_labels=True, **options,
                connectionstyle='arc3, rad = 0.3')
        nx.draw_networkx_edge_labels(
            g, pos=pos, edge_labels=weight, label_pos=0.2)
        options = {
            'nodelist': res,
            'node_color': 'blue',
            'node_size': 3500,
            'width': 1,
            'arrowstyle': '-|>',
            'arrowsize': 18,
            'edge_color': 'black',
        }
        nx.draw(g, pos=pos, with_labels=True, **options,
                connectionstyle='arc3, rad = 0.3')
        nx.draw_networkx_edge_labels(
            g, pos=pos, edge_labels=weight, label_pos=0.2)
        print(*self.iteration(self.budget, g))
        self.canvas.draw_idle()

    def start(self):
        budget, ok = QInputDialog.getText(self, 'Input Dialog',
                                          'Enter amount for bidding:')
        self.budget = budget
        self.btn.hide()
        self.drawingGraph()

    def next(self):
        self.figure.clf()
        self.drawingGraph()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    app.setStyle(QStyleFactory.create("gtk"))
    ex = App()
    ex.show()
    sys.exit(app.exec_())
