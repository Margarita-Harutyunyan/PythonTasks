#return true if a given string is a palindrome, or false otherwise
def is_palindrome(s):
    alnum = ''.join(ch.lower() for ch in s if ch.isalnum())
    return alnum == alnum[::-1]
