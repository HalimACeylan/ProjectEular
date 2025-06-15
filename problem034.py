answer = []
def primeFactors(n):
    factors = {}
    i = 2
    while i*i <= n:
        while n % i == 0:
            if i not in factors:
                factors[i] = 0
            factors[i] += 1
            n //= i
        i += 1
    if n > 1:
        if n not in factors:
            factors[n] = 0
        factors[n] += 1
    return factors

def factorial(n):
    result = 1
    for i in range(2, n+1):
        factors = primeFactors(i)
        for p in factors:
            result *= p ** factors[p]
    return result

def isCuriosNumber(n):
    total = 0
    for i in str(n):
        total += factorial(int(i))
    if total == n:
        return True

for i in range(10000000):
    isCurios = isCuriosNumber(i)
    if isCurios:
        answer.append(i)
print(answer)
    