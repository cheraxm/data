"""LAB 7.1 - SUMMATION(N)"""

from time import time

def summation_one(n):
    summ = 0
    for i in range(1,n):
        summ += i
    print(summ)


# def summation_two(n):
#     total = (n*(n+1))/2
#     print(total)


def analyze_algo(n):
    stime = time() # record the starting time
    summation_one(n)
    etime = time() # record the ending time
    elapsed = etime-stime # compute the elapsed time
    print("execution time: ", elapsed)
analyze_algo(1000000)
