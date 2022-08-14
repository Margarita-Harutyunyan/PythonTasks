#find the difference between square of sum of 1-100 and sum of square of 1-100
def sqr_differ():
    sumofsqr = 0
    sqrofsum = 0
    sum = 0
    for n in range(1, 101):
        sumofsqr += n ** 2
        sum += n
        sqrofsum = sum ** 2
    print(sqrofsum - sumofsqr)
