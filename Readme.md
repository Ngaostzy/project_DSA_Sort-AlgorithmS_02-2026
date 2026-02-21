# DSA Sorting Algorithms Project

## Giới thiệu
Dự án triển khai và so sánh hiệu năng các thuật toán sắp xếp trong môn Cấu trúc dữ liệu & Giải thuật (DSA).

---
## Cấu trúc thư mục

```
DSA/
│
├── algorithms/
│   ├── BubbleSort.py
│   ├── InsertionSort.py
│   ├── MergeSort.py
│   ├── QuickSort.py
│   └── dataset.py # File tạo dữ liệu
│
├── benchmarks/
│   └── compare_time.py
│
├── Dataset/ # Chứa dữ liệu test (không push lên GitHub)
│
├── main.py # File chạy chính để benchmark
└── README.md
```

**Dataset/**  
Chứa 10 bộ dữ liệu (1.000.000 phần tử mỗi bộ), gồm:
  - 2 bộ dữ liệu tăng dần
  - 2 bộ dữ liệu giảm dần
  - 6 bộ dữ liệu ngẫu nhiên
  - Bao gồm cả kiểu `int` và `float` (5 5)