'''
Given a sequence of integers. Write a program that determines whether a given sequence is a progression,
and if so, determines its type.

Input format
An arbitrary number of lines (at least three) are given as input to the program; each line contains a natural
number - the next member of the sequence.

Output format
The program should output the text:

'Arithmetic progression', if the entered sequence of numbers is an arithmetic progression
'Geometric progression', if the entered sequence of numbers is a geometric progression
'Not a progression' if the number sequence entered is not a progression
'''

import sys

# Reading integers from standard input
s = [int(i) for i in sys.stdin]

# Calculating common difference for arithmetic progression and common ratio for geometric progression
ar, geom = s[1] - s[0], s[1] / s[0]
arflag, geomflag = True, True

# Checking for arithmetic and geometric progression
for i in range(1, len(s)):
    if arflag == True and s[i - 1] + ar != s[i]:
        arflag = False
    if geomflag == True and s[i - 1] * geom != s[i]:
        geomflag = False

# Printing the result
if arflag:
    print("Arithmetic progression")
elif geomflag:
    print("Geometric progression")
else:
    print("Not a progression")


# input
# 2
# 4
# 8
# 16
# output:
# Geometric progression

