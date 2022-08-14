#move the given string to the right by the given amount
def strmove(string, number):
    newstring = string[-number:] + string[:-number]
    return newstring
