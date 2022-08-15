def is_palindrome(n):
    tmp = n
    reversed = 0
    while n > 0:
        digit = n % 10
        reversed = reversed * 10 + digit
        n //= 10
    return tmp == reversed:

ls = []
for i in range(100, 1000):
    for j in range(100, 1000):
        n = i * j
        if is_palindrome(n) and n not in ls:
            ls.append(n)
            ls.sort()
print(ls[-1])

