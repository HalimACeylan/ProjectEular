n = 100
sumOfSquares = 0
squareOfsum = 0

for i in range(n+1):
    sumOfSquares += i**2
    squareOfsum += i

print((squareOfsum**2)-sumOfSquares)
