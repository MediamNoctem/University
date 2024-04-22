# import random
# import sys
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
# from PyQt5.QtCore import QTimer
# from matplotlib.figure import Figure
# import numpy as np
# import matplotlib.pyplot as plt
#
# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         # Создать холст matplotlib
#         self.figure = Figure()
#         self.canvas = FigureCanvas(self.figure)
#
#         # Создать график
#         self.ax = self.figure.add_subplot(111)
#         self.line, = self.ax.plot([], [])
#
#         # Настроить таймер
#         self.timer = QTimer()
#         self.timer.setInterval(10)  # Интервал обновления в миллисекундах
#         self.timer.timeout.connect(self.update_plot)
#         self.timer.start()
#
#         # Макет
#         layout = QVBoxLayout()
#         layout.addWidget(self.canvas)
#         self.setLayout(layout)
#
#     def update_plot(self):
#         # Сгенерировать новые данные
#         x = np.linspace(0, random.randint(1,200) * np.pi, 100)
#         y = np.sin(x)
#
#         # Обновить линию
#         self.line.set_data(x, y)
#
#         # Обновить холст
#         self.canvas.draw()
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     app.exec()

import matplotlib.pyplot as plt
import networkx as nx

G = nx.cubical_graph()
pos = nx.spring_layout(G, seed=3113794652)  # positions for all nodes

# nodes
options = {"edgecolors": "tab:gray", "node_size": 800, "alpha": 0.9}
nx.draw_networkx_nodes(G, pos, nodelist=[0, 1, 2, 3], node_color="tab:red", **options)
nx.draw_networkx_nodes(G, pos, nodelist=[4, 5, 6, 7], node_color="tab:blue", **options)

# edges
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
nx.draw_networkx_edges(
    G,
    pos,
    edgelist=[(0, 1), (1, 2)],
    width=8,
    alpha=0.5,
    edge_color="tab:red",
)
nx.draw_networkx_edges(
    G,
    pos,
    edgelist=[(4, 5), (5, 6), (6, 7), (7, 4)],
    width=8,
    alpha=0.5,
    edge_color="tab:blue",
)


# some math labels
labels = {}
labels[0] = r"$a$"
labels[1] = r"$b$"
labels[2] = r"$c$"
labels[3] = r"$d$"
labels[4] = r"$\alpha$"
labels[5] = r"$\beta$"
labels[6] = r"$\gamma$"
labels[7] = r"$\delta$"
nx.draw_networkx_labels(G, pos, labels, font_size=22, font_color="whitesmoke")

plt.tight_layout()
plt.axis("off")
plt.show()