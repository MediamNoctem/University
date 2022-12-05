import sys
import numpy as np
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

import lab4
from forms2 import Ui_MainWindow
import lab1
import lab2
import lab3
import function


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.gridlayout = None
        self.f = None
        self.setupUi(self)
        self.comboBox.activated.connect(self.on_selected)
        self.pushButton.clicked.connect(self.button1_clicked)
        self.graph = Canvas(self, width=1, height=1, dpi=100)
        self.resize(618, 897)

    def on_selected(self):
        self.graph.axes.clear()
        if self.comboBox.currentIndex() == 0:
            self.lineEdit.setText("f = 2*x1^2 + x1*x2 + x2^2")
            self.resize(618, 897)
        else:
            if self.comboBox.currentIndex() == 1:
                self.lineEdit.setText("f = 2*x1^2 + 2*x1*x2 + 2*x2^2 - 4*x1 - 6*x2")
                self.resize(618, 897)
            else:
                if self.comboBox.currentIndex() == 2:
                    self.lineEdit.setText("f = (1 - x)^2 + 100*(y - x^2)^2")
                    self.label_9.setText("Количество поколений:")
                    self.label_10.setText("\nПроцент выживаемости:")
                    self.label_11.setText("\n\nКоличество итераций:")
                    self.label_12.hide()
                    self.lineEdit_10.hide()
                    self.lineEdit_11.hide()
                    self.label_13.hide()

                    self.lineEdit_5.setText("")
                    self.lineEdit_6.setText("")
                    self.lineEdit_7.setText("")
                    self.lineEdit_8.setText("")
                    self.lineEdit_9.setText("")
                    self.lineEdit_10.setText("")
                    self.lineEdit_11.setText("")
                    self.resize(894, 897)
                else:
                    if self.comboBox.currentIndex() == 3:
                        self.lineEdit.setText("f = x^2 + y^2")
                        self.label_9.setText("Размер роя:")
                        self.label_10.setText("Коэффициент для\nскорости:")
                        self.label_11.setText("Коэффициент влияния\nлучшей точки от каждой\nчастицы на скорость:")
                        self.label_12.setText("Коэффициент влияния\nлучшей точки от всех\nчастиц на скорость:")
                        self.label_13.setText("Количество итераций:")

                        self.label_12.setVisible(1)
                        self.lineEdit_10.setVisible(1)
                        self.lineEdit_11.setVisible(1)
                        self.label_13.setVisible(1)

                        self.lineEdit_5.setText("")
                        self.lineEdit_6.setText("")
                        self.lineEdit_7.setText("")
                        self.lineEdit_8.setText("")
                        self.lineEdit_9.setText("")
                        self.lineEdit_10.setText("")
                        self.lineEdit_11.setText("")
                        self.resize(894, 897)

    def button1_clicked(self):
        n = 50
        x = np.linspace(-2, 2, n)
        y = np.linspace(-2, 2, n)
        x_y = None
        xgrid, ygrid = np.meshgrid(x, y)

        self.f = function.Function()

        if self.comboBox.currentIndex() == 0:
            g = lab1.GradientDescent(self.f.function1, self.f.gradient_function1)
            x_y = g.gradient_descent()
            self.f = self.f.function1

        else:
            if self.comboBox.currentIndex() == 1:
                sm = lab2.SimplexMethod([[0, 1, 2, 3, 4]])
                x_y = sm.simplex_method([5, 6, 7, 8], [4, 6, 2, 10],
                                        [[[0], [4, 2, 1, 6]], [[1], [2, 4, 2, 6]], [[2], [1, 2, 0, 3]],
                                         [[3], [-1, 0, 0, -1]], [[4], [0, -1, 0, -1]]])
                self.f = self.f.function2
            else:
                if self.comboBox.currentIndex() == 2:
                    a =  float(self.lineEdit_5.text())
                    b =  float(self.lineEdit_6.text())
                    num_population =  int(self.lineEdit_7.text())
                    probability = float(self.lineEdit_8.text())
                    iterations = int(self.lineEdit_9.text())
                    ga = lab3.GeneticAlgorithm(self.f.Rosenbrok, a, b, num_population, probability)
                    x_y = ga.search_minimum(iterations)
                    self.f = self.f.Rosenbrok
                else:
                    if self.comboBox.currentIndex() == 3:
                        a = float(self.lineEdit_5.text())
                        b = float(self.lineEdit_6.text())
                        min_values = np.array ([a] * 2)
                        max_values = np.array ([b] * 2)
                        swarm_size = int(self.lineEdit_7.text())
                        current_velocity_ratio = float(self.lineEdit_8.text())
                        local_velocity_ratio = float(self.lineEdit_9.text())
                        global_velocity_ratio = float(self.lineEdit_10.text())
                        iterations = int(self.lineEdit_11.text())
                        ps = lab4.ParticleSwarmMethod()
                        x_y = ps.particle_swarm_method(swarm_size, min_values, max_values, current_velocity_ratio, local_velocity_ratio, global_velocity_ratio, iterations)
                        self.f = self.f.sphere

        zgrid = np.array([self.f([xgrid[i], ygrid[i]]) for i in range(n)])
        self.graph.axes.plot_surface(xgrid, ygrid, zgrid, cmap='viridis', linewidths=0.2)

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
