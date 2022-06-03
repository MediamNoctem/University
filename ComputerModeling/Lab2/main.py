import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import numpy as np
from lab2 import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.gridlayout = None
        self.setupUi(self)
        self.pushButton.clicked.connect(self.button1_clicked)
        self.graph = Canvas(self, width=1, height=1, dpi=100)

    def button1_clicked(self):
        mcm = MonteCarloMethod()

        mcm.exercise_1()
        self.graph.axes = self.graph.figure.add_subplot(2, 2, 1)
        self.graph.axes.set_title('Задание 1')
        self.graph.axes.grid(color='lightgray')
        self.graph.axes.plot(mcm.x1, mcm.y1, 'c-', label='y = 10/13 * x')
        self.graph.axes.plot(mcm.x1, mcm.y2, 'c-', label='y = 10*(x - 20)/(-7) + 20')
        self.graph.axes.plot(mcm.x3, mcm.y3, 'c-', label='x = 0')
        self.graph.axes.plot(mcm.xN, mcm.yN, 'r+')
        self.graph.axes.plot(mcm.xM, mcm.yM, 'y*')
        self.graph.axes.legend()

        self.lineEdit.setText(str(round(len(mcm.xM) / len(mcm.xN) * mcm.a1 * mcm.b1, 3)))
        self.lineEdit_2.setText(str(round(340.0 * 22.1 / 14, 3)))

        mcm.exercise_2()
        self.graph.axes = self.graph.figure.add_subplot(2, 2, 2)
        self.graph.axes.set_title('Задание 2')
        self.graph.axes.plot(mcm.x1, mcm.y1, 'c-', label='y = sqrt(29 - 13 * cos^2(x))')
        self.graph.axes.plot(mcm.xN, mcm.yN, 'r+')
        self.graph.axes.plot(mcm.xM, mcm.yM, 'y*')
        self.graph.axes.legend()

        self.lineEdit_4.setText(str(round(len(mcm.xM) / len(mcm.xN) * mcm.a2 * mcm.b2, 3)))
        self.lineEdit_3.setText(str(32.687))

        mcm.exercise_3()
        self.graph.axes = self.graph.figure.add_subplot(2, 2, 3)
        self.graph.axes.set_title('Задание 3')
        self.graph.axes.plot(mcm.x1, mcm.y1, 'c-', label='r^2 = x^2 + y^2')
        self.graph.axes.plot(mcm.xN, mcm.yN, 'r+')
        self.graph.axes.plot(mcm.xM, mcm.yM, 'y*')
        self.graph.axes.legend()

        self.lineEdit_6.setText(str(round(len(mcm.xM) / len(mcm.xN) * 4, 3)))
        self.lineEdit_5.setText(str(3.142))

        mcm.exercise_4()
        self.graph.axes = self.graph.figure.add_subplot(2, 2, 4)
        self.graph.axes.set_title('Задание 4')
        self.graph.axes.plot(mcm.x1, mcm.y1, 'c-', label='p^2 = 23 * cos^2(x) + 3 * sin^2(x)')
        self.graph.axes.plot(mcm.xN, mcm.yN, 'r+')
        self.graph.axes.plot(mcm.xM, mcm.yM, 'y*')
        self.graph.axes.legend()

        self.lineEdit_8.setText(str(round(len(mcm.xM) / len(mcm.xN) * mcm.a3 * mcm.b3 * 4, 3)))
        self.lineEdit_7.setText(str(round(13 * np.pi, 3)))

        self.gridlayout = QGridLayout(self.groupBox_5)
        self.gridlayout.addWidget(self.graph)
        self.show()


class Canvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=1, height=1, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = None
        super(Canvas, self).__init__(fig)


