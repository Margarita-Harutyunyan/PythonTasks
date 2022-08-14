#find the sum of even fibonacci numbers below four million
def fib_sum():
    a,b = 0,1
    sum = 0
    while True:
        a,b = b, a + b
        if b >= 4000000:
            break
        if b % 2 == 0:
            sum += b
    return sum
