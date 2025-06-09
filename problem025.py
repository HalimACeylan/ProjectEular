#gpt did this : 
def get_cycle_length(d):
    remainders = {}
    value = 1
    position = 0

    while value != 0:
        if value in remainders:
            return position - remainders[value]
        remainders[value] = position
        value = (value * 10) % d
        position += 1

    return 0

max_length = 0
result = 0

for d in range(1, 1000):
    cycle_length = get_cycle_length(d)
    if cycle_length > max_length:
        max_length = cycle_length
        result = d

print(result)