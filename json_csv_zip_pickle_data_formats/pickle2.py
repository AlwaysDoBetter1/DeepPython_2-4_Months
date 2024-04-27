'''
Given a pickle file containing a single serialized function. Write a program that calls a given function with given
arguments and prints the function's return value.

Input format
The program's input in the first line is the name of the pickle file, which contains the only serialized function.
Next, an arbitrary number of lines are fed, each of which contains a positional argument for this function.

Output format
The program must call the function from the specified pickle file with all string arguments entered, and print the
function's return value. Moreover, the arguments must be passed in the order in which they were entered.
'''

import pickle
import sys

nname = input()
with open(nname, "rb") as file:
    res = pickle.load(file)
    lis = [i.strip() for i in sys.stdin]
    print(res(*lis))

# example
# First, the name of the file is given - func.pkl, which contains the serialized function:
#
# def func(*args):
#      return ' '.join(args)
# then the arguments to this function are: Hello,, how, are, you and today?.
#
# The program prints the result of the following call:
#
# func('Hello,', 'how', 'are', 'you', 'today?')

