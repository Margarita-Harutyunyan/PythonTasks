#return true if the given integer is palindrome
def is_palindrome():
    n = int(input('Enter ur number: '))
    tmp = n
    reversed = 0
    while n > 0:
        digit = n % 10
        reversed = reversed * 10 + digit
        n //= 10
    if tmp == reversed:
        return True
    else:
        return False
