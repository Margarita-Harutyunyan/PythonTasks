#remove duplicates from sorted aray and return the number of elements remaining
def duplicate(lst):
    count = 1
    for i in range(1, len(lst)):
        if lst[i] != lst[i - 1]:
            count += 1
    return count
