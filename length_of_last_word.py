#return the length of the last word in the string
def last_word(s):
    slist = s.split()
    return len(slist[-1])
