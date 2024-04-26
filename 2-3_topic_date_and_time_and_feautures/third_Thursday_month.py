'''
In many museums, there is one day of the month when visiting the museum for all persons or certain categories
of citizens occurs without charging a fee. For example, in the Hermitage it is the third Thursday of the month.

Write a program that determines the dates of free days to visit the Hermitage in a given year.

Input format
The input to the program is a natural number representing the year.

Output format
The program must determine all the dates of free days to visit the Hermitage in the entered year and display them.
Dates must be arranged in ascending order, each on a separate line, in the format DD.MM.YYYY.
'''

import datetime
import calendar

def res(year):
  m = datetime.datetime(year, 1, 1)
  for i in range(1, 366):
      if calendar.weekday(int(year), m.month, m.day) == 3 and 14 < m.day < 22:
          print(m.strftime("%d.%m.%Y"))
      m += datetime.timedelta(days=1)
res(int(input()))

# input:
# 2021
# output:
# 21.01.2021
# 18.02.2021
# 18.03.2021
# 15.04.2021
# 20.05.2021
# 17.06.2021
# 15.07.2021
# 19.08.2021
# 16.09.2021
# 21.10.2021
# 18.11.2021
# 16.12.2021

