import math
import numpy as np


class Function:
    # lab1
    @staticmethod
    def function1(x_k):
        return 2 * x_k[0] * x_k[0] + x_k[0] * x_k[1] + x_k[1] * x_k[1]

    @staticmethod
    def gradient_function1(x_k):
        return np.array([4 * x_k[0] + x_k[1], x_k[0] + 2 * x_k[1]])

    # lab2
    @staticmethod
    def function2(x_k):
        # x_k[0] + 2 * x_k[1]
        # 2 * (x_k[0] ** 2) + 4 * x_k[0] * x_k[1] + 3 * (x_k[1] ** 2) - 6 * x_k[0] - 3 * x_k[1]
        # 2 * (x_k[0] ** 2) + 2 * x_k[0] * x_k[1] + 2 * (x_k[1] ** 2) - 4 * x_k[0] - 6 * x_k[1]
        return 2 * (x_k[0] ** 2) + 2 * x_k[0] * x_k[1] + 2 * (x_k[1] ** 2) - 4 * x_k[0] - 6 * x_k[1]

    # lab3
    @staticmethod
    def Rosenbrok(x_k):
        return (1 - x_k[0]) ** 2 + 100 * (x_k[1] - x_k[0] ** 2) ** 2

    @staticmethod
    def Ackley(x_k):
        return -20 * math.exp(-0.2 * math.sqrt(0.5 * (x_k[0]**2 + x_k[1]**2))) - math.exp(0.5 * (math.cos(2 * math.pi * x_k[0]) + math.cos(2 * math.pi * x_k[1]))) + math.e + 20

    @staticmethod
    def Beal(x_k):
        return pow(1.5 - x_k[0] + x_k[0] * x_k[1], 2) + pow(2.25 - x_k[0] + x_k[0] * x_k[1] * x_k[1], 2) + pow(2.625 - x_k[0] + x_k[0] * x_k[1] * x_k[1] * x_k[1], 2)

    # lab4
    @staticmethod
    def sphere(x_k):
        return x_k[0]**2 + x_k[1]**2
