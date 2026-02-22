import numpy as np

N = 1000000
dataset = []

#Array 1 int sorted raising
arr1 = np.random.randint(0, 10000000,N)
arr1.sort()
dataset.append(arr1)
#array 2 float sorted raising
arr2 = np.random.uniform(0, 10000000, N)
arr2.sort()
dataset.append(arr2)
#array 3 int sorted descending
arr3 = np.random.randint(0, 10000000, N)
arr3.sort()
arr3[::-1]
dataset.append(arr3)
#array 4 float sorted descending
arr4 = np.random.uniform(0, 10000000, N)
arr4.sort()
arr4[::-1]
dataset.append(arr4)

#Random arrays
for i in range(6):
    if (i%2==0):
        array = np.random.randint(0, 10000000, N)
    else:
        array = np.random.uniform(0, 10000000, N)
    dataset.append(array)
print("Đã tạo xong bộ dữ liệu 10 dãy")


for i, arr in enumerate(dataset):
    np.save(f"dataset_{i+1}.npy", arr)
        
