import math
import random
import matplotlib.pyplot as plt
import datetime


class Antibody:
    def __init__(self, x_value, y_value):
        self.x = x_value
        self.y = y_value


class Antigen:
    def __init__(self, x_value, y_value):
        self.x = x_value
        self.y = y_value


ab = [[4.962839362865536, 3.9820617276003656], [2.5844671883527104, 1.9135660997888237], [-0.39768018724216336, -2.4576265565897604], [-3.0247691574893656, -3.4144729250174164], [-3.645195175090267, 0.16510613437367816], [-3.1779974437756464, -0.09853680039819679], [0.33084262463772607, 3.954619077172296], [3.126519754778217, 1.4734491253034374], [0.6448946280206354, -4.164979232329863], [2.302720916881908, -2.441509209494732], [-1.6825225884857273, -1.0225122745687152], [0.5208415499374475, -4.113637880496026], [4.542666066418233, 2.35431544136374], [4.079375722655458, 0.41296101002868735], [-1.62010146557382, -3.885668244593062], [2.0273135268393014, -1.7732093437130092], [0.31220596662483047, 0.9055262318169097], [-4.336180958149312, 1.8628851194625398], [-1.420779135612892, -0.053358024795514325], [-0.41371576627855866, -4.63412799667962], [-4.959299805595208, 0.7914535039464639], [4.969732857388788, 4.269780844544734], [1.8869816253497067, 3.32658674697427], [2.553217493733606, 2.077944933025239], [-2.2735902824958663, 3.9668388533354033], [2.085993433723628, -2.6087264906042664], [0.4653576610170571, 4.442105661231752], [2.9175169215996384, 2.880036343721647], [-1.7978726661375988, -3.9580265521963796], [-3.9321836551229303, 1.8740783292423906], [2.8183026834129423, 3.473196802788358], [-3.417995298685698, 2.3915344265714076], [-2.909287465591226, 3.005382155715882], [-0.166833226843897, -3.6008163322134856], [3.9097111621227185, 3.202664866160548], [2.963408010839311, -3.580602562898656], [-2.05155120171571, 2.1986492092147643], [-2.9090950202241226, -1.179098497852963], [-3.1947757238399808, -1.6036180870184724], [3.4121687681937445, -4.720174194654342], [2.6719930096949804, 4.5978998317435344], [0.4504872098040451, -4.117648385570666], [-4.3156279627387395, 3.164153178075786], [-1.871726722563627, -0.49334193777984225], [4.576508289760181, 2.721797262529238], [-0.9666001245847884, -1.5202557963276297], [-1.6366837665700573, 2.391448107941704], [1.9837199327733623, -0.4235797417746312], [-1.0285984019233831, -3.225062427172103], [0.3292893955026308, -2.6053475721581343], [1.2525396474334158, 2.468539071209089], [-0.8317894256482354, 2.224609139865528], [-4.592520282132422, -4.9776277387311545], [2.5768488168312427, 0.977686032939312], [0.1727795199247497, 3.7684957628327425], [1.188944553980516, -0.7623311783390267], [-4.475155618687791, 2.6282915739378856], [-2.0994955761017655, -4.467021824461761], [-3.0898443855752378, -1.756870508173515], [-1.744250675522939, -2.582506234609041], [3.410466703214846, -2.2925891453291647], [3.671136131521717, 2.5769460146951753], [4.522360522133356, -0.5542422295622078], [4.323195551169581, -1.4079791523880258], [2.6680702416291355, 2.785467094510386], [-0.718703951172218, 1.176548777578553], [-3.949148691563713, -3.6188035672073604], [-0.9640938523567755, -1.991566599511394], [4.159452174422224, 4.296404678482823], [-4.585305360995392, 2.6223172306152804]]
ag = [[-2.5084699377238584, -4.808062921996237], [-2.577382529254705, -4.753020176676261], [4.683711108865946, 1.5231502023361285], [-1.7604352517653545, 0.332740497333857], [-3.6943511657886785, -4.849463572748359], [-3.0923888699991418, 4.9609785849304195], [-4.610255372556255, -2.407371772356103], [4.665188439150347, -0.3665567208047813], [-2.7993207303178402, 0.08584424761709109], [-4.86920125204612, 4.043439985670002]]

class Population:
    def __init__(self):
        self.individuals = None

    def create_population_of_antibodies(self, population_size, a, b):

        self.individuals = [Antibody(i[0], i[1]) for i in ab]
        # print(self.to_list())

    def create_population_of_antigens(self, population_size, a, b):
        self.individuals = [Antigen(i[0], i[1]) for i in ag]
        # print(self.to_list())

    def reduce_population(self, min_affinity, f):
        flag = True
        population_size = len(self.individuals)
        while flag:
            flag = False
            for i in range(population_size):
                for j in range(i + 1, population_size):
                    if self.individuals[i] is not None and self.individuals[j] is not None:
                        if affinity(self.individuals[i], self.individuals[j]) < min_affinity:
                            flag = True
                            if f([self.individuals[i].x, self.individuals[i].y]) < f([self.individuals[j].x, self.individuals[j].y]):
                                self.individuals[j] = None
                            else:
                                self.individuals[i] = None
        self.individuals = list(filter(lambda a: a is not None, self.individuals))

    def to_list(self):
        list_individuals_of_population = []
        for i in self.individuals:
            list_individuals_of_population.append([i.x, i.y])
        return list_individuals_of_population


class ImmuneNetworkAlgorithm:
    def __init__(self, f):
        self.f = f
        self.population_of_antibodies = None
        self.population_of_antigens = None

    def create_memory_cells(self, nb, nc, nd, bb, br):
        for antigen in self.population_of_antigens.individuals:
            best_antibodies = self.get_best_antibodies(antigen, nb)
            population_memory_cells = self.clone_and_mutate(best_antibodies, nc, nd, antigen, bb, br)
            for memory_cells in population_memory_cells.individuals:
                self.population_of_antibodies.individuals.append(memory_cells)
            self.population_of_antibodies.reduce_population(br, self.f)

    def get_best_antibodies(self, antigen, nb):
        population_of_best_antibodies = Population()
        population_of_best_antibodies.individuals = []

        self.population_of_antibodies.individuals.sort(key=lambda x: affinity(x, antigen), reverse=False)

        for i in self.population_of_antibodies.individuals[:nb]:
            population_of_best_antibodies.individuals.append(i)

        return population_of_best_antibodies

    def clone_and_mutate(self, population_of_antibodies, nc, nd, antigen, bb, br):
        clone_population = Population()
        clone_population.individuals = []
        for antibody in population_of_antibodies.individuals:
            clone_population.individuals = []
            alpha = math.exp(-0.1 * affinity(antibody, antigen))
            for c in range(nc):
                clone_population.individuals.append(Antibody(antibody.x + alpha * random.uniform(-0.5, 0.5), antibody.y + alpha * random.uniform(-0.5, 0.5)))

        clone_population.individuals.sort(key=lambda a: affinity(a, antigen), reverse=False)

        population_memory_cells = Population()
        population_memory_cells.individuals = clone_population.individuals[:nd]

        for i in range(nd):
            if affinity(population_memory_cells.individuals[i], antigen) < bb:
                population_memory_cells.individuals = population_memory_cells.individuals[:i]
                break

        population_memory_cells.reduce_population(br, self.f)
        return population_memory_cells

    def immune_network_algorithm(self, a, b, size_population_of_antibodies, size_population_of_antigens, nb, nd, nc, iterations, bb, br):
        # min_point_iteration = []
        # min_time = []
        # time1 = datetime.datetime.now().second * 1000000 + datetime.datetime.now().microsecond

        self.population_of_antibodies = Population()
        self.population_of_antibodies.create_population_of_antibodies(size_population_of_antibodies, a, b)

        self.population_of_antigens = Population()
        self.population_of_antigens.create_population_of_antigens(size_population_of_antigens, a, b)
        # print(self.population_of_antibodies.to_list())

        for i in range(iterations):
            self.create_memory_cells(nb, nc, nd, bb, br)
            # print(self.population_of_antibodies.to_list())

            mn = self.f([self.population_of_antibodies.individuals[0].x, self.population_of_antibodies.individuals[0].y])
        idx = 0
        for ind in range(1, len(self.population_of_antibodies.individuals)):
            if self.f([self.population_of_antibodies.individuals[ind].x, self.population_of_antibodies.individuals[ind].y]) < mn:
                idx = ind
                mn = self.f([self.population_of_antibodies.individuals[ind].x, self.population_of_antibodies.individuals[ind].y])

            # time2 = datetime.datetime.now().second * 1000000 + datetime.datetime.now().microsecond
            # min_point_iteration.append(mn)
            # min_time.append(i)

        # print(min_time)
        # plt.plot(min_time, min_point_iteration)
        # plt.show()
        return [self.population_of_antibodies.individuals[idx].x, self.population_of_antibodies.individuals[idx].y, mn]

def affinity(individual1, individual2):
    return (individual1.x - individual2.x)**2 + (individual1.y - individual2.y)**2

def f(x_k):
    return (x_k[0]**2 + x_k[1] - 11) ** 2 + (x_k[0] + x_k[1]** 2 - 7) ** 2


imm = ImmuneNetworkAlgorithm(f)
imm.immune_network_algorithm(-5, 5, 70, 10, 10, 5, 7, 50, 0.4, 0.4)
