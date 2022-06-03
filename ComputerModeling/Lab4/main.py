import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import numpy as np
from lab4 import Ui_MainWindow
from lab4_1 import Ui_Dialog as Lab4_1


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.w = None
        self.setupUi(self)
        self.pushButton.clicked.connect(self.show_new_window1)
        self.pushButton_2.clicked.connect(self.show_new_window2)

    def show_new_window1(self):
        self.w = NewWindow(int(self.lineEdit.text()), 1)
        self.w.show()

    def show_new_window2(self):
        self.w = NewWindow(int(self.lineEdit.text()), 2)
        self.w.show()


class NewWindow(QtWidgets.QDialog, Lab4_1):
    def __init__(self, num_points, flag):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.gridlayout = None
        self.graph = Canvas(self, width=1, height=1, dpi=100)

        self.gridlayout = QGridLayout(self.groupBox)
        self.gridlayout.addWidget(self.graph)

        t = np.array([0.1 * i for i in range(num_points)])

        if flag == 1:
            x, y = rk4(num_points, 3, 0, f1_x, f1_y)
            x_, y_ = f1(t)
        else:
            x, y = rk4(num_points, 2, 2, f2_x, f2_y)
            x_, y_ = f2(t)

        self.graph.axes.plot(t, x_, label='Точное решение X')
        self.graph.axes.plot(t, y_, label='Точное решение Y')
        self.graph.axes.plot(t, x, label='Численное решение X методом Рунге-Кутта 4-го порядка')
        self.graph.axes.plot(t, y, label='Численное решение Y методом Рунге-Кутта 4-го порядка')
        self.graph.axes.legend()


class Canvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=1, height=1, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(Canvas, self).__init__(fig)


def f1(t):
    return 4 * np.exp(-t) - np.exp(2 * t), np.exp(-t) - np.exp(2 * t)


def f2(t):
    return np.exp(2 * t) + 1, 2 * np.exp(2 * t)


def f1_x(x, y):
    return -2 * x + 4 * y


def f1_y(x, y):
    return -x + 3 * y


def f2_x(x, y):
    return y


def f2_y(x, y):
    return 2 * y


def clarify_error(k1, k2, k3):
    try:
        q = abs((k2 - k3) / (k1 - k2))
        if q > 0.1:
            return -1
        if q < 0.1:
            return 1
        return 0
    finally:
        return 0


def rk4(num_points, x0, y0, f_x, f_y):
    h = 0.1
    x = [x0]
    y = [y0]

    i = 0

    while i < num_points - 1:
        k1 = h * f_x(x[i], y[i])
        l1 = h * f_y(x[i], y[i])

        k2 = h * f_x(x[i] + 0.5 * k1, y[i] + 0.5 * l1)
        l2 = h * f_y(x[i] + 0.5 * k1, y[i] + 0.5 * l1)

        k3 = h * f_x(x[i] + 0.5 * k2, y[i] + 0.5 * l2)
        l3 = h * f_y(x[i] + 0.5 * k2, y[i] + 0.5 * l2)

        k4 = h * f_x(x[i] + k3, y[i] + l3)
        l4 = h * f_y(x[i] + k3, y[i] + l3)

        if clarify_error(k1, k2, k3) == -1 or clarify_error(l1, l2, l3) == -1:
            h = h / 2.0
        else:
            if clarify_error(k1, k2, k3) == 1 or clarify_error(k1, k2, k3) == 1:
                h = h * 2.0
            else:
                x.append(x[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6)
                y.append(y[i] + (l1 + 2 * l2 + 2 * l3 + l4) / 6)
                i += 1
    return x, y


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
