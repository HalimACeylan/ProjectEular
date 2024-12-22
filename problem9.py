import math

for a in range(1, 1000):
    for b in range(a + 1, 1000 - a): 
        c = 1000 - a - b  # c is determined by the sum constraint
        if a < b < c and a**2 + b**2 == c**2:  # Ensure it's a Pythagorean triplet
            print(a*b*c)
            break  # Exit the loop once a solution is found