#find all the factors of a number
def find_factors(num):
    ls = []
    for n in range(1, num // 2 + 1):
        if num % n == 0:
            ls.append(n)
    return ls
#check if a number is prime
def is_prime(n):
    if n == 2 or n == 3:
        return True
    flag = False
    i = 2
    for i in range(2, n // 2):
        if n % i == 0:
            flag = True
            break
    if flag:
        return False
    else:
        return True

#find the largest prime factor
def largest_prime(number):
    primefactors = []
    factors = find_factors(number)
    for num in factors:
        if is_prime(num):
            primefactors.append(num)
    return primefactors[-1]

print(largest_prime(600851475143))


