import numpy as np

def CountingSortByDigit(a, exp):
    n = len(a)
    out = [0] * n
    count = [0] * 10
    for i in range(n):
        digit = (a[i]//exp)%10
        count[digit]+=1
    for i in range(1, 10):
        count[i] += count[i-1]
    for i in range(n-1,-1, -1):
        digit = (a[i]//exp)%10
        target_index = count[digit]-1
        out[target_index] = a[i]
        count[digit] -=1
    for i in range(n):
        a[i] = out[i]



def radixSort(a):
    exp = 1
    max_val = int(np.max(a))
    while (max_val//exp > 0):
        CountingSortByDigit(a, exp)
        exp *=10
    