import math
import matplotlib.pyplot as plt
import numpy as np


def normRaspr(o, M):
    x = np.arange(M - 3 * o, M + 3 * o, 0.1)
    plt.plot(x, (1 / (o * math.sqrt(2 * math.pi))) * math.e ** (-0.5 * ((x - M) / o) ** 2))
    plt.show()


o1 = 2
M1 = 10
o2 = 1
M2 = 10
o3 = 0.5
M3 = 10
o4 = 1
M4 = 12

normRaspr(o1, M1)
normRaspr(o2, M2)
normRaspr(o3, M3)
normRaspr(o4, M4)
