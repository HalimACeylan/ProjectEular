fib = [1,1]

for i in range(2, 10000):
    f = fib[i-1] + fib[i-2]
    if len(str(f)) == 1000:
        print(i)
        break
    fib.append(f)