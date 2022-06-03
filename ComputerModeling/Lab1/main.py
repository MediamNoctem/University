import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import numpy as np
from lab1 import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.gridlayout = None
        self.setupUi(self)
        self.pushButton.clicked.connect(self.button1_clicked)
        self.lsm = LeastSquaredMethod()
        self.graph = Canvas(self, width=1, height=1, dpi=100)

    def button1_clicked(self):
        num_points = self.spinBox.value()
        x = self.lineEdit.text()
        y = self.lineEdit_2.text()

        self.lsm.set_num_points(num_points)
        self.lsm.least_squared_method(x, y)

        self.lineEdit_3.setText(make_formula('linear', self.lsm.linear_fun))
        self.lineEdit_4.setText(make_formula('power', self.lsm.power_fun))
        self.lineEdit_5.setText(make_formula('exponential', self.lsm.exponential_fun))
        self.lineEdit_6.setText(make_formula('quadratic', self.lsm.quadratic_fun))

        self.lineEdit_7.setText(str(self.lsm.s1))
        self.lineEdit_8.setText(str(self.lsm.s2))
        self.lineEdit_9.setText(str(self.lsm.s3))
        self.lineEdit_10.setText(str(self.lsm.s4))

        self.lineEdit_11.setText(make_formula(self.lsm.type_approximating_fun, self.lsm.approximating_fun))

        self.graph.axes.grid(color='lightgray')
        self.graph.axes.plot(self.lsm.x, self.lsm.y, 'ro', label='Points')
        self.graph.axes.plot(self.lsm.x, self.lsm.y1, '-', label='Linear')
        self.graph.axes.plot(self.lsm.x, self.lsm.y2, '-', label='Power')
        self.graph.axes.plot(self.lsm.x, self.lsm.y3, '-', label='Exponential')
        self.graph.axes.plot(self.lsm.x, self.lsm.y4, '-', label='Quadratic')
        self.graph.axes.legend()
        self.gridlayout = QGridLayout(self.groupBox_3)
        self.gridlayout.addWidget(self.graph)
        self.show()


class Canvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=1, height=1, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(Canvas, self).__init__(fig)


