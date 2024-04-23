import sys
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PyQt5.QtCore import QTimer
import networkx as nx
from functools import partial
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

    #     #
    #     #     else:
    #     #         if self.comboBox.currentIndex() == 2:
    #     #             self.label_6.setVisible(1)
    #     #             self.label_7.setVisible(1)
    #     #             self.label_8.setVisible(1)
    #     #
    #     #             self.lineEdit_5.setVisible(1)
    #     #             self.lineEdit_6.setVisible(1)
    #     #             self.lineEdit.setText("f = (1 - x)^2 + 100*(y - x^2)^2")
    #     #             self.label_9.setText("Размер начальной\nпопуляции антител:")
    #     #             self.label_10.setText("Размер начальной\nпопуляции антигенов:")
    #     #             self.label_11.setText("Количество антител\nдля мутации:")
    #     #             self.label_12.setText("Количество оставляемых\nклонов:")
    #     #             self.label_13.setText("Количество клонов\nклонируемого антитела:")
    #     #             self.label_14.setText("Количество итераций:")
    #     #
    #     #             self.label_12.setVisible(1)
    #     #             self.lineEdit_10.setVisible(1)
    #     #             self.lineEdit_11.setVisible(1)
    #     #             self.lineEdit_12.setVisible(1)
    #     #             self.label_13.setVisible(1)
    #     #             self.label_14.setVisible(1)
    #     #
    #     #             self.lineEdit_5.setText("")
    #     #             self.lineEdit_6.setText("")
    #     #             self.lineEdit_7.setText("")
    #     #             self.lineEdit_8.setText("")
    #     #             self.lineEdit_9.setText("")
    #     #             self.lineEdit_10.setText("")
    #     #             self.lineEdit_11.setText("")
    #     #             self.lineEdit_12.setText("")
    #     #             self.resize(894, 897)

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

            self.canvas.draw()
            self.canvas.update()

            # self.timer = QTimer()
            # self.timer.setInterval(100)
            # self.condition_met = False
            # k = 0
            # # (ga, k, iterations)
            # self.timer.timeout.connect(partial(self.update_graph, ga, k, iterations))
            # self.timer.start()

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
                pos = nx.spring_layout(G, seed=33)
                self.matching = ga.search_matching(iterations)
                colors = colorize_matching(self.matching, self.edges)
                nx.draw(G, pos=pos, ax=ax, with_labels=True, node_color='#bdbdbd', edge_color=colors, width=5,
                        node_size=800)

                self.canvas.draw()
                self.canvas.update()
        #     else:
        #         if self.comboBox.currentIndex() == 2:
        #             self.lineEdit_2.setText("")
        #             self.lineEdit_3.setText("")
        #             self.lineEdit_4.setText("")
        #             self.f = self.f.Rosenbrok
        #             a = float(self.lineEdit_5.text())
        #             b = float(self.lineEdit_6.text())
        #             size_population_of_antibodies = int(self.lineEdit_7.text())
        #             size_population_of_antigens = int(self.lineEdit_8.text())
        #             nb = int(self.lineEdit_9.text())
        #             nd = int(self.lineEdit_10.text())
        #             nc = int(self.lineEdit_11.text())
        #             iterations = int(self.lineEdit_12.text())
        #             immnet = lab6.ImmuneNetworkAlgorithm(self.f)
        #             matching = immnet.immune_network_algorithm(a, b, size_population_of_antibodies,
        #                                                   size_population_of_antigens, nb, nd, nc,
        #                                                   iterations, 0.4, 0.4)

        layout = QVBoxLayout()
        self.groupBox_2.setLayout(layout)
        layout.addWidget(self.canvas)

        self.lineEdit_5.setText(str(self.matching).replace('\'', ''))

    # def update_graph(self, ga, k, iterations):
    #     k += 1
    #     self.figure.clf()
    #     G = nx.Graph()
    #     G.add_nodes_from(self.nodes)
    #     G.add_edges_from(self.edges)
    #     ax = self.figure.add_subplot(111)
    #     pos = nx.spring_layout(G, seed=33)
    #     self.matching = ga.next_iteration()
    #     colors = colorize_matching(self.matching, self.edges)
    #     nx.draw(G, pos=pos, ax=ax, with_labels=True, node_color='#18c94a', edge_color=colors)
    #     if k == iterations:
    #         self.condition_met = True
    #         self.timer.stop()
    #
    #     self.canvas.draw()
    #     self.canvas.update()
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


# def get_nodes_from_list_edges(edges):
#     nodes = []
#     for e in edges:
#         for i in range(len(e)):
#             if e[i] not in nodes:
#                 nodes.append(e[i])
#     return nodes


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
