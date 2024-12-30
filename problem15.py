import math


#How many such routes to (0,19) are there through a 20x20 grid?


def calculateTheMatrixPaths(m,n):
    return math.factorial(m+n-2) / (math.factorial(n-1) * math.factorial(m-1))

print(calculateTheMatrixPaths(21,21))