from numpy import random
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider


class Machine:
    def __init__(self):
        self.time_receipt_task = 1
        self.min_setup_time = 0.2
        self.max_setup_time = 0.5
        self.mean_work_time = 0.5
        self.sd_work_time = 0.1
        self.mean_interval_between_breakdowns = 20
        self.sd_interval_between_breakdowns = 2
        self.min_time_to_fix_breakdown = 0.1
        self.max_time_to_fix_breakdown = 0.5
        self.number_detail = 500

    def modeling_operation_machine(self):
        interval_between_tasks = random.exponential(self.time_receipt_task, self.number_detail + 10)
        number_processed_details = 0
        number_breakdowns = 0
        n = 35
        interval_between_breakdowns = random.normal(self.mean_interval_between_breakdowns,
                                                    self.sd_interval_between_breakdowns, n)
        time_to_fix_breakdown = random.uniform(self.min_time_to_fix_breakdown, self.max_time_to_fix_breakdown, n)
        number_details_in_queue = 0

        fig, ax = plt.subplots()
        plt.subplots_adjust(left=0.1, bottom=0.3)

        # Задания.
        y_task = [0 for i in range(self.number_detail + 10)]
        x_task = [0 for i in range(self.number_detail + 10)]
        z = 0

        for i in range(self.number_detail + 10):
            x_task[i] = z + interval_between_tasks[i]
            z = x_task[i]

        plt.grid('grey')

        for i in range(self.number_detail):
            plt.plot([x_task[i], x_task[i]], [0, 1], 'black')
        plt.plot(x_task[0:self.number_detail], y_task[0:self.number_detail], 'kv')

        # Поломки.
        x_breakdown = [0 for i in range(2 * n)]
        z = 0
        for i in range(n):
            x_breakdown[2 * i] = z + interval_between_breakdowns[i]
            x_breakdown[2 * i + 1] = x_breakdown[2 * i] + time_to_fix_breakdown[i]
            z = x_breakdown[2 * i + 1]

        plt.axhline(0, xmin=0, xmax=1)

        while number_processed_details < self.number_detail:
            # Получаем задание.
            # Проверим, есть ли в очереди деталь.
            if number_details_in_queue != 0:
                number_details_in_queue -= 1
            # Генерируем время наладки.
            setup_time = random.uniform(self.min_setup_time, self.max_setup_time)

            # Проверяем, не произойдет ли поломки во время наладки.
            # Поломка начинается до задания, устраняется во время или после наладки.
            if (x_task[number_processed_details] >= x_breakdown[2 * number_breakdowns]) and (
                    x_task[number_processed_details] <= x_breakdown[2 * number_breakdowns + 1]):
                x_task[number_processed_details] = x_breakdown[2 * number_breakdowns + 1]
                number_breakdowns += 1
                continue

            # Поломка начинается во время наладки.
            if (x_task[number_processed_details] < x_breakdown[2 * number_breakdowns]) and (
                    (x_task[number_processed_details] + setup_time) >= x_breakdown[2 * number_breakdowns]):
                plt.fill_between([x_task[number_processed_details], x_breakdown[2 * number_breakdowns]], [0], [0.8],
                                 facecolor='green', alpha=0.5)
                x_task[number_processed_details] = x_breakdown[2 * number_breakdowns + 1]
                number_breakdowns += 1
                continue

            # Если поломки (уже) нет.
            plt.fill_between([x_task[number_processed_details], x_task[number_processed_details] + setup_time], [0],
                             [0.8], facecolor='green', alpha=0.5)

            # Выполнение задания.
            # Генерируем время выполнения задания.
            work_time = random.normal(self.mean_work_time, self.sd_work_time)

            # Проверим на наличие поломки во время выполнения задания.
            if (x_task[number_processed_details] + setup_time < x_breakdown[2 * number_breakdowns]) and (
                    x_task[number_processed_details] + setup_time + work_time >= x_breakdown[2 * number_breakdowns]):
                plt.fill_between([x_task[number_processed_details] + setup_time, x_breakdown[2 * number_breakdowns]],
                                 [0], [0.8], facecolor='grey', alpha=0.5)
                x_task[number_processed_details] = x_breakdown[2 * number_breakdowns + 1]
                number_breakdowns += 1
                continue

            # Если поломки во время выполнения задания (уже) нет.
            plt.fill_between([x_task[number_processed_details] + setup_time,
                              x_task[number_processed_details] + setup_time + work_time], [0], [0.8], facecolor='grey',
                             alpha=0.5)

            # Поломка произошла в состоянии простоя.
            if (number_processed_details + 1 < self.number_detail):
                if (x_task[number_processed_details] + setup_time + work_time < x_breakdown[
                    2 * number_breakdowns]) and (
                        x_task[number_processed_details + 1] > x_breakdown[2 * number_breakdowns + 1]):
                    number_breakdowns += 1

            # Учтем момент, когда при выполнении одного задания, поступает ещё одно задание.
            if (number_processed_details + 1 < self.number_detail):
                if (x_task[number_processed_details] + setup_time + work_time > x_task[number_processed_details + 1]):
                    x_task[number_processed_details + 1] = x_task[number_processed_details] + setup_time + work_time
                    number_details_in_queue += 1

            number_processed_details += 1

        for i in range(number_breakdowns):
            plt.fill_between(x_breakdown[(2 * i): (2 * i + 2)], [0], [0.65], facecolor='red')

        i = number_processed_details
        while (x_task[self.number_detail - 1] + setup_time + work_time >= x_task[i]) and (i < self.number_detail + 9):
            number_details_in_queue += 1
            i += 1

        for i in range(number_details_in_queue):
            plt.plot([x_task[number_processed_details + i], x_task[number_processed_details + i]], [0, 1], 'black')
        plt.plot(x_task[self.number_detail:(self.number_detail + number_details_in_queue)],
                 y_task[self.number_detail:(self.number_detail + number_details_in_queue)], 'kv')

        s = 0
        for i in range(number_breakdowns):
            s += x_breakdown[2 * i + 1] - x_breakdown[2 * i]

        print('Суммарное время поломок: ', s)

        print('Общее время работы: ', x_task[self.number_detail - 1] + setup_time + work_time)

        print('Количество поломок: ', number_breakdowns)

        print('Количество оставшихся деталей в очереди: ', number_details_in_queue)

        plt.axis([-0.5, 5, -0.1, 2])

        axpos = plt.axes([0.1, 0.15, 0.8, 0.05])
        spos = Slider(axpos, 'Pos', -0.1, x_task[self.number_detail - 1] + setup_time + work_time - 3)

        def update(val):
            pos = spos.val
            ax.axis([pos - 0.5, pos + 5, -0.1, 2])
            fig.canvas.draw_idle()

        spos.on_changed(update)
        plt.show()


if __name__ == '__main__':
    m = Machine()
    m.modeling_operation_machine()