class LeastSquaredMethod:
    def __init__(self):
        self.num_points = 6
        self.x = [0.0 for i in range(self.num_points)]
        self.y = [0.0 for i in range(self.num_points)]
        self.linear_fun = [0.0 for i in range(2)]
        self.power_fun = [0.0 for i in range(2)]
        self.exponential_fun = [0.0 for i in range(2)]
        self.quadratic_fun = [0.0 for i in range(3)]
        self.approximating_fun = None
        self.type_approximating_fun = None

        self.y1 = [0.0 for i in range(self.num_points)]
        self.y2 = [0.0 for i in range(self.num_points)]
        self.y3 = [0.0 for i in range(self.num_points)]
        self.y4 = [0.0 for i in range(self.num_points)]

        self.s1 = 0.0
        self.s2 = 0.0
        self.s3 = 0.0
        self.s4 = 0.0

    def set_num_points(self, num_points):
        self.num_points = num_points

    def create_arrays(self, a, b):
        self.x = np.fromstring(a, sep=' ', dtype='float')
        self.y = np.fromstring(b, sep=' ', dtype='float')

    def approximating_linear_fun(self, x, y):
        _x = np.array([np.sum(x ** 2), np.sum(x)])
        _y = np.array([np.sum(x), np.array(self.num_points)])
        vector = np.array([np.sum(x * y), np.sum(y)])

        matrix = np.array([_x, _y])
        return np.round(np.linalg.solve(matrix, vector), decimals=3)

    def approximating_power_fun(self, x, y):
        _x = np.log(x)
        _y = np.log(y)
        m = self.approximating_linear_fun(_x, _y)
        self.power_fun = np.round(np.array([m[0], np.exp(m[1])]), decimals=3)

    def approximating_exponential_fun(self, x, y):
        _y = np.log(y)
        m = self.approximating_linear_fun(x, _y)
        self.exponential_fun = np.round(np.array([m[0], np.exp(m[1])]), decimals=3)

    def approximating_quadratic_fun(self, x, y):
        x2 = x ** 2
        x3 = x2 * x
        x4 = x3 * x
        _x = np.array([np.sum(x4), np.sum(x3), np.sum(x2)])
        _y = np.array([np.sum(x3), np.sum(x2), np.sum(x)])
        _z = np.array([np.sum(x2), np.sum(x), np.sum(self.num_points)])
        vector = np.array([np.sum(x2 * y), np.sum(x * y), np.sum(y)])

        matrix = np.array([_x, _y, _z])
        self.quadratic_fun = np.round(np.linalg.solve(matrix, vector), decimals=3)

    def calc_fun_values(self, x, type_fun, fun):
        y = [0.0 for i in range(self.num_points)]
        if type_fun == 'linear':
            y = np.round(fun[0] * x + fun[1], decimals=3)
        else:
            if type_fun == 'power':
                y = np.round(fun[1] * (x ** fun[0]), decimals=3)
            else:
                if type_fun == 'exponential':
                    y = np.round(fun[1] * np.exp(fun[0] * x), decimals=3)
                else:
                    if type_fun == 'quadratic':
                        y = np.round(fun[0] * (x ** 2) + fun[1] * x + fun[2], decimals=3)
        return y

    def calc_error(self, y, _y):
        return np.round(np.sum((_y - y) ** 2), decimals=3)

    def least_squared_method(self, x, y):
        self.create_arrays(x, y)

        self.linear_fun = self.approximating_linear_fun(self.x, self.y)
        self.approximating_power_fun(self.x, self.y)
        self.approximating_exponential_fun(self.x, self.y)
        self.approximating_quadratic_fun(self.x, self.y)

        self.y1 = self.calc_fun_values(self.x, 'linear', self.linear_fun)
        self.y2 = self.calc_fun_values(self.x, 'power', self.power_fun)
        self.y3 = self.calc_fun_values(self.x, 'exponential', self.exponential_fun)
        self.y4 = self.calc_fun_values(self.x, 'quadratic', self.quadratic_fun)

        self.s1 = self.calc_error(self.y, self.y1)
        self.s2 = self.calc_error(self.y, self.y2)
        self.s3 = self.calc_error(self.y, self.y3)
        self.s4 = self.calc_error(self.y, self.y4)

        s_min = np.min([self.s1, self.s2, self.s3, self.s4])

        if s_min == self.s1:
            self.approximating_fun = self.linear_fun
            self.type_approximating_fun = 'linear'
        else:
            if s_min == self.s2:
                self.approximating_fun = self.power_fun
                self.type_approximating_fun = 'power'
            else:
                if s_min == self.s3:
                    self.approximating_fun = self.exponential_fun
                    self.type_approximating_fun = 'exponential'
                else:
                    if s_min == self.s4:
                        self.approximating_fun = self.quadratic_fun
                        self.type_approximating_fun = 'quadratic'


def make_formula(type_fun, fun):
    s = ""
    if type_fun == 'linear':
        if fun[1] < 0:
            sign = ""
        else:
            sign = " + "
        s = "y = " + str(fun[0]) + "*x" + sign + str(fun[1])
    else:
        if type_fun == 'power':
            if fun[0] < 0:
                f2 = "(" + str(fun[0]) + ")"
            else:
                f2 = str(fun[0])
            s = "y = " + str(fun[1]) + "*(x ** " + f2 + ")"
        else:
            if type_fun == 'exponential':
                s = "y = " + str(fun[1]) + "*exp(" + str(fun[0]) + "*x)"
            else:
                if fun[1] < 0:
                    f2_1 = str(fun[1])
                else:
                    f2_1 = " + " + str(fun[1])
                if fun[2] < 0:
                    f2_2 = str(fun[2])
                else:
                    f2_2 = " + " + str(fun[2])
                if type_fun == 'quadratic':
                    s = "y = " + str(fun[0]) + "*(x ** 2)" + f2_1 + "*x" + f2_2
    return s


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

    # x = "1 2 3 4 5 6"
    # y = "1.0 1.5 3.0 4.5 7.0 8.5"

    # x = "10 20 30 40 50 60"
    # y = "1.06 1.33 1.52 1.68 1.81 1.91"
