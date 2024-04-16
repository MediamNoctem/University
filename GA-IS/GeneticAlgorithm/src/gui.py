import sys
import numpy as np
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

import Darwin_model


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("form.ui", self)
        self.gridlayout = None
        self.f = None
        # self.comboBox_1.activated.connect(self.on_selected)
        self.pushButton_1.clicked.connect(self.button1_clicked)
        self.graph = Canvas(self, width=1, height=1, dpi=100)
        # self.resize(618, 897)

    # def on_selected(self):
    #     self.graph.axes.clear()
    #     if self.comboBox.currentIndex() == 0:
    #         self.label_6.setVisible(1)
    #         self.label_7.setVisible(1)
    #         self.label_8.setVisible(1)
    #
    #         self.lineEdit_5.setVisible(1)
    #         self.lineEdit_6.setVisible(1)
    #         self.lineEdit.setText("f = (1 - x)^2 + 100*(y - x^2)^2")
    #         self.label_9.setText("Количество поколений:")
    #         self.label_10.setText("\nПроцент выживаемости:")
    #         self.label_11.setText("\n\nКоличество итераций:")
    #         self.label_12.hide()
    #         self.lineEdit_10.hide()
    #         self.lineEdit_11.hide()
    #         self.lineEdit_12.hide()
    #         self.label_13.hide()
    #         self.label_14.hide()
    #
    #         self.lineEdit_5.setText("")
    #         self.lineEdit_6.setText("")
    #         self.lineEdit_7.setText("")
    #         self.lineEdit_8.setText("")
    #         self.lineEdit_9.setText("")
    #         self.lineEdit_10.setText("")
    #         self.lineEdit_11.setText("")
    #         self.lineEdit_12.setText("")
    #         self.resize(894, 897)
    #     # else:
    #     #     if self.comboBox.currentIndex() == 1:
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
        self.graph.axes.clear()
        n = 50
        x = np.linspace(-2, 2, n)
        y = np.linspace(-2, 2, n)
        x_y = None
        xgrid, ygrid = np.meshgrid(x, y)

        # self.f = function.Function()

        if self.comboBox.currentIndex() == 0:
            # self.lineEdit_1.setText("")
            # self.lineEdit_2.setText("")
            # self.lineEdit_3.setText("")
            self.textEdit_1.setText("")
            num_nodes = int(self.lineEdit_1.text())
            num_edges = int(self.lineEdit_2.text())

            # Реализовать перевод строки в список ребер
            edges = self.textEdit_1.text()

            num_population = int(self.lineEdit_3.text())
            probability = float(self.lineEdit_4.text())
            iterations = int(self.lineEdit_5.text())
            ga = Darwin_model.GeneticAlgorithm(edges, num_population, probability)
            x_y = ga.search_minimum(iterations)
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
        #         x_y = ps.particle_swarm_method(swarm_size, min_values, max_values, current_velocity_ratio,
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
        #             x_y = immnet.immune_network_algorithm(a, b, size_population_of_antibodies,
        #                                                   size_population_of_antigens, nb, nd, nc,
        #                                                   iterations, 0.4, 0.4)

        zgrid = np.array([self.f([xgrid[i], ygrid[i]]) for i in range(n)])
        self.graph.axes.plot_surface(xgrid, ygrid, zgrid, cmap='viridis', linewidths=0.2, alpha=0.8)
        z = self.f(x_y)
        self.graph.axes.scatter(x_y[0], x_y[1], z, c="r")
        self.lineEdit_2.setText(str(round(x_y[0], 3)))
        self.lineEdit_3.setText(str(round(x_y[1], 3)))
        self.lineEdit_4.setText(str(round(z, 3)))
        self.gridlayout = QGridLayout(self.groupBox)
        self.gridlayout.addWidget(self.graph)
        self.show()


class Canvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=1, height=1, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111, projection='3d')
        super(Canvas, self).__init__(fig)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
