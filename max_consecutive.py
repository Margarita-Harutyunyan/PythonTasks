def max_consecutive(lst):
    count = 0
    max = 0
    for i in range(len(lst)):
        if lst[i] == 1:
            count += 1
            if count > max:
                max = count
        else:
                count = 0
    return max
