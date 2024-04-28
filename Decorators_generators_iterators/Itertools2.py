'''
Implement a first_largest() function that takes two arguments in the following order:

iterable — an iterable object whose elements are integers
number - arbitrary number
The function must return the index of the first element of the iterable object that is greater than number.
If there are no such elements, the function should return the number −1.

Note 1: Consider the list of numbers 10,2,14,7,7,18,20 from the first test. The first number greater than 11 is 14,
which has an index of 2.

Note 2: It is guaranteed that the iterable object passed to the function is not a set.
'''

from itertools import compress, count

first_largest = lambda it, n: next(compress(count(), (i>n for i in it)), -1)
# Check
numbers = [10, 2, 14, 7, 7, 18, 20]

print(first_largest(numbers, 11))
# output:
# 2