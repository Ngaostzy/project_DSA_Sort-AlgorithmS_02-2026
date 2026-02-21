import numpy as np


def merge(a, left, middle, right):
    b = [0] * (right-left +1)
    i = left
    j = middle+1
    count = 0
    while i<= middle and j<=right:
        if (a[i] < a[j]): 
            b[count] = a[i]
            i+=1
        else: 
            b[count] = a[j]
            j+=1 
        count+=1
    while j <= right:
        b[count] = a[j]
        j +=1 
        count +=1
    while i <= middle:
        b[count] = a[i]
        i+=1
        count+=1
    a[left:right+1] = b

def merge_Sort(a, left, right):
    if (left>=right): return
    middle = (left+right)//2
    merge_Sort(a, left, middle)
    merge_Sort(a, middle +1, right)
    merge(a, left, middle ,right)

def mergeSort(a):
    merge_Sort(a, 0, len(a)-1)
        


