from problem5 import is_prime
goal = 2000000

listOfPrime = []
for i in range(2, goal):
    if is_prime(i):
        listOfPrime.append(i)

print(sum(listOfPrime))
