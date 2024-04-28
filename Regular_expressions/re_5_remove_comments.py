'''
When writing programs, we often leave comments or documentation lines for functions. Let's define three types of comments:

single-line comments are lines of code starting with the hash symbol #. Single-line comments can be at any nesting level.
For example:
# this is a one-line comment

def func(a, b):
     # this is a one-line comment
     return a + b
comments immediately following a line of code. In other words, it is a line of code followed by
2
2 spaces, a hash symbol #, a space and the comment itself, for example:
numbers = [1, 2, 3] # this is a comment
multiline comments are one or more lines of code that begin and end with three quotes """. Multiline comments can be
at any nesting level. For example:
"""this is a multi-line comment"""

def func(a, b):
     """This
     multiline
     a comment"""
     return a + b
Write a program that removes all comments from Python code.
'''

import re
import sys

regh = r'\n? *#.*?$|\s*""".*?"""$'
s = sys.stdin.read()
print(re.sub(regh, "", s, flags=re.S | re.M))

# Example
# Input
# """hello everyone
# welcome to my project"""
#
# import math  # importing a useful math module
#
# # let's take a look at some functions
#
# def circle_area(radius):
#     """coming soon"""
#     return math.pi * r ** 2  # my favorite formula
#
# def triangle_area(base, height):
#     """the function takes
#     the base and height
#     of a triangle and
#     returns its area"""
#     return 0.5 * base * height
# Output:
# import math
#
#
# def circle_area(radius):
#     return math.pi * r ** 2
#
# def triangle_area(base, height):
#     return 0.5 * base * height