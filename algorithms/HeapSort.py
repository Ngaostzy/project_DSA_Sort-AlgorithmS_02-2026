import numpy as np

def heapify(a, n, i):
    largest = i
    l = i*2 + 1
    r = i*2 + 2
    if l < n and a[l] > a[largest]:
        largest = l
    if r < n and a[r] > a[largest]:
        largest = r
    if largest != i:
        a[largest], a[i] = a[i], a[largest]
        heapify(a, n, largest)

def heapSort(a):
    n = len(a)
    for i in range((n-1)//2, -1, -1):
        heapify(a, n, i)
    for i in range(n-1,0,-1):
        a[0], a[i] = a[i], a[0]

        heapify(a, i, 0)
        


   