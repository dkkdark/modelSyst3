import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as sc


o = 2
M = 10

def normFunc(el):
    quad = sc.quad(lambda t: math.e ** (-0.5 * ((t - M) / o) ** 2), 0, el)
    f = (1 / (o * math.sqrt(2 * math.pi))) * quad[0]
    return f


x = np.arange(0, 20, 1)
res = []
for el in x:
    res.append(normFunc(el))

plt.plot(res)
plt.show()
