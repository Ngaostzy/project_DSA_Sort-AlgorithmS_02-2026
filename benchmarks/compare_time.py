import time

def measure_execution_time(sort_func, ori_arr, repeat=5):
    total_time = 0
    try:
        for _ in range(repeat):
            test_array = ori_arr.copy()

            start_time = time.perf_counter()

            sort_func(test_array)

            end_time = time.perf_counter()

            total_time += (end_time - start_time)
        return total_time/repeat
    except RecursionError:
        return -1
    except Exception as e:
        print(f"Lỗi ở {sort_func.__name__}: {e}")
        return -1


def compare_multiple_algorithms(algo_dict, ori_array, repeat=5):
    results = {}
    for name, func in algo_dict:
        exec_time = measure_execution_time(func, ori_array, repeat)
        results[name] = exec_time
    return results