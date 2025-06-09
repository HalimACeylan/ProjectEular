triangleNumber = []
currTriangle = 0
for i in range(1,1000000):
    currTriangle += i
    triangleNumber.append(currTriangle)

def getFactors(n):
    factors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            factors.append(i)
            factors.append(n//i)
    return factors

for i in triangleNumber:
    if len(getFactors(i)) > 500:
        print(i)
        break