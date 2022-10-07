import random
import matplotlib.pyplot as plt
import numpy as np

import zd2

eps = 10**-5

def F1(minArg, maxArg, xi):
    min = zd2.normFunc(minArg)
    max = zd2.normFunc(maxArg)
    while abs((max - min) / max) > eps:
        centArg = (maxArg + minArg) / 2
        cent = zd2.normFunc(centArg)
        if cent > xi:
            maxArg = centArg
            max = cent
        else:
            minArg = centArg
            min = cent
    return (minArg + maxArg) / 2


def F2(minArg, maxArg, m):
    min = zd2.normFunc(minArg)
    max = zd2.normFunc(maxArg)
    dY = (max - min) / m
    yTab = []
    xTab = []

    yTab.append(min)
    xTab.append(minArg)
    for i in range(1, m - 1):
        yTab.append(min + dY * i)
        xTab.append(F1(minArg, maxArg, yTab[i]))
    yTab.append(max)
    xTab.append(maxArg)
    return yTab, xTab


def model_n(xTab, yTab, xn):
    res = []
    for x in xn:
        for j in range(1, len(xTab)):
            if yTab[j-1] <= x <= yTab[j]:
                y = ((x - yTab[j])/(yTab[j-1] - yTab[j])) * xTab[j-1] + ((x - yTab[j-1])/(yTab[j] - yTab[j-1])) * xTab[j]
                res.append(int(y))
    return res


print("Task 3")
print("-----------")
def generateNums(n):
    xn = []
    for i in range(n):
        xn.append(random.random())
    yTab, xTab = F2(0, 20, 100)
    res = model_n(xTab, yTab, xn)
    return res


nums1 = generateNums(1000)
print("Числа при 10^3:", nums1)
nums2 = generateNums(10000)
print("Числа при 10^4:", nums2)
nums3 = generateNums(100000)
print("Числа при 10^5:", nums3)
nums4 = generateNums(1000000)
print("Числа при 10^6:", nums4)
print("-----------")
print()

'''
Task 4
'''
print("Task 4")
print("-----------")


def freqNumbers(A, B, m, res):
    S = (B - A) / m
    freq = []
    for i in range(0, m-1):
        freq = [0] * m
        for j in range(0, len(res)):
            t = int(res[j]/S)
            freq[t] = freq[t] + 1
    return freq


fr1 = freqNumbers(0, 20, 20, nums1)
print("Частота при n = 10^3: ", fr1)
fr2 = freqNumbers(0, 20, 20, nums2)
print("Частота при n = 10^4: ", fr2)
fr3 = freqNumbers(0, 20, 20, nums2)
print("Частота при n = 10^5: ", fr3)
fr4 = freqNumbers(0, 20, 20, nums2)
print("Частота при n = 10^6: ", fr4)
print("-----------")


fig, ax = plt.subplots(4, 1)
x = np.arange(1, 21)

ax[0].bar(x, fr1)
ax[1].bar(x, fr2)
ax[2].bar(x, fr3)
ax[3].bar(x, fr4)

fig.set_figwidth(24)
fig.set_figheight(18)
plt.show()