class MonteCarloMethod:
    def __init__(self):
        self.n = 13.0
        self.R = 33
        self.N = 300
        self.a1 = 22.1
        self.b1 = 340.0 / 7.0
        self.a2 = 7.0
        self.b2 = np.sqrt(29.0)
        self.angle = np.linspace(0, 2 * np.pi, self.N)
        self.a3 = 4.8
        self.b3 = 2.571

        self.x1 = []
        self.x3 = []
        self.xN = []
        self.xM = []
        self.y1 = []
        self.y2 = []
        self.y3 = []
        self.yN = []
        self.yM = []

    def f1(self, x):
        return 10.0 / self.n * x

    def f2(self, x):
        return 10.0 * (x - 20.0) / (self.n - 20.0) + 20.0

    def f3(self, x):
        return np.sqrt(29.0 - self.n * (np.cos(x) ** 2))

    def f4(self, angle):
        return self.R * np.sin(angle)

    def f5(self, angle):
        return np.sin(angle) * np.sqrt(23 * (np.cos(angle) ** 2) + 3 * (np.sin(angle) ** 2))

    def generating_uniform_distribution(self, t):
        x = np.random.uniform(0, t, self.N)
        while (abs(x.mean() - t / 2) >= 0.01) or (abs(x.var() - (t ** 2) / 12) >= 0.01):
            x = np.random.uniform(0, t, self.N)
        return x

    def exercise_1(self):
        self.x1 = [i for i in range(23)]
        self.y1 = [self.f1(self.x1[i]) for i in range(len(self.x1))]
        self.y2 = [self.f2(self.x1[i]) for i in range(len(self.x1))]
        self.x3 = [0 for i in range(48)]
        self.y3 = np.linspace(0, self.b1, 48)

        self.xN = self.generating_uniform_distribution(self.a1)
        self.yN = self.generating_uniform_distribution(self.b1)

        self.yM = [self.yN[i] for i in range(len(self.yN)) if (self.yN[i] > self.f1(self.xN[i])) and (self.yN[i] < self.f2(self.xN[i]))]
        self.xM = [self.xN[i] for i in range(len(self.yN)) if (self.yN[i] > self.f1(self.xN[i])) and (self.yN[i] < self.f2(self.xN[i]))]

    def exercise_2(self):
        self.x1 = np.linspace(0, 8, 150)
        self.y1 = [self.f3(self.x1[i]) for i in range(len(self.x1))]

        self.xN = self.generating_uniform_distribution(self.a2)
        self.yN = self.generating_uniform_distribution(self.b2)

        self.yM = [self.yN[i] for i in range(len(self.yN)) if self.yN[i] < self.f3(self.xN[i])]
        self.xM = [self.xN[i] for i in range(len(self.yN)) if self.yN[i] < self.f3(self.xN[i])]

    def exercise_3(self):
        angle = np.linspace(0, 2 * np.pi, self.N)
        self.x1 = self.R * np.cos(angle)
        self.y1 = self.f4(angle)

        self.xN = self.generating_uniform_distribution(self.R * 2) - self.R
        self.yN = self.generating_uniform_distribution(self.R * 2) - self.R

        self.yM = [self.yN[i] for i in range(len(self.yN)) if (self.xN[i] ** 2 + self.yN[i] ** 2) < self.R ** 2]
        self.xM = [self.xN[i] for i in range(len(self.yN)) if (self.xN[i] ** 2 + self.yN[i] ** 2) < self.R ** 2]

    def exercise_4(self):
        self.x1 = np.cos(self.angle) * np.sqrt(23 * (np.cos(self.angle) ** 2) + 3 * (np.sin(self.angle) ** 2))
        self.y1 = self.f5(self.angle)

        self.xN = self.generating_uniform_distribution(self.a3 * 2) - self.a3
        self.yN = self.generating_uniform_distribution(self.b3 * 2) - self.b3

        fi = []

        for i in range(len(self.xN)):
            if self.xN[i] > 0:
                fi.append(np.arctan(self.yN[i] / self.xN[i]))
            else:
                if self.xN[i] < 0:
                    fi.append(np.arctan(self.yN[i] / self.xN[i]) + np.pi)
                else:
                    if self.yN[i] > 0:
                        fi.append(np.pi / 2)
                    else:
                        if self.yN[i] < 0:
                            fi.append(np.pi * 3 / 2)
                        else:
                            fi.append(0)

        self.xM = np.array([self.xN[i] for i in range(len(self.xN)) if (self.xN[i] ** 2 + self.yN[i] ** 2) < (23 * (np.cos(fi[i]) ** 2) + 3 * (np.sin(fi[i]) ** 2))])
        self.yM = np.array([self.yN[i] for i in range(len(self.xN)) if (self.xN[i] ** 2 + self.yN[i] ** 2) < (23 * (np.cos(fi[i]) ** 2) + 3 * (np.sin(fi[i]) ** 2))])


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
