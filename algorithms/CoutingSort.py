import numpy as np


def countingSort(a):
    max_value = int(np.max(a))
    b = [0] * (max_value + 1)
    for x in a:
        b[x] +=1
    index = 0
    for i in range(max_value +1 ):
        while b[i] > 0:
            a[index] = i
            index += 1
            b[i] -=1
