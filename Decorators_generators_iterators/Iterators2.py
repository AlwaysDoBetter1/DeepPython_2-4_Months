'''
Implement a random_numbers() function that takes two arguments:

left — integer
right — integer
The function must return an iterator that generates an infinite sequence of random integers ranging from left to right,
inclusive.
'''

from random import randint
def random_numbers(l, r):
    c = randint(l, r)
    return iter(lambda: c, "")
