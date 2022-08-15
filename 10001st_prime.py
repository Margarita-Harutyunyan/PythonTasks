def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def prime(n):
    i = 2
    while n > 0:
        if is_prime(i):
            n -= 1
            if n == 0:
                return i
        i += 1
    return -1
print(prime(10001))
