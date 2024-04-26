'''
We will assume that the PIN code is correct if it satisfies the following conditions:

consists of 5 or 6 characters
consists only of numbers (0−9)
does not contain spaces

Implement an is_valid() function that takes one argument: string - an arbitrary string

The function must return True if string is a valid PIN, or False otherwise.

Note 1: If an empty string is passed to a function, the function must return False.
'''

def is_valid(pin):
    return pin.isdigit() and len(pin) in (4, 5, 6)