with open('problem22.txt', 'r') as file:
    names = file.read().replace('"', '').split(',')
    file.close()

names.sort()
alphabet_order = {chr(i + 64): i for i in range(1, 27)}
total = 0
for i in range(len(names)):
    letterScore = sum([alphabet_order.get(letter) for letter in str(names[i])])
    total += letterScore * (i + 1)

print(total)