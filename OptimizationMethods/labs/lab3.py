import math
import numpy as np
import random


class Chromosome:
    def __init__(self, value):
        self.value = value


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
    def __init__(self, f, a, b, number_generations, percent_of_best_ones_to_live):
        self.a = a
        self.b = b
        self.population_x = None
        self.population_y = None
        self.number_generations = number_generations
        self.probability = 0.00001
        self.percent_of_best_ones_to_live = percent_of_best_ones_to_live
        self.f = f

    def generation_initial_population(self):
        self.population_x = Population()
        self.population_x.chromosomes = self.create_new_population()
        self.population_y = Population()
        self.population_y.chromosomes = self.create_new_population()

    def create_new_population(self):
        return [Chromosome(random.uniform(self.a, self.b)) for i in range(self.number_generations)]

    def get_best_members(self):
        function_values = []
        population_x_length = len(self.population_x.chromosomes)
        for i in range(population_x_length):
            function_values.append(self.f([self.population_x.chromosomes[i].value, self.population_y.chromosomes[i].value]))
        self.Hoare_sorting(function_values, self.population_x, self.population_y)
        amount_of_best_values = round(population_x_length * self.percent_of_best_ones_to_live)
        return self.population_x.chromosomes[0:amount_of_best_values], self.population_y.chromosomes[0:amount_of_best_values]

    def crossing_over(self):
        population_x_length = len(self.population_x.chromosomes)
        for i in range(population_x_length, self.number_generations):
            self.population_x.chromosomes.append(Chromosome((self.population_x.chromosomes[random.randint(0, population_x_length - 1)].value + self.population_x.chromosomes[random.randint(0, population_x_length - 1)].value) // 2))
            self.population_y.chromosomes.append(Chromosome((self.population_y.chromosomes[random.randint(0, population_x_length - 1)].value + self.population_y.chromosomes[random.randint(0, population_x_length - 1)].value) // 2))

    def mutate(self):
        population_x_length = len(self.population_x.chromosomes)
        min_population_x = self.population_x.min()
        min_population_y = self.population_y.min()
        for i in range(population_x_length):
            self.population_x.chromosomes[i].value += min_population_x * random.uniform(0, self.probability)
        for i in range(population_x_length):
            self.population_y.chromosomes[i].value += min_population_y * random.uniform(0, self.probability)

    def get_min_value_index(self):
        function_values = []
        population_x_length = len(self.population_x.chromosomes)
        for i in range(population_x_length):
            function_values.append(self.f([self.population_x.chromosomes[i].value, self.population_y.chromosomes[i].value]))
        return function_values.index(np.min(function_values))

    def get_arguments_of_min_value(self):
        minimum_value_index = self.get_min_value_index()
        return self.population_x.chromosomes[minimum_value_index].value, self.population_y.chromosomes[minimum_value_index].value

    def search_minimum(self, iterations):
        # population = []
        self.generation_initial_population()
        for i in range(iterations):
            self.population_x.chromosomes, self.population_y.chromosomes = self.get_best_members()
            self.crossing_over()
            self.mutate()
        min_point_x, min_point_y = self.get_arguments_of_min_value()
        return min_point_x, min_point_y, self.f([min_point_x, min_point_y])

    @staticmethod
    def Hoare_sorting(function_values, population_x, population_y):
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
                        population_x.chromosomes[l2].value, population_x.chromosomes[r2].value = population_x.chromosomes[r2].value, population_x.chromosomes[l2].value
                        population_y.chromosomes[l2].value, population_y.chromosomes[r2].value = population_y.chromosomes[r2].value, population_y.chromosomes[l2].value
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


def from_range_to_range(x, low1, hight1, low2, hight2):
    return low2 + (hight2 - low2) * (x - low1) / (hight1 - low1)


# f = Function()
# ga = GeneticAlgorithm(f, -1, 4, 100, 0.8)
# print("Rosenbrok Function: ")
# min = ga.search_minimum(100)
# print("Min: " + str(min[0]) + "  " + str(min[1]) + "  " + str(min[2]))