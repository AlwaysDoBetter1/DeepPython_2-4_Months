'''
The program receives an indefinite number of lines as input, each of which contains an arbitrary value.
Write a program using a try-except construct that prints the sum of all numbers entered and then the number
of non-numeric values entered.

Input format
The input to the program is an indefinite number of lines (at least one), each of which contains an arbitrary value.

Output format
The program should print the sum of all entered numbers (type int and float), and then on the next line - the number
of entered non-numeric values.
'''

import sys
s, counter = 0, 0
for line in sys.stdin:
    try:
        s += int(line)
    except ValueError:
        try:
            s += float(line)
        except ValueError:
            counter += 1
print(s)
print(counter)

# Input:
# 100
# i'm number!
# 10
# [1, 99]
# 1.1
# {'math', 'physics'}
# Output:
# 111.1
# 3