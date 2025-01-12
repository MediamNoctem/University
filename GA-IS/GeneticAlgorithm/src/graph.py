import random
import time
import networkx as nx
import Darwin_model, de_Vries_model
import matplotlib.pyplot as plt

list_num_nodes = []
list_time_D = []
list_time_V = []

for num_nodes in range(10, 110, 10):
    print(num_nodes)
    max_num_edges = int(num_nodes * (num_nodes - 1) / 2)
    time_D = 0
    time_V = 0
    for i in range(10):
        print(i)
        num_edges = random.randint(round(max_num_edges / 2), max_num_edges)
        G = nx.gnm_random_graph(num_nodes, num_edges)

        start_time_D = time.time()
        ga_D = Darwin_model.GeneticAlgorithm(list(G.edges), 100, 30)
        matching = ga_D.search_matching(100)
        end_time_D = time.time()
        time_elapsed_D = end_time_D - start_time_D
        time_D += time_elapsed_D

        start_time_V = time.time()
        ga_V = de_Vries_model.GeneticAlgorithm(list(G.edges), 100, 30, 40)
        matching = ga_V.search_matching(100)
        end_time_V = time.time()
        time_elapsed_V = end_time_V - start_time_V
        time_V += time_elapsed_V

    list_num_nodes.append(num_nodes)
    list_time_D.append(time_D / 10)
    list_time_V.append(time_V / 10)

fig, ax = plt.subplots()
ax.plot(list_num_nodes, list_time_D, label="Модель Дарвина", color="#8CCB5E")
ax.plot(list_num_nodes, list_time_V, label="Модель де Фриза", color="#9966CC")

# is_list_num_nodes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# is_list_time = [0.14, 0.38, 0.52, 0.78, 1.01, 1.31, 1.74, 2.04, 2.31, 2.62]
# ax.plot(is_list_num_nodes, is_list_time, label="Иммунная сеть", color="#FFD700")

plt.legend(loc="upper left")

ax.set_title("График зависимости времени выполнения алгоритма от количества вершин")
ax.set_xlabel("Количество вершин")
ax.set_ylabel("Время выполнения алгоритма")
plt.show()

# import networkx as nx
# import Darwin_model, de_Vries_model
# import matplotlib.pyplot as plt
#
# max_len_matching_D = []
# max_len_matching_V = []
# num_iterations = []
#
# num_nodes = 10
# num_edges = 35
# G = nx.gnm_random_graph(num_nodes, num_edges)
# ga_D = Darwin_model.GeneticAlgorithm(list(G.edges), 500, 30)
# ga_V = de_Vries_model.GeneticAlgorithm(list(G.edges), 500, 30, 200)
#
# for iteration in range(10, 211, 50):
#     print(iteration)
#     matching_D = ga_D.search_matching(iteration)
#     matching_V = ga_V.search_matching(iteration)
#
#     max_len_matching_D.append(len(matching_D))
#     max_len_matching_V.append(len(matching_V))
#     num_iterations.append(iteration)
#
# fig, ax = plt.subplots()
# ax.plot(num_iterations, max_len_matching_D, label="Модель Дарвина", color="#8CCB5E")
# ax.plot(num_iterations, max_len_matching_V, label="Модель де Фриза", color="#9966CC")
#
# is_num_iterations = [10, 50, 100, 150, 200]
# is_max_len_matching = [4, 5, 5, 5, 5]
# ax.plot(is_num_iterations, is_max_len_matching, label="Иммунная сеть", color="#FFD700")
#
# plt.legend(loc="upper left")
#
# ax.set_title("График зависимости мощности наибольшего паросочетания от количества итераций")
# ax.set_xlabel("Количество итераций")
# ax.set_ylabel("Мощность наибольшего паросочетания")
# plt.show()
