from functools import lru_cache

@lru_cache(None)
def collatz(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 1 + collatz(n // 2)
    else:
        return 1 + collatz(3 * n + 1)

top = 0
topCount = 0
for i in range(1, 1000000):
    count = collatz(i)
    if count > topCount:
        topCount = count
        top = i

print(top, topCount)
