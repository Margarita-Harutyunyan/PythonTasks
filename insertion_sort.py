def insertion_sort(arr):
    for i in range(1, len(arr)):
        while arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
    return arr
