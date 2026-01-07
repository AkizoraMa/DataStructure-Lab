import random
import time

# 冒泡排序
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 选择排序
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# 插入排序
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# 快速排序
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[random.randint(0, len(arr) - 1)]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    middle = [x for x in arr if x == pivot]
    return quicksort(left) + middle + quicksort(right)

# 计算排序时间
def sort_with_time(sort_function, arr):
    start_time = time.time()
    sorted_arr = sort_function(arr)
    return sorted_arr, time.time() - start_time

# 测试排序
if __name__ == "__main__":
    arr = [random.randint(1, 100) for _ in range(20)]
    print("原始数组:", arr)

    sorted_bubble, time_bubble = sort_with_time(bubble_sort, arr.copy())
    print("冒泡排序结果:", sorted_bubble, "排序时间:", time_bubble)

    sorted_selection, time_selection = sort_with_time(selection_sort, arr.copy())
    print("选择排序结果:", sorted_selection, "排序时间:", time_selection)

    sorted_insertion, time_insertion = sort_with_time(insertion_sort, arr.copy())
    print("插入排序结果:", sorted_insertion, "排序时间:", time_insertion)

    sorted_quick, time_quick = sort_with_time(quicksort, arr.copy())
    print("快速排序结果:", sorted_quick, "排序时间:", time_quick)
