# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lab3.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(542, 225)
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(14)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 481, 41))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setEnabled(True)
        self.comboBox.setGeometry(QtCore.QRect(30, 90, 481, 31))
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 160, 121, 41))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Генерация случайных чисел"))
        self.label.setText(_translate("MainWindow", "Выберите метод для генерации случайных чисел."))
        self.comboBox.setCurrentText(_translate("MainWindow", "Метод квадратов"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Метод квадратов"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Метод произведений"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Мультипликативный конгруэнтный метод"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Смешанный конгруэнтный метод"))
        self.pushButton.setText(_translate("MainWindow", "Выбрать"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())