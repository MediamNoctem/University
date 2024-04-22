import random
import numpy as np


class Chromosome:
    def __init__(self, value):
        self.value = value


class Population:
    def __init__(self):
        self.chromosomes = None

    def print(self):
        s = ""
        for i in self.chromosomes:
            s += str(i.value) + "  "
        print(s)


class GeneticAlgorithm:
    def __init__(self, edges, number_generations, percent_of_best_ones_to_live, frequency_disasters):
        self.population = None
        self.number_generations = number_generations
        self.probability_of_mutation = 0.2
        self.percent_of_best_ones_to_live = percent_of_best_ones_to_live
        self.frequency_disasters = frequency_disasters - 1
        self.num_edges = len(edges)
        self.edges = edges
        self.descendants = None

    def generation_initial_population(self):
        self.population = Population()
        self.population.chromosomes = self.create_new_population()

    def create_new_population(self):
        chromosomes = []
        for _ in range(self.number_generations):
            chromosome = []
            for _ in range(self.num_edges):
                chromosome.append(random.randint(0, 1))
            chromosomes.append(Chromosome(chromosome))
        return chromosomes

    def sort(self):
        list_cardinality_matching = []
        for k in self.population.chromosomes:
            list_cardinality_matching.append(calc_cardinality_matching(self.edges, k.value))

        self.Hoare_sorting(list_cardinality_matching, self.population)
        list_cardinality_matching.reverse()
        self.population.chromosomes.reverse()

    def get_best_members(self):
        self.sort()
        amount_of_best_values = round(len(self.population.chromosomes) * (self.percent_of_best_ones_to_live / 100))
        return self.population.chromosomes[0:amount_of_best_values]

    def crossing_over(self):
        self.descendants = []
        population_length = len(self.population.chromosomes)
        population_chromosome_length = len(self.population.chromosomes[0].value)
        for i in range(self.number_generations):
            chromosome = self.population.chromosomes[random.randint(0, population_length - 1)]
            chromosome_1_value = []
            for c in chromosome.value:
                chromosome_1_value.append(c)
            chromosome_1 = Chromosome(chromosome_1_value)

            chromosome = self.population.chromosomes[random.randint(0, population_length - 1)]
            chromosome_2_value = []
            for c in chromosome.value:
                chromosome_2_value.append(c)
            chromosome_2 = Chromosome(chromosome_2_value)

            x = random.randint(0, population_chromosome_length - 2)
            for j in range(x + 1, population_chromosome_length - 1):
                chromosome_1.value[j], chromosome_2.value[j] = chromosome_2.value[j], chromosome_1.value[j]
            self.descendants.append(chromosome_1)
            self.descendants.append(chromosome_2)

    def mutate(self):
        length_chromosome = len(self.descendants[0].value)
        for i in self.descendants:
            probability = np.random.choice(np.array([0, 1]), 1, p=[1 - self.probability_of_mutation,
                                                                   self.probability_of_mutation])
            x = random.randint(0, length_chromosome - 1)
            if probability:
                if i.value[x]:
                    i.value[x] = 0
                else:
                    i.value[x] = 1
        # length_chromosome = len(self.descendants[0].value)
        # magnitude_mutation = random.randint(0, length_chromosome // 2)
        #
        # for i in self.descendants:
        #     probability = np.random.choice(np.array([0, 1]), 1, p=[1 - self.probability_of_mutation,
        #                                                            self.probability_of_mutation])
        #     if probability:
        #         for m in range(magnitude_mutation):
        #             x = random.randint(0, length_chromosome - 1)
        #
        #             if i.value[x]:
        #                 i.value[x] = 0
        #             else:
        #                 i.value[x] = 1

    def selection(self):
        self.sort()
        self.population.chromosomes = self.population.chromosomes[0:self.number_generations]

    def search_matching(self, iterations):
        self.generation_initial_population()

        for i in range(iterations):
            if (i > 0) and ((i % self.frequency_disasters) == 0):
                self.population.chromosomes = self.population.chromosomes[0:round(len(self.population.chromosomes) * 0.1)]
            self.population.chromosomes = self.get_best_members()
            self.crossing_over()
            self.mutate()
            for j in self.descendants:
                self.population.chromosomes.append(j)
            self.selection()

        return self.population.chromosomes[0].value

    @staticmethod
    def Hoare_sorting(function_values, population):
        left = 0
        right = len(function_values) - 1
        # l2 = None
        # r2 = None
        # pivot_value = None
        lows = []
        highs = []
        lows.append(left)
        highs.append(right)

        while lows:
            left = lows.pop()
            right = highs.pop()
            l2 = left
            r2 = right
            pivot_value = function_values[(left + right) // 2]
            while True:
                while function_values[l2] < pivot_value:
                    l2 += 1
                while function_values[r2] > pivot_value:
                    r2 -= 1
                if l2 <= r2:
                    if function_values[l2] > function_values[r2]:
                        function_values[l2], function_values[r2] = function_values[r2], function_values[l2]
                        population.chromosomes[l2].value, population.chromosomes[r2].value \
                            = population.chromosomes[r2].value, population.chromosomes[l2].value
                    l2 += 1
                    if r2 > 0:
                        r2 -= 1
                if l2 > r2:
                    break
            if l2 < right:
                lows.append(l2)
                highs.append(right)
            if r2 > left:
                lows.append(left)
                highs.append(r2)


def calc_cardinality_matching(list_edges, matching):
    if is_matching(list_edges, matching):
        return matching.count(1)
    else:
        return 0


def is_matching(list_edges, matching):
    nodes_in_matching = []
    for i in range(len(list_edges)):
        if matching[i] == 1:
            if (list_edges[i][0] not in nodes_in_matching) and (list_edges[i][1] not in nodes_in_matching):
                nodes_in_matching.append(list_edges[i][0])
                nodes_in_matching.append(list_edges[i][1])
            else:
                return False
    return True


# edges = [[1, 7], [1, 8], [2, 8], [3, 5], [3, 6], [3, 7], [4, 6]]
# [[1, 7], [1, 8], [2, 8], [3, 5], [3, 6], [3, 7], [4, 6]]
# [[1, 2], [1, 6], [2, 3], [2, 6], [3, 4], [3, 5], [5, 6]]
# ga = GeneticAlgorithm(edges, 100, 30, 50)
# matching = ga.search_matching(200)
# print(matching)
# print(is_matching(edges, matching))
