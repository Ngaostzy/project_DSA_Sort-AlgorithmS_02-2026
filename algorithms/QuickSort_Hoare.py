import sys
import numpy as np

sys.setrecursionlimit(2000000)

def partition(a, start, end):
    pivot = a[(start+end)//2]
    start_counting = start-1
    end_counting = end+1
    while True:
        start_counting +=1
        while a[start_counting] < pivot:
            start_counting+=1
        end_counting -= 1
        while a[end_counting] > pivot:
            end_counting -=1
        if (start_counting >= end_counting): 
            return end_counting
        a[start_counting], a[end_counting] = a[end_counting], a[start_counting]

def Quicksort_Hoare(a, start, end):
    if (start>=end):
        return
    pivot = partition(a, start, end)

    Quicksort_Hoare(a, start, pivot)
    Quicksort_Hoare(a, pivot+1, end)

def quickSort(a):
    Quicksort_Hoare(a, 0, len(a)-1)
