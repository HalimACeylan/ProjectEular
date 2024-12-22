fib = [1,2,3]

while fib[-1] < 4000000:
    fib.append(fib[-1] + fib[-2])

rsult = sum([i for i in fib if i % 2 == 0])

print(rsult)