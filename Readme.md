# DSA Sorting Algorithms Project

## Giới thiệu
Dự án triển khai và so sánh hiệu năng các thuật toán sắp xếp trong môn Cấu trúc dữ liệu & Giải thuật (DSA).

---

## Cấu trúc thư mục
DSA/
│
├── algorithms/
│ ├── Bubblesort.py
│ ├── dataset.py # file khởi tạo thư mục dataset
│ ├── InsertionSort.py
│ ├── MergeSort.py
│ ├── QuickSort.py
│ └── ...
│
├── benchmarks/
│ └── compare_time.py
│
├── Dataset/ # Chứa dữ liệu test (1 triệu phần tử mỗi file, không push lên GitHub)
│
├── main.py # File chạy chính để thực hiện benchmark
└── README.md

**Dataset/**  
Chứa 10 bộ dữ liệu (1.000.000 phần tử mỗi bộ), gồm:
  - 2 bộ dữ liệu tăng dần
  - 2 bộ dữ liệu giảm dần
  - 6 bộ dữ liệu ngẫu nhiên
  - Bao gồm cả kiểu `int` và `float` (5 5)