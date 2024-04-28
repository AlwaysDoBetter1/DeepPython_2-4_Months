'''
Implement a grouper() function that takes two arguments in the following order:

iterable — iterable object
n - natural number
The function must return an iterator that generates a sequence whose elements are the adjacent elements
of the iterable object, combined into tuples of n elements. If the element does not have enough neighbors,
then the value becomes None.

Note 1: The elements of the iterable object in the iterator returned by the function must be in their original order.

Note 2: It is guaranteed that the iterable object passed to the function is not a set.
'''

from typing import Generator, Iterable
from itertools import zip_longest, tee, islice

def grouper(iterable: Iterable, times: int) -> Generator:
    args = tee(iterable, times)
    usingg = (islice(args[i], i, None, times) for i in range(len(args)))
    return zip_longest(*usingg)
# Check
numbers = [1, 2, 3, 4, 5, 6]

print(*grouper(numbers, 2))
# output:
# (1, 2) (3, 4) (5, 6)