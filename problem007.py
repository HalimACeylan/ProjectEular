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

listOfPrime = []
i = 0
while len(listOfPrime) < 10001:
    if is_prime(i):
        listOfPrime.append(i)
    i += 1;

print(listOfPrime[-1])