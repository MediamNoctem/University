import tkinter as tk
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from hypernetx import Hypergraph as HnxHypergraph
import hypernetx as hnx
import networkx as nx


def find_vertex_with_min_degree(graph):
    nodes = graph.nodes()
    degree = graph.number_of_nodes()
    min_vertex = None
    for vertex in nodes:
        degree_vertex = len(list(graph.neighbors(vertex)))
        if degree > degree_vertex:
            degree = degree_vertex
            min_vertex = vertex
    return min_vertex


def find_treewidth_exact(graph):
    n = graph.number_of_nodes()
    if n == 0:
        return 0

    min_width = n

    width = calculate_width_for_removal_order(graph, generate_vertex_removal_orders(graph))

    return min(min_width, width)


def generate_vertex_removal_orders(graph):
    order = []
    graph_copy = graph.copy()
    while len(list(graph_copy.nodes())) != 0:
        min_vertex = find_vertex_with_min_degree(graph_copy)
        order.append(min_vertex)
        graph_copy.remove_node(min_vertex)
    return order


def calculate_width_for_removal_order(graph, removal_order):
    graph_copy = graph.copy()
    max_bag_size = 0

    for vertex in removal_order:
        neighbors = list(graph_copy.neighbors(vertex))

        max_bag_size = max(max_bag_size, len(neighbors) + 1)

        for i in range(len(neighbors)):
            for j in range(i + 1, len(neighbors)):
                if not graph_copy.has_edge(neighbors[i], neighbors[j]):
                    graph_copy.add_edge(neighbors[i], neighbors[j])

        graph_copy.remove_node(vertex)

    return max_bag_size - 1


def convert_hypergraph_to_L_2(hypergraph):
    L_2_edges = []
    for edge in hypergraph:
        for vertex in edge:
            for another_edge in hypergraph:
                if vertex in another_edge:
                    for another_vertex in another_edge:
                        if vertex != another_vertex and {vertex, another_vertex} not in L_2_edges:
                            L_2_edges.append({vertex, another_vertex})
    return L_2_edges


class HypergraphApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.graph_frame = None
        self.manual_hyperedges_input = None
        self.hyperedge_input = None
        self.vertex_input = None

        self.title("Вычисление древовидной ширины гиперграфа")
        self.geometry("800x600")

        self.create_widgets()

    def create_widgets(self):
        input_frame = tk.Frame(self)
        input_frame.pack(pady=10)

        vertex_label = tk.Label(input_frame, text="Количество вершин:")
        vertex_label.pack(side=tk.LEFT)
        self.vertex_input = tk.Spinbox(input_frame, from_=2, to=100, width=5)
        self.vertex_input.pack(side=tk.LEFT, padx=5)

        hyperedge_label = tk.Label(input_frame, text="Количество гиперребер:")
        hyperedge_label.pack(side=tk.LEFT)
        self.hyperedge_input = tk.Spinbox(input_frame, from_=1, to=100, width=5)
        self.hyperedge_input.pack(side=tk.LEFT, padx=5)

        manual_hyperedges_label = tk.Label(input_frame, text="Введите гиперребра вручную (например, {1,2,3}):")
        manual_hyperedges_label.pack(pady=5)
        self.manual_hyperedges_input = tk.Text(input_frame, height=5, width=30)
        self.manual_hyperedges_input.pack()

        generate_button = tk.Button(self, text="Сгенерировать и найти",
                                    command=lambda: self.generate_and_calculate(my_label))
        generate_button.pack(pady=10)

        my_label = tk.Label(self, text="", fg="black")
        my_label.pack()

        self.graph_frame = tk.Frame(self)
        self.graph_frame.pack()

    def generate_and_calculate(self, my_label):
        num_vertices = int(self.vertex_input.get())

        num_hyperedges = int(self.hyperedge_input.get())

        manual_hyperedges_text = self.manual_hyperedges_input.get("1.0", tk.END).strip()

        hyperedges = []

        if manual_hyperedges_text:
            try:
                for line in manual_hyperedges_text.splitlines():
                    hyperedge = set(map(int, line.strip().strip('{}').split(',')))
                    hyperedges.append(hyperedge)

            except ValueError:
                print("Ошибка ввода гиперребер. Убедитесь, что они заданы в правильном формате.")
                return
        else:
            try:
                for i in range(num_hyperedges):
                    hyperedge_size = random.randint(1, min(10, num_vertices))
                    hyperedge = set(random.sample(range(num_vertices), hyperedge_size))
                    if i == num_hyperedges - 1:
                        num_added_vertices = 0
                        not_added_vertices = []
                        for vertex in range(num_vertices):
                            flag = True
                            for edge in hyperedges:
                                if vertex in edge:
                                    flag = False
                                    num_added_vertices += 1
                                    break
                            if flag:
                                not_added_vertices.append(vertex)

                        if not (num_added_vertices == num_vertices or len(not_added_vertices) == 0):
                            hyperedge = set(not_added_vertices)
                    hyperedges.append(hyperedge)
            except ValueError:
                print("Ошибка генерации гиперграфа по заданным количествам вершин и ребер.")
                return

        L_2 = nx.Graph()
        L_2.add_edges_from(convert_hypergraph_to_L_2(hyperedges))

        print("Гиперграф: ", str(hyperedges))

        exact_treewidth = find_treewidth_exact(L_2)
        print("Древовидная ширина графа:", exact_treewidth)

        my_label.config(text=f"Древовидная ширина графа: {exact_treewidth}")

        self.visualize_hypergraph(hyperedges, L_2)

    def visualize_hypergraph(self, hypergraph, L_2_graph):
        for widget in self.graph_frame.winfo_children():
            widget.destroy()

        plt.subplot(1, 2, 1)

        h = HnxHypergraph(hypergraph)

        hnx.drawing.draw(h, with_color=True)

        plt.title('Гиперграф')

        plt.subplot(1, 2, 2)

        nx.draw(L_2_graph,
                with_labels=True,
                node_color='lightgreen',
                node_size=400,
                font_size=10,
                font_weight='bold',
                edge_color='darkgray',
                width=1,
                )

        plt.title('L2-граф')

        figure = plt.gcf()
        canvas = FigureCanvasTkAgg(figure, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        plt.close(figure)


if __name__ == '__main__':
    app = HypergraphApp()
    app.mainloop()
