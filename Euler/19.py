import calendar

year = 1901
month = 1
day = 1

count = 0

while True:
    if month == 13:
        month = 1
        year += 1

    if year == 2001:
        break

    if calendar.weekday(year, month, 1) == 6:
        count += 1

    month += 1

print(count)