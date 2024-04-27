'''
The BEEGEEK team plans to release their new course on 11/08/2022 at exactly 12:00. Write a program that takes
the current date and time as input and determines how much time is left until the course is released.

Input format
The program input is the current date and time in the format DD.MM.YYYY HH:MM.

Output format
The program should output text indicating the number of days and hours remaining until the course is released,
in the following format:

There are: <number of days> days and <number of hours> hours left until the course is released
If in this case the number of hours is zero, then only days need to be displayed.

If the number of days is zero, then you only need to display the hours and minutes in the following format:

There are: <number of hours> hours and <number of minutes> minutes left until the course is released
If in this case the number of minutes is zero, then only the hours need to be displayed. Similarly, if the number
of hours is zero, then only minutes need to be displayed.

If the entered date and time is greater than or equal to 11/08/2022 12:00, the program should output the text:

The course is out now!
'''

from datetime import date, time, datetime, timedelta

def choose_plural(amount, variants):
    if amount % 10 == 1 and amount % 100 != 11:
        variant = 0
    elif amount % 10 >= 2 and amount % 10 <= 4 and \
            (amount % 100 < 10 or amount % 100 >= 20):
        variant = 1
    else:
        variant = 2
    return '{} {}'.format(amount, variants[variant])


date_now = datetime.strptime(input(), '%d.%m.%Y %H:%M')
date_x = datetime(2022, 11, 8, 12)

if date_x > date_now:
    delta = date_x - date_now
    days = delta.days
    hours = delta.seconds // 3600
    minutes = (delta.seconds - hours * 3600) // 60
    result = ''
    if days > 0:
        result = choose_plural(days, ('день', 'дня', 'дней'))
        if hours > 0:
            result += ' и ' + choose_plural(hours, (' час', 'часа', 'часов'))
    elif hours > 0:
        result = choose_plural(hours, ('час', 'часа', 'часов'))
        if minutes > 0:
            result += ' и ' + choose_plural(minutes, ('минута', 'минуты', 'минут'))
    else:
        result = choose_plural(minutes, ('минута', 'минуты', 'минут'))
    print('До выхода курса осталось: ' + result)
else:
    print('Курс уже вышел!')

# input:
# 16.11.2021 06:30
# output:
# До выхода курса осталось: 357 дней и 5 часов
# input:
# 08.11.2022 10:30
# output:
# До выхода курса осталось: 1 час и 30 минут
# input:
# 08.11.2022 11:40
# output:
# До выхода курса осталось: 20 минут

