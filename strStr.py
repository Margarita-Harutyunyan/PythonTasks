#return the index of the first occurrence of needle in haystack
def strStr():
    haystack = input('Enter 1st: ')
    needle = input('Enter 2nd: ')
    for i in haystack:
        if i in needle:
            return haystack.index(i)
        if len(needle) == 0:
            return 0
    return -1
