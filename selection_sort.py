def selection_sort(arr):
    count = 0
    while count < len(arr):
        min = count
        for i in range(count, len(arr)):
            if arr[count] > arr[i]:
                if arr[i] < arr[min]:
                    min = i
        arr[count], arr[min] = arr[min], arr[count]
        count += 1
    return arr
