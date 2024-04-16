import math
import random
import numpy as np


class Chromosome:
    def __init__(self, num_edges):
        self.value = []
        # max_num_nodes_in_matching = math.ceil(num_nodes / 2)
        for i in range(num_edges):
            self.value.append(random.randint(0, 1))


class Population:
    def __init__(self):
        self.chromosomes = None

    def to_list(self):
        list_population = []
        for i in self.chromosomes:
            list_population.append(i.value)
        return list_population

    def min(self):
        min = self.chromosomes[0].value
        for i in self.chromosomes:
            if min > i.value:
                min = i.value
        return min

    def print(self):
        s = ""
        for i in self.chromosomes:
            s += str(i.value) + "  "
        print(s)


class GeneticAlgorithm:
    def __init__(self, edges, number_generations, percent_of_best_ones_to_live):
        self.population = None
        self.number_generations = number_generations
        self.probability_of_mutation = 0.2
        self.percent_of_best_ones_to_live = percent_of_best_ones_to_live
        self.num_edges = len(edges)
        self.edges = edges
        self.descendants = []

    def generation_initial_population(self):
        self.population = Population()
        self.population.chromosomes = self.create_new_population()

    def create_new_population(self):
        return [Chromosome(self.num_edges) for _ in range(self.number_generations)]

    def get_best_members(self):
        list_cardinality_matching = []

        for i in self.population.chromosomes:
            list_cardinality_matching.append(calc_cardinality_matching(self.edges, i.value))

        self.Hoare_sorting(list_cardinality_matching, self.population)

        amount_of_best_values = round(len(self.population.chromosomes) * self.percent_of_best_ones_to_live)
        return self.population.chromosomes[0:amount_of_best_values]

    def crossing_over(self):
        population_length = len(self.population.chromosomes)
        population_chromosome_length = len(self.population.chromosomes[0].value)
        for i in range(self.number_generations):
            chromosomes_1 = self.population.chromosomes[random.randint(0, population_length - 1)]
            chromosomes_2 = self.population.chromosomes[random.randint(0, population_length - 1)]
            x = random.randint(0, population_chromosome_length - 2)
            for j in range(x + 1, population_chromosome_length - 2):
                tmp = chromosomes_1.value[j]
                chromosomes_1.value[j] = chromosomes_2.value[j]
                chromosomes_2 = tmp
            self.descendants.append(chromosomes_1)
            self.descendants.append(chromosomes_2)

    def mutate(self):
        length_chromosome = len(self.population.chromosomes[0].value)
        for i in self.population.chromosomes:
            probability = np.random.choice(np.array([0, 1]), 1, p=[1 - self.probability_of_mutation, self.probability_of_mutation])
            x = random.randint(0, length_chromosome - 1)
            if probability:
                if i.value[x]:
                    i.value[x] = 0
                else:
                    i.value[x] = 1

    def search_matching(self, iterations):
        self.generation_initial_population()
        for i in range(iterations):
            self.population.chromosomes = self.get_best_members()
            self.crossing_over()
            self.mutate()
        self.population.chromosomes = self.get_best_members()
        return self.population.chromosomes[0].value

    @staticmethod
    def Hoare_sorting(function_values, population):
        left = 0
        right = len(function_values) - 1
        l2 = None
        r2 = None
        pivot_value = None
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
                        population.chromosomes[l2].value, population.chromosomes[r2].value = population.chromosomes[r2].value, population.chromosomes[l2].value
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


edges = [[1, 2], [1, 6], [2, 3], [2, 6], [3, 4], [3, 5], [5, 6]]
ga = GeneticAlgorithm(edges, 100, 0.5)
matching = ga.search_matching(500)
print(matching)
