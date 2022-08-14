def firstlast(lst, target):
    ls = []
    if target not in lst:
        return [-1, -1]
    for i in range(len(lst)):
        if lst[i] == target:
            ls.append(i)
    return [ls[0], ls[-1]]
