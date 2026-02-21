import numpy as np
import sys

sys.setrecursionlimit(2000000)

from algorithms.Bubblesort import bubbleSort
from algorithms.CoutingSort import countingSort
from algorithms.HeapSort import heapSort
from algorithms.InsertionSort import shellSort
from algorithms.InsertionSort import binaryInsertionSort
from algorithms.MergeSort import mergeSort
from algorithms.QuickSort_Hoare import quickSort
from algorithms.RadixSort import radixSort

from benchmarks.compare_time import compare_multiple_algorithms



if __name__ == "__main__":
    int_only_algorithms = [
        ("Counting Sort", countingSort),
        ("Radix Sort", radixSort),
    ]
    slow_algorithms = [
        ("Binary Insertion Sort", binaryInsertionSort),
        ("Bubble Sort", bubbleSort),
    ]
    fast_algorithms = [
        ("Heap Sort", heapSort),
        ("Shell Sort", shellSort),
        ("Merge Sort", mergeSort),
        ("Quick Sort", quickSort),
    ]
    built_in_algorithms = [
        ("Python sorted()", lambda a:sorted(a)),
        ("Numpy sort", lambda a:np.sort(a)),
    ]

    print(f"\n========== SORTING BENCHMARK ==========")

    for i in range(1, 11):
        arr = np.load(f"Dataset/dataset_{i}.npy")

        print(f"\n========== Dataset {i} ==========")
        print(f"Size       : {len(arr):,}")
        print(f"Data type  : {arr.dtype}")
        print("---------------------------------------")
        if np.issubdtype(arr.dtype, np.integer):
            running_algo = fast_algorithms + int_only_algorithms+ built_in_algorithms
        else:
            running_algo = fast_algorithms + built_in_algorithms
        results = compare_multiple_algorithms(running_algo, arr)

        for name, time_taken in results.items():
            if time_taken == -1:
                print(f"{name}: Error")
            else:
                print(f"{name}: {time_taken:.6f} seconds")
    print("\n========== BENCHMARK COMPLETED ==========\n")
        
    
    