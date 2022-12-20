import random
import numpy as np

# f(x1, x2) = (2 - x1^2) + (1 + x2)^2
n = 50
x1 = np.array([round(random.uniform(-1, 1),3) for _ in range(n)])
x2 = np.array([round(random.uniform(-1, 1), 3) for _ in range(n)])
y = (2 - x1**2) + (1 + x2)**2
s = ""
for i in range(n):
    s += str(x1[i]) + " " + str(x2[i]) + " " + str(round(y[i], 3)) + "\n"

print(s)
