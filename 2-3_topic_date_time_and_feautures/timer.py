'''
The clock shows time in the format HH:MM:SS. A timer has been started on this clock that will ring in n seconds.
Write a program that will determine what time the clock will be when the timer rings.

Input format
The input to the program in the first line is the current time on the clock in the format HH:MM:SS.
The next line contains a non-negative integer n — the number of seconds after which the timer should ring.

Output format
The program should output the time in the format HH:MM:SS, which will be on the clock when the timer rings.
'''

from datetime import timedelta, datetime

res = datetime.strptime(input(), "%H:%M:%S")
n = int(input())
print((res + timedelta(seconds=n)).time())

# input
# 09:00:00
# 90
# output:
# 09:01:30

