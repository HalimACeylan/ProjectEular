def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_days_in_month(year):
    return [
        31,
        29 if is_leap_year(year) else 28,
        31,
        30,
        31,
        30,
        31,
        31,
        30,
        31,
        30,
        31
    ]

# Step 1: Calculate the day of the week for Jan 1, 1901
# Jan 1, 1900 = Monday = 0
day_of_week = 0  # Monday
for month_days in get_days_in_month(1900):
    day_of_week = (day_of_week + month_days) % 7

# Step 2: Count Sundays on the 1st of each month from 1901 to 2000
sundays_on_first = 0

for year in range(1901, 2001):
    for month_days in get_days_in_month(year):
        if day_of_week == 6:  # Sunday
            sundays_on_first += 1
        day_of_week = (day_of_week + month_days) % 7

print("Total Sundays on the first of the month:", sundays_on_first)