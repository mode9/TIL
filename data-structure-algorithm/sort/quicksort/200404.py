def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr)+equal_arr+quick_sort(greater_arr)


def quick_sort_in_place(arr):
    def sort(low, high):
        if high <= low:
            return

        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low

    return sort(0, len(arr) - 1)

import random, time

arr = random.sample(list(range(5000000)), 5000000)
start = time.time()
quick_sort_in_place(arr.copy())
end = time.time()
print('in place 실행시간: %s' % round(end-start, 2))
start = time.time()
quick_sort(arr)
end = time.time()
print('normal 실행시간: %s' % round(end-start, 2))
