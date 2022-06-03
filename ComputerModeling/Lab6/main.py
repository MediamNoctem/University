import sys

import PyQt5.QtWidgets
from PyQt5 import QtWidgets
import random
from lab6 import Ui_MainWindow
from lab6_1 import Ui_MainWindow as Lab6_1
from lab6_2 import Ui_MainWindow as Lab6_2


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.w = None
        self.setupUi(self)
        self.pushButton.clicked.connect(self.show_new_window)
        self.pushButton_2.clicked.connect(self.fill_fields)

    def show_new_window(self):
        m = Model(self.lineEdit_12.text(), self.lineEdit.text(), self.lineEdit_4.text(), self.lineEdit_13.text(),
                  self.lineEdit_5.text(), self.lineEdit_14.text(), self.lineEdit_6.text(), self.lineEdit_15.text(),
                  self.lineEdit_8.text(), self.lineEdit_7.text(), self.lineEdit_9.text(), self.lineEdit_11.text(),
                  self.lineEdit_10.text(), self.lineEdit_2.text(), self.lineEdit_3.text())
        if self.lineEdit_12.text() == "1":
            self.show_new_window1(m)
        else:
            self.show_new_window2(m)

    def show_new_window1(self, model):
        self.w = NewWindow1(model)
        self.w.show()

    def show_new_window2(self, model):
        self.w = NewWindow2(model)
        self.w.show()

    def fill_fields(self):
        self.lineEdit.setText("200")

        self.lineEdit_2.setText("3")
        self.lineEdit_3.setText("1")

        self.lineEdit_4.setText("4")
        self.lineEdit_13.setText("1")
        self.lineEdit_5.setText("3")
        self.lineEdit_14.setText("1")
        self.lineEdit_6.setText("5")
        self.lineEdit_15.setText("2")

        self.lineEdit_8.setText("0.4")
        self.lineEdit_7.setText("0.3")
        self.lineEdit_9.setText("0.3")

        self.lineEdit_11.setText("0.3")
        self.lineEdit_10.setText("0.7")


class NewWindow1(QtWidgets.QMainWindow, Lab6_1):
    def __init__(self, model):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        item = PyQt5.QtWidgets.QTableWidgetItem()
        temp_n, res_t_interval, time, done_exs, len_queue_0, len_queue_1, len_queue_2, max_len_queue, all_in_queue, t_prost, sred_t_in_queue = model.model()
        item.setText(str(round(time[0])))
        self.tableWidget.setItem(0, 0, item)

        item.setText(str(t_prost[0] / res_t_interval * 100))
        self.tableWidget.setItem(1, 0, item)

        item.setText(str(time[0] / res_t_interval * 100))
        self.tableWidget.setItem(2, 0, item)

        item.setText(str(done_exs[0]))
        self.tableWidget.setItem(3, 0, item)

        item.setText("-")
        self.tableWidget.setItem(4, 0, item)

        item.setText(str(len_queue_0))
        self.tableWidget.setItem(5, 0, item)

        item.setText(str(max_len_queue[0]))
        self.tableWidget.setItem(6, 0, item)

        item.setText(str(all_in_queue[0]))
        self.tableWidget.setItem(7, 0, item)

        item.setText(str(sred_t_in_queue[0]))
        self.tableWidget.setItem(8, 0, item)

        item.setText(str(time[1]))
        self.tableWidget.setItem(0, 1, item)

        item.setText(str(t_prost[1] / res_t_interval * 100))
        self.tableWidget.setItem(1, 1, item)

        item.setText(str(time[1] / res_t_interval * 100))
        self.tableWidget.setItem(2, 1, item)

        item.setText(str(done_exs[1][0]))
        self.tableWidget.setItem(3, 1, item)

        item.setText(str(done_exs[1][1]))
        self.tableWidget.setItem(4, 1, item)

        item.setText(str(len_queue_1))
        self.tableWidget.setItem(5, 1, item)

        item.setText(str(max_len_queue[1]))
        self.tableWidget.setItem(6, 1, item)

        item.setText(str(all_in_queue[1]))
        self.tableWidget.setItem(7, 1, item)

        item.setText(str(sred_t_in_queue[1]))
        self.tableWidget.setItem(8, 1, item)

        item.setText(str(time[2]))
        self.tableWidget.setItem(0, 2, item)

        item.setText(str(t_prost[2] / res_t_interval * 100))
        self.tableWidget.setItem(1, 2, item)

        item.setText(str(time[2] / res_t_interval * 100))
        self.tableWidget.setItem(2, 2, item)

        item.setText(str(done_exs[2][0]))
        self.tableWidget.setItem(3, 2, item)

        item.setText(str(done_exs[2][1]))
        self.tableWidget.setItem(4, 2, item)

        item.setText(str(len_queue_2))
        self.tableWidget.setItem(5, 2, item)

        item.setText(str(max_len_queue[2]))
        self.tableWidget.setItem(6, 2, item)

        item.setText(str(all_in_queue[2]))
        self.tableWidget.setItem(7, 2, item)

        item.setText(str(sred_t_in_queue[2]))
        self.tableWidget.setItem(8, 2, item)


class NewWindow2(QtWidgets.QMainWindow, Lab6_2):
    def __init__(self, model):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)


class Model:
    def __init__(self, kol, n, t1, t1_r, t2, t2_r, t3, t3_r, p1, p2, p3, p1_2, p1_3, interv, interv_r):
        self.kol = int(kol)
        self.n = int(n)
        self.t1 = float(t1)
        self.t1_range = float(t1_r)
        self.t2 = float(t2)
        self.t2_range = float(t2_r)
        self.t3 = float(t3)
        self.t3_range = float(t3_r)
        self.p1 = float(p1)
        self.p2 = float(p2)
        self.p3 = float(p3)
        self.p1_2 = float(p1_2)
        self.p1_3 = float(p1_3)
        self.interv = float(interv)
        self.interv_range = float(interv_r)

    def choose_t(self, evm):
        if evm == 0:
            return random.uniform(self.t1 - self.t1_range, self.t1 + self.t1_range)
        elif evm == 1:
            return random.uniform(self.t2 - self.t2_range, self.t2 + self.t2_range)
        elif evm == 2:
            return random.uniform(self.t3 - self.t3_range, self.t3 + self.t3_range)

    def model(self):
        global t1, t2
        res_t_interval = 0
        res = [0, 0, 0]
        done_exs = [0, [0, 0], [0, 0]]
        queue = [[], [], []]
        temp_n = 0
        time = [0, 0, 0]
        interval = 0
        max_len_queue = [0, 0, 0]
        all_in_queue = [0, 0, 0]
        sred_t_in_queue = [0, 0, 0]

        while temp_n < self.n:
            t1 = 0
            t2 = [0, 0, 0]

            if temp_n > 0:
                interval = random.uniform(self.interv - self.interv_range, self.interv + self.interv_range)
            res_t_interval += interval
            evm = random.choices([0, 1, 2], weights=[self.p1, self.p2, self.p3])[0]
            to_queue = False

            if res[evm] > res_t_interval or queue[evm] != []:
                queue[evm].append((1, res_t_interval))
                to_queue = True
                all_in_queue[evm] += 1
                if len(queue[evm]) > max_len_queue[evm]:
                    max_len_queue[evm] = len(queue[evm])
            else:
                t1 = self.choose_t(evm)
                time[evm] += t1
                if evm == 0:
                    done_exs[evm] += 1
                else:
                    done_exs[evm][0] += 1
                    temp_n += 1

                res[evm] = res_t_interval + t1

            for i in [0, 1, 2]:
                if temp_n < self.n and queue[i] != [] and res[i] < res_t_interval:
                    t2[i] = self.choose_t(i)
                    time[i] += t2[i]
                    res[i] += t2[i]

                    if queue[i][0][0] == 2:
                        done_exs[i][1] += 1
                    sred_t_in_queue[i] += res_t_interval - queue[i][0][1]
                    del (queue[i][0])

                    if i != 0:
                        done_exs[i][0] += 1
                        temp_n += 1
                    else:
                        done_exs[i] += 1
                        evm2_p = random.choices([1, 2], weights=[self.p1_2, self.p1_3])[0]

                        if res[evm2_p] > res_t_interval - interval + t1:
                            queue[evm2_p].append((2, res_t_interval))
                            all_in_queue[evm2_p] += 1
                            if len(queue[evm2_p]) > max_len_queue[evm2_p]:
                                max_len_queue[evm2_p] = len(queue[evm2_p])
                        else:
                            t21 = self.choose_t(evm2_p)
                            done_exs[evm2_p][1] += 1
                            done_exs[evm2_p][0] += 1
                            time[evm2_p] += t21
                            res[evm2_p] = res_t_interval - interval + t2[i] + t21
                            temp_n += 1
                            t2[i] += t21

            if evm == 0 and to_queue == False:
                evm2 = random.choices([1, 2], weights=[self.p1_2, self.p1_3])[0]

                if res[evm2] > res_t_interval + t1:
                    queue[evm2].append((2, res_t_interval))
                    all_in_queue[evm2] += 1
                    if len(queue[evm2]) > max_len_queue[evm2]:
                        max_len_queue[evm2] = len(queue[evm2])
                elif temp_n < self.n:
                    t11 = self.choose_t(evm2)
                    temp_n += 1
                    done_exs[evm2][1] += 1
                    done_exs[evm2][0] += 1
                    time[evm2] += t11
                    res[evm2] = res_t_interval + t1 + t11
                    t1 += t11

        res_t_interval += max(t1, t2[0], t2[1], t2[2])
        t_prost = [0, 0, 0]
        t_prost[0] = (res_t_interval - time[0]) % res_t_interval
        t_prost[1] = (res_t_interval - time[1]) % res_t_interval
        t_prost[2] = (res_t_interval - time[2]) % res_t_interval
        sred_t_in_queue[0] /= all_in_queue[0]
        sred_t_in_queue[1] /= all_in_queue[1]
        sred_t_in_queue[2] /= all_in_queue[2]
        return temp_n, res_t_interval, time, done_exs, len(queue[0]), len(queue[1]), len(queue[2]), max_len_queue, all_in_queue, t_prost, sred_t_in_queue

    def n_start(self):
        sred_time = [0, 0, 0]
        sred_res_t_interval = 0
        sred_done_exs = [0, [0, 0], [0, 0]]
        sred_t_prost = [0, 0, 0]
        sred_sred_t_in_queue = [0, 0, 0]
        sred_len_queue = [0, 0, 0]
        for i in range(self.kol):
            temp_n, res_t_interval, time, done_exs, len_queue, max_len_queue, all_in_queue, t_prost, sred_t_in_queue = self.model()
            sred_res_t_interval += res_t_interval
            for j in [0, 1, 2]:
                sred_time[j] += time[j]
                sred_t_prost[j] += t_prost[j]
                sred_sred_t_in_queue[j] += sred_t_in_queue[j]
                sred_len_queue[j] += len_queue[j]
                if j != 0:
                    sred_done_exs[j][0] += done_exs[j][0]
                    sred_done_exs[j][1] += done_exs[j][1]
                else:
                    sred_done_exs[j] += done_exs[j]
        for j in [0, 1, 2]:
            sred_time[j] /= self.kol
            sred_t_prost[j] /= sred_res_t_interval
            sred_sred_t_in_queue[j] /= self.kol
            sred_len_queue[j] /= self.kol
            if j != 0:
                sred_done_exs[j][0] /= self.kol
                sred_done_exs[j][1] /= self.kol
            else:
                sred_done_exs[j] /= self.kol

        return sred_res_t_interval / self.kol, sred_time, sred_done_exs, sred_t_prost, sred_sred_t_in_queue, sred_len_queue


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
