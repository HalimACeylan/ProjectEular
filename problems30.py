numbers = []

def get_digits(num):
    digits = []
    while num > 0:
        digits.append(num % 10)  
        num //= 10               
    digits.reverse()      
    return digits

def is_powerful_number(n):
    digits = get_digits(n)
    sumOfDigits = 0
    for digit in digits:
        sumOfDigits += digit ** 5
    return sumOfDigits == n

for i in range(9999999):
    if is_powerful_number(i):
        numbers.append(i)

print(sum(numbers)-1)
