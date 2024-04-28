'''
Write a program that, in a given text, finds all phone numbers that match the following formats:
7-ddd-ddd-dd-dd
8-ddd-dddd-dddd
where d is a number from 0 to 9.

Input format
The input to the program is a string of arbitrary content.

Output format
The program must find in the entered text all telephone numbers that correspond to the formats specified in the
problem statement and display them in the order in which they were found, each on a separate line.
'''

import re

def obrabotchik(s:str):
    regex = r'7\-[0-9]{3}\-[0-9]{3}\-[0-9]{2}\-[0-9]{2}|8\-[0-9]{3}\-[0-9]{4}\-[0-9]{4}'
    return re.findall(regex, s)
print(*obrabotchik(input()), sep="\n")

# Example
# Input
# Arthur: +7-919-667-21-19, Anri: 7-hey-anri-anri, Timur: 8-917-4864-1911
# Output:
# 7-919-667-21-19
# 8-917-4864-1911