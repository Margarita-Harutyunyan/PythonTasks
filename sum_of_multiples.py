#find the sum of multiples of 3 or 5 below 1000
def sum_of_multiples():
    sum = 0
    for i in range(1, 1001):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum
