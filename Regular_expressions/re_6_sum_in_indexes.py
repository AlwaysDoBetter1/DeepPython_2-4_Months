'''
Write a program that adds all the natural numbers in a string that are in a specified range of indices.

Input format
The input to the program is first given two integers a and b, greater than or equal to 0, separated by a space,
and then a string.

Output format
The program must print the sum of all natural numbers in the input string that are in the index range from a (inclusive)
to b (not inclusive). If there is no number in the specified range, the program should output 0.
'''

import re

a, b = (int(i) for i in input().split())
stroka = input()

gex = re.compile(r'\d+')
res = gex.findall(stroka, pos=a, endpos=b)
print(sum(int(i) for i in res))

# Example
# Input
# 0 5
# 11:20 a.m. - 12:00 p.m
# Output:
# 31