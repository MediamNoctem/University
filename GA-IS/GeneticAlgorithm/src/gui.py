import sys
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PyQt5.QtCore import QTimer
import networkx as nx
import Darwin_model, de_Vries_model


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("form.ui", self)

        self.label_8.hide()
        self.lineEdit_6.hide()

        self.comboBox_1.activated.connect(self.on_selected)
        self.pushButton_1.clicked.connect(self.button1_clicked)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = None

    def on_selected(self):
        if self.comboBox_1.currentIndex() == 0:
            self.label_8.hide()
            self.lineEdit_6.hide()
            self.lineEdit_1.setText("")
            self.lineEdit_2.setText("")
            self.textEdit_1.setText("")
            self.lineEdit_3.setText("")
            self.lineEdit_4.setText("")
            self.lineEdit_5.setText("")
            self.lineEdit_7.setText("")
        else:
            if self.comboBox_1.currentIndex() == 1:
                self.label_8.setVisible(1)
                self.lineEdit_6.setVisible(1)
                self.lineEdit_1.setText("")
                self.lineEdit_2.setText("")
                self.textEdit_1.setText("")
                self.lineEdit_3.setText("")
                self.lineEdit_4.setText("")
                self.lineEdit_5.setText("")
                self.lineEdit_6.setText("")
                self.lineEdit_7.setText("")
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
        if self.comboBox_1.currentIndex() == 0:
            num_nodes = int(self.lineEdit_1.text())
            num_edges = int(self.lineEdit_2.text())

            # Реализовать перевод строки в список ребер
            edges = self.textEdit_1.text()

            num_population = int(self.lineEdit_3.text())
            probability = float(self.lineEdit_4.text())
            iterations = int(self.lineEdit_5.text())
            ga = Darwin_model.GeneticAlgorithm(edges, num_population, probability)
            ga.generation_initial_population()

            self.timer = QTimer()
            self.timer.setInterval(10)
            self.condition_met = False
            k = 0
            self.timer.timeout.connect(self.update_graph(ga, k, iterations))
            self.timer.start()

            layout = QVBoxLayout()
            self.groupBox_2.setLayout(layout)
            layout.addWidget(self.canvas)
        # else:
        #     if self.comboBox.currentIndex() == 1:
        #         self.lineEdit_2.setText("")
        #         self.lineEdit_3.setText("")
        #         self.lineEdit_4.setText("")
        #         a = float(self.lineEdit_5.text())
        #         b = float(self.lineEdit_6.text())
        #         min_values = np.array([a] * 2)
        #         max_values = np.array([b] * 2)
        #         swarm_size = int(self.lineEdit_7.text())
        #         current_velocity_ratio = float(self.lineEdit_8.text())
        #         local_velocity_ratio = float(self.lineEdit_9.text())
        #         global_velocity_ratio = float(self.lineEdit_10.text())
        #         iterations = int(self.lineEdit_11.text())
        #         ps = lab4.ParticleSwarmMethod()
        #         matching = ps.particle_swarm_method(swarm_size, min_values, max_values, current_velocity_ratio,
        #                                        local_velocity_ratio, global_velocity_ratio, iterations)
        #         self.f = self.f.sphere
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

    def update_graph(self, ga, k, iterations):
        k += 1
        self.figure.clf()
        G = nx.Graph()
        nodes = [1, 2, 3, 4, 5, 6]
        G.add_nodes_from(nodes)
        edges = [[1, 2], [1, 6], [2, 3], [2, 6], [3, 4], [3, 5], [5, 6]]
        G.add_edges_from(edges)
        ax = self.figure.add_subplot(111)
        pos = nx.spring_layout(G, seed=33)
        matching = ga.next_iteration()
        nx.draw(G, pos, ax)

        if k == iterations:
            self.condition_met = True
            self.timer.stop()

        self.canvas.draw()
        # self.canvas.update()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
