import math
import numpy as np


def norma(x):
    return math.sqrt(np.sum(x ** 2))


class GradientDescent:
    def __init__(self, f, g_f):
        self.f = f
        self.g_f = g_f
        self.x_k = np.array([0.5, 1])
        self.e1 = 0.1
        self.e2 = 0.15
        self.M = 10

    def gradient_descent(self):
        k = 0
        while True:
            gradient = self.g_f(self.x_k)
            if norma(gradient) < self.e1:
                return self.x_k
            else:
                if k >= self.M:
                    return self.x_k
                else:
                    t_k = 0.1
                    while True:
                        x_k_plus_1 = self.x_k - t_k * self.g_f(self.x_k)
                        if self.f(x_k_plus_1) - self.f(self.x_k) < 0:
                            if norma(x_k_plus_1 - self.x_k) < self.e2 and abs(
                                    self.f(x_k_plus_1) - self.f(self.x_k)) < self.e2:
                                return x_k_plus_1
                            else:
                                k += 1
                                self.x_k = x_k_plus_1
                                break
