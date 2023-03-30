"""LAB 7.2 - ISINTERSECT(A,B,C)"""


from time import time
import random

def isIntersect1(A, B, C):
    isSame = None
    ans = False
    for i in A:
        for j in B:
            if i == j:
                if i in C:
                    ans = True
    return ans

def isIntersect2(A, B, C):
    ans = False
    for i in A:
        for j in B:
            for k in C:
                if i == j == k:
                    ans = True
    return ans

def randomList(n):
    A = [random.randint(1, n*100) for _ in range(n)]
    B = [random.randint(1, n*100) for _ in range(n)]
    C = [random.randint(1, n*100) for _ in range(n)]
    return A, B, C

def analyze_algorithms(n):
    testCase = randomList(n)
    stime = time()
    ans = isIntersect1(testCase[0], testCase[1], testCase[2])
    etime = time()
    print("isIntersect(%d)" %n)
    print("isIntersect1  = "+str(ans)+", Time = "+str(etime-stime)+"s")
    stime = time()
    ans = isIntersect2(testCase[0], testCase[1], testCase[2])
    etime = time()
    print("isIntersect2  = "+str(ans)+", Time = "+str(etime-stime)+"s")
    

def testProgram():
    print("case1 :")
    print("Intersect1 =", isIntersect1([50, 20, 80], [40, 30, 20], [20, 70, 90]))
    print("Intersect2 =", isIntersect2([50, 20, 80], [40, 30, 20], [20, 70, 90]))
    print()
    print("case2 :")
    print("Intersect1 =", isIntersect1([40, 60, 80, 100], [10, 30, 50, 60], [10, 20, 30, 40]) )
    print("Intersect2 =", isIntersect2([40, 60, 80, 100], [10, 30, 50, 60], [10, 20, 30, 40]) )

analyze_algorithms(100)
analyze_algorithms(1000)
analyze_algorithms(10000)
analyze_algorithms(100000)