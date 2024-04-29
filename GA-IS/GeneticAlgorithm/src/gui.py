import sys
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import networkx as nx
import Darwin_model, de_Vries_model


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.condition_met = None
        self.timer = None
        uic.loadUi("form.ui", self)

        self.label_7.hide()
        self.lineEdit_4.hide()

        self.comboBox_1.activated.connect(self.on_selected)
        self.pushButton_1.clicked.connect(self.button1_clicked)
        self.pushButton_2.clicked.connect(self.button2_clicked)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = None

        self.edges = None
        self.nodes = None
        self.matching = None

    def on_selected(self):
        if self.comboBox_1.currentIndex() == 0:
            self.label_7.hide()
            self.lineEdit_4.hide()
        else:
            if self.comboBox_1.currentIndex() == 1:
                self.label_7.setVisible(1)
                self.lineEdit_4.setVisible(1)

    def button1_clicked(self):
        self.figure.clear()
        self.lineEdit_5.setText('')

        if self.comboBox_1.currentIndex() == 0:
            self.nodes = to_list_nodes(self.textEdit_1.toPlainText())
            self.edges = to_list_edges(self.textEdit_2.toPlainText())

            num_population = int(self.lineEdit_1.text())
            probability = float(self.lineEdit_2.text())
            iterations = int(self.lineEdit_3.text())

            ga = Darwin_model.GeneticAlgorithm(self.edges, num_population, probability)
            ga.generation_initial_population()

            G = nx.Graph()
            G.add_nodes_from(self.nodes)
            G.add_edges_from(self.edges)
            ax = self.figure.add_subplot(111)
            pos = nx.spring_layout(G, seed=33)
            self.matching = ga.search_matching(iterations)
            colors = colorize_matching(self.matching, self.edges)
            # 18c94a
            nx.draw(G, pos=pos, ax=ax, with_labels=True, node_color='#bdbdbd', edge_color=colors, width=5,
                    node_size=800)

        else:
            if self.comboBox_1.currentIndex() == 1:
                self.nodes = to_list_nodes(self.textEdit_1.toPlainText())
                self.edges = to_list_edges(self.textEdit_2.toPlainText())

                num_population = int(self.lineEdit_1.text())
                probability = float(self.lineEdit_2.text())
                iterations = int(self.lineEdit_3.text())
                frequency_disasters = int(self.lineEdit_4.text())

                ga = de_Vries_model.GeneticAlgorithm(self.edges, num_population, probability, frequency_disasters)
                ga.generation_initial_population()

                G = nx.Graph()
                G.add_nodes_from(self.nodes)
                G.add_edges_from(self.edges)
                ax = self.figure.add_subplot(111)
                pos = nx.spring_layout(G, seed=123456)
                self.matching = ga.search_matching(iterations)
                colors = colorize_matching(self.matching, self.edges)
                nx.draw(G, pos=pos, ax=ax, with_labels=True, node_color='#bdbdbd', edge_color=colors, width=5,
                        node_size=800)
       
        layout = QVBoxLayout()
        self.groupBox_2.setLayout(layout)
        layout.addWidget(self.canvas)

        self.canvas.draw()
        self.canvas.update()

        self.lineEdit_5.setText(str(self.matching).replace('\'', ''))

    def button2_clicked(self):
        self.figure.clear()
        self.lineEdit_1.setText("")
        self.lineEdit_2.setText("")
        self.textEdit_1.setText("")
        self.textEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")


def to_list_edges(edges_string):
    edges_list = []
    if (edges_string[0] == '[') and (edges_string[-1] == ']'):
        edges_string = edges_string[1:-1]

        count_1 = edges_string.count('[')
        count_2 = edges_string.count(']')

        if count_1 == count_2:
            while edges_string:
                index_1 = edges_string.find('[')
                index_2 = edges_string.find(']')

                if (index_1 > -1) and (index_2 > -1):
                    edge_string = edges_string[(index_1 + 1): index_2]

                    separator = None
                    if edge_string.find(', ') > -1:
                        separator = ', '
                    else:
                        if edge_string.find(','):
                            separator = ','
                    edges_list.append(edge_string.split(separator))

                edges_string = edges_string[(index_2 + 1):]
    return edges_list


def to_list_nodes(nodes_string):
    nodes_list = []
    if (nodes_string[0] == '[') and (nodes_string[-1] == ']'):
        nodes_string = nodes_string[1:-1]
        separator = None
        if nodes_string.find(', ') > -1:
            separator = ', '
        else:
            if nodes_string.find(','):
                separator = ','
        nodes_list = nodes_string.split(separator)
    return nodes_list


def colorize_matching(matching, edges):
    colors = []
    for i in range(len(edges)):
        if edges[i] in matching:
            colors.append('red')
        else:
            colors.append('black')
    return colors


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
