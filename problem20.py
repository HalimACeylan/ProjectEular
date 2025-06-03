def calculate_mult_numbers(n):
    if (n != 1):
        return n * calculate_mult_numbers(n-1)
    else:
        return 1

digit_sum = sum(int(digit) for digit in str(calculate_mult_numbers(100)))
print(digit_sum)