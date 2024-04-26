'''
Implement a function num_of_sundays() that takes one argument as input:

year — natural number, year
The function should return the number of Sundays in the year 'year'.
'''

from datetime import date, timedelta
def num_of_sundays(year):
    count = 0
    now = date(year, 1, 1)
    while now.year == year:
        if now.weekday() == 6:
            count += 1
        now += timedelta(days=1)
    return count

# example
print(num_of_sundays(2021))
# output:
# 52

