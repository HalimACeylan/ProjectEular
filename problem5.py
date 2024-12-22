def is_prime(n):
    if n in (2, 3): 
        return True
    if n < 2 or n % 2 == 0: 
        return False
    if n < 9: 
        return True
    if n % 3 == 0: 
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0 or n % (f + 2) == 0:
            return False
        f += 6
    return True

def highest_power_under_limit(prime, limit):
    p = 0
    while prime**p <= limit:
        p += 1
    return prime**(p - 1)

def smallest_multiple(limit):
    primes = [i for i in range(2, limit) if is_prime(i)]
    result = 1
    for prime in primes:
        result *= highest_power_under_limit(prime, limit)
    return result

n = 20
print(smallest_multiple(n))
