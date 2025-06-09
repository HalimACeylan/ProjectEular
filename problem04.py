
listOfPolindromes = []
for i in range(1000,100,-1):
    for j in range(1000,100,-1):
        if str(i*j) == str(i*j)[::-1]:
            listOfPolindromes.append(i*j)

print(max(listOfPolindromes))            