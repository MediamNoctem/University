import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from lab3 import Ui_MainWindow
from lab3_1 import Ui_Dialog as Lab3_1
from lab3_2 import Ui_Dialog as Lab3_2
from lab3_3 import Ui_Dialog as Lab3_3
from lab3_4 import Ui_Dialog as Lab3_4
from lab3_5 import Ui_Dialog as Lab3_5


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.w = None
        self.setupUi(self)
        self.pushButton.clicked.connect(self.show_new_window)

    def show_new_window(self):
        if self.comboBox.currentIndex() == 0:
            self.w = NewWindow1()

        if self.comboBox.currentIndex() == 1:
            self.w = NewWindow2()

        if self.comboBox.currentIndex() == 2:
            self.w = NewWindow3()

        if self.comboBox.currentIndex() == 3:
            self.w = NewWindow4()

        self.w.show()


class NewWindow1(QtWidgets.QDialog, Lab3_1):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.w = None
        self.setupUi(self)
        self.pushButton.clicked.connect(self.button1_clicked)

    def button1_clicked(self):
        num_num = int(self.lineEdit.text())
        num_digits = len(self.lineEdit_2.text())
        init_num = int(self.lineEdit_2.text())

        ar_num = method_of_squares(num_num, num_digits, init_num)
        ar = ""
        for i in range(num_num):
            ar = ar + str(ar_num[i]) + ", "
        ar = ar[:len(ar) - 2]
        self.w = NewWindow5(ar, ar_num)
        self.w.show()


class NewWindow2(QtWidgets.QDialog, Lab3_2):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.button1_clicked)

    def button1_clicked(self):
        num_num = int(self.lineEdit.text())
        num_digits = len(self.lineEdit_2.text())
        init_num = int(self.lineEdit_2.text())
        kernel = int(self.lineEdit_3.text())

        ar_num = method_of_mult(num_num, num_digits, kernel, init_num)
        ar = ""
        for i in range(num_num):
            ar = ar + str(ar_num[i]) + ", "
        ar = ar[:len(ar) - 2]
        self.w = NewWindow5(ar, ar_num)
        self.w.show()


class NewWindow3(QtWidgets.QDialog, Lab3_3):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.button1_clicked)

    def button1_clicked(self):
        num_num = int(self.lineEdit.text())
        num_digits = len(self.lineEdit_2.text())
        init_num = int(self.lineEdit_2.text())
        _lambda = int(self.lineEdit_3.text())
        m = int(self.lineEdit_4.text())

        ar_num = method_of_congruent(num_num, num_digits, init_num, _lambda, m, 0)
        ar = ""
        for i in range(num_num):
            ar = ar + str(ar_num[i]) + ", "
        ar = ar[:len(ar) - 2]
        self.w = NewWindow5(ar, ar_num)
        self.w.show()


class NewWindow4(QtWidgets.QDialog, Lab3_4):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.button1_clicked)

    def button1_clicked(self):
        num_num = int(self.lineEdit.text())
        num_digits = len(self.lineEdit_2.text())
        init_num = int(self.lineEdit_2.text())
        _lambda = int(self.lineEdit_3.text())
        m = int(self.lineEdit_4.text())
        mu = int(self.lineEdit_5.text())

        ar_num = method_of_congruent(num_num, num_digits, init_num, _lambda, m, mu)
        ar = ""
        for i in range(num_num):
            ar = ar + str(ar_num[i]) + ", "
        ar = ar[:len(ar) - 2]
        self.w = NewWindow5(ar, ar_num)
        self.w.show()


class NewWindow5(QtWidgets.QDialog, Lab3_5):
    def __init__(self, ar, ar_num):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.textEdit.setText(ar)
        self.gridlayout = None
        self.graph = Canvas(self, width=1, height=1, dpi=100)

        self.gridlayout = QGridLayout(self.groupBox)
        self.gridlayout.addWidget(self.graph)

        self.graph.axes.hist(ar_num)


class Canvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=1, height=1, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(Canvas, self).__init__(fig)


def select_middle_n(num, _n):
    return (num // (10 ** round(_n / 2))) % (10 ** _n)


def select_last_n(num, _n):
    return num % (10 ** _n)


def method_of_squares(num_num, num_digits, init_num):
    ar_num = [0 for i in range(num_num)]
    num = init_num
    for i in range(num_num):
        num2 = num ** 2
        _num = select_middle_n(num2, num_digits)
        ar_num[i] = _num / (10 ** num_digits)
        num = _num
    return ar_num


def method_of_mult(num_num, num_digits, kernel, init_num):
    ar_num = [0 for i in range(num_num)]
    num = init_num
    for i in range(num_num):
        num2 = kernel * num
        _num = select_middle_n(num2, num_digits)
        ar_num[i] = _num / (10 ** num_digits)
        num = select_last_n(num2, num_digits)
    return ar_num


def method_of_congruent(num_num, num_digits, init_num, _lambda, m, mu):
    ar_num = [0 for i in range(num_num)]
    num = init_num
    for i in range(num_num):
        num = (_lambda * num + mu) % m
        ar_num[i] = num / (10 ** num_digits)
    return ar_num


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

