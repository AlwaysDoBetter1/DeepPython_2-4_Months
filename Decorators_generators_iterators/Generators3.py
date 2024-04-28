'''
Implement a generator function that takes one argument:

iterable — iterable object
The function must return a generator that generates a sequence of tuples, each of which contains the next element
of the iterable object, as well as the previous and subsequent elements:

(<previous element>, <next element>, <next element>)
For the first element, the previous value is considered to be None, for the last element, the next value is also
considered to be None.

Note 1: The elements of the iterable object in the generator returned by the function must be in their original order.

Note 2: It is guaranteed that the iterable object passed to the function is not a set.
'''

def around(iterable):
    if iterable:
        start = None
        ist = iter(iterable)
        fu = next(ist, None)
        for i in ist:
            yield (start, fu, i)
            start = fu
            fu = i
        yield (start, fu, None)
    else:
        return iterable
# Check
numbers = [1, 2, 3, 4, 5]

print(*around(numbers))
# output:
# (None, 1, 2) (1, 2, 3) (2, 3, 4) (3, 4, 5) (4, 5, None)