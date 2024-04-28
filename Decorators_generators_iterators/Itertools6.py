'''
Write a program that generates all numbers of length m in number system n.

Input format
The input to the program in the first line is a natural number n≤16 - the base of the number system, and
then a natural number m - the length of the generated numbers.

Output format
The program must generate all numbers of length m in the n number system and display them in ascending order
separated by a space.
'''

from itertools import product

numbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')
[print(*item, sep="", end=" ") for item in product(numbers[:int(input())], repeat=int(input()))]

# Check
# Input:
# 2
# 3

# output:
# 000 001 010 011 100 101 110 111