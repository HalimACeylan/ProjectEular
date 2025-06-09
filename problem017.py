totalLetterNumbers = {
    0: 0,    # No letters for 0
    1: 3,    # one
    2: 3,    # two
    3: 5,    # three
    4: 4,    # four
    5: 4,    # five
    6: 3,    # six
    7: 5,    # seven
    8: 5,    # eight
    9: 4,    # nine
    10: 3,   # ten
    11: 6,   # eleven
    12: 6,   # twelve
    13: 8,   # thirteen
    14: 8,   # fourteen
    15: 7,   # fifteen
    16: 7,   # sixteen
    17: 9,   # seventeen
    18: 8,   # eighteen
    19: 8,   # nineteen
    20: 6,   # twenty
    30: 6,   # thirty
    40: 5,   # forty
    50: 5,   # fifty
    60: 5,   # sixty
    70: 7,   # seventy
    80: 6,   # eighty
    90: 6,   # ninety
    100: 7,  # hundred
    1000: 11 # one thousand
}

totalNumber = 0

for i in range(1, 1000):
    if i < 20:
        # Numbers 1 to 19
        totalNumber += totalLetterNumbers[i]
    elif i < 100:
        # Numbers 20 to 99
        tens = i // 10 * 10
        units = i % 10
        totalNumber += totalLetterNumbers[tens] + totalLetterNumbers[units]
    else:
        # Numbers 100 to 999
        hundreds = i // 100
        totalNumber += totalLetterNumbers[hundreds] + totalLetterNumbers[100]  # e.g., "one hundred"

        # Handle the last two digits
        twoDigits = i % 100
        if twoDigits > 0:
            totalNumber += 3  # Add "and"
            if twoDigits < 20:
                totalNumber += totalLetterNumbers[twoDigits]
            else:
                tens = twoDigits // 10 * 10
                units = twoDigits % 10
                totalNumber += totalLetterNumbers[tens] + totalLetterNumbers[units]

# Add "one thousand"
totalNumber += totalLetterNumbers[1000]

print(f"Total number of letters used: {totalNumber}")
