
amicables = []

def divisor(n):
    return [i for i in range(1, n) if n % i == 0]

def amicar(n):
    return sum(divisor(n))

def is_amicable(n,m):
    if n != m and amicar(n) == m and amicar(m) == n :
        if(n not in amicables):
            amicables.append(n)
        if(m not in amicables):
            amicables.append(m)

for i in range(1,10001):
    is_amicable(amicar(i),i)


print(sum(amicables))

