from problem5 import is_prime

def dynamicFormula(a, b, n):
    return (n**2) + (a*n) + b

def count_primes():
    largestCounter = 0
    result = 0
    for a in range(-1000, 1001):
        for b in range(-1000, 1001):
            n = 0
            while is_prime(dynamicFormula(a, b, n)):
                n += 1
            if n > largestCounter:
                largestCounter = n
                result = a * b
    return result

print(count_primes())
