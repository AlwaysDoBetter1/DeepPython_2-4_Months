'''
Timur often receives emails with offers of cooperation. Timur values mutual respect and considers a letter
worthy of attention if it begins with one of the following expressions:

Здравствуйте
Доброе утро
Добрый день
Добрый вечер
Write a program that determines whether a letter is worthy of Timur's attention.

Input format
A single line is given as input to the program.

Output format
The program should output True if the entered string begins with one of the expressions presented in the problem
condition (in arbitrary case), or False otherwise.
'''

import re

import re

s = input()

match1 = re.match("Здравствуйте", s, flags=re.I)
match2 = re.match("Доброе утро", s, flags=re.I)
match3 = re.match("Добрый день", s, flags=re.I)
match4 = re.match("Добрый вечер", s, flags=re.I)
print(any([match1, match2, match3, match4]))

# Example
# Input
# здарова, я кирилл, хочу, чтобы ты сделал курс, суть такова...
# Output:
# False