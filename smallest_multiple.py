def divisible(num):
    flag = False
    for i in range(11, 21):
        if num % i != 0:
            return False
    return True

n = 2520
while True:
    if divisible(n):
        break
    else:
        n += 2520
print(n)
