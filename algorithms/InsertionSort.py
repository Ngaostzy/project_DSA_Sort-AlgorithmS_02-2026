import numpy as np

def insertionSort(a):
    n = len(a)
    for i in range(1, n):
        Cur = a[i]
        pos = i-1
        while Cur < a[pos] and pos>=0:
            a[pos+1] = a[pos]
            pos -=1
        a[pos+1] = Cur  

def binary_finding_pos(a, item, low, high):
    while low <= high:
        mid = (low + high)//2

        if a[mid] == item:
            return mid + 1
        if item > a[mid]:
            low = mid + 1
        else: 
            high = mid -1
    return low

def binaryInsertionSort(a):
    n = len(a)
    for i in range(1, n):
        item = a[i]
        j =i -1
        loc = binary_finding_pos(a, item, 0, j)
        while j >= loc:
            a[j+1] = a[j]
            j = j-1
        
        a[loc] = item

def shellSort(a):
    n = len(a)
    gap = n//2
    while (gap > 0):
        for i in range(gap, n):
            temp = a[i]
            j = i
            while j>=gap and a[j-gap] > temp:
                a[j] = a[j-gap]
                j = j - gap
            a[j] = temp

        gap = gap//2



    
