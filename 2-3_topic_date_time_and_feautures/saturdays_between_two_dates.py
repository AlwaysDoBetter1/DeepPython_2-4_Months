'''
Implement a function saturdays_between_two_dates() that takes two arguments in the following order:

start — start date, date type
end — end date, date type
The function must return the number of Saturdays between the start and end dates, inclusive.
'''

from datetime import date


def saturdays_between_two_dates(start, endd):
    if start > endd:
        start, endd = endd, start

    return sum(date.fromordinal(i).weekday() == 5 for i in range(start.toordinal(), endd.toordinal() + 1))

# Input:
# date1 = date(2021, 11, 1)
# date2 = date(2021, 11, 22)
#
# print(saturdays_between_two_dates(date1, date2))
# Output:
# 3