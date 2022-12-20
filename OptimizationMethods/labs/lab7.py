import random
import math


def hipersphere(x, y):
    return -(x ** 2 + y ** 2)


def mod(x):
    return math.sqrt(x[0] ** 2 + x[1] ** 2)


def generate(num):
    population = []
    for i in range(num):
        b = [[random.uniform(-3, 3), random.uniform(-3, 3)]]
        b.append([random.uniform(-1, 1), random.uniform(-1, 1)])
        b.append(hipersphere(b[0][0], b[0][1]))
        population.append(b.copy())
    return population


def chemotaxis(bacteria, lmbd):
    operation = random.randint(0, 1)
    if operation == 0:
        bacteria[0][0] = bacteria[0][0] + lmbd * bacteria[1][0] / (mod(bacteria[1]))
        bacteria[0][0] = bacteria[0][1] + lmbd * bacteria[1][1] / (mod(bacteria[1]))
    else:
        v = [random.uniform(-1, 1), random.uniform(-1, 1)]
        bacteria[0][0] = bacteria[0][0] + lmbd * v[0] / mod(v)
        bacteria[0][1] = bacteria[0][1] + lmbd * v[1] / mod(v)
        bacteria[1] = v
    bacteria[2] += hipersphere(bacteria[0][0], bacteria[0][1])
    return bacteria


def reproduction(bacteries):
    count = len(bacteries)
    bacteries.sort(key=lambda a: a[2], reverse=True)
    bacteries = bacteries[:int(count / 2)]
    bacteries += bacteries.copy()
    return bacteries


def elimination(bacteries, n):
    for i in range(n):
        x = random.randint(0, (len(bacteries) - 1))
        del bacteries[x]
        new_bacteria = generate(1)
        bacteries += (new_bacteria.copy())
    return bacteries


def get_best_solution(bacteries):
    best_solution = [bacteries[0][0].copy()]
    best_solution.append(hipersphere(best_solution[0][0], best_solution[0][1]))
    for bac in bacteries:
        if hipersphere(bac[0][0], bac[0][1]) > best_solution[1]:
            best_solution[0] = bac[0].copy()
            best_solution[1] = hipersphere(bac[0][0], bac[0][1])
    return best_solution


def bacteria_algorithm(num, iterations, lmbd, n, ep):
    population = generate(num)
    current_best = get_best_solution(population)

    global_best = current_best.copy()
    bst = current_best.copy()
    for it in range(iterations):
        if bst[1] <= current_best[1]:
            current_best = bst.copy()
            for i in range(len(population)):
                population[i] = chemotaxis(population[i], lmbd)
            bst = get_best_solution(population)
        else:
            i = random.uniform(0, 1)
            if i > ep:
                population = reproduction(population)
            else:
                population = elimination(population, n)
            bst = get_best_solution(population)
            current_best = bst.copy()

        if global_best[1] < current_best[1]:
            global_best = current_best.copy()
    global_best[1] = -global_best[1]
    return global_best[0]

# bacteria_algorithm(10, 250, 0.1, 5, 0.1)