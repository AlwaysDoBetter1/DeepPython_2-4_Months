'''
Implement a roundrobin() function that takes an arbitrary number of positional arguments, each of which is an iterable.

The function must return an iterator that generates a sequence of elements of all passed iterables: first the first
element of the first iterable, then the first element of the second iterable, and so on; after the second element
of the first iterable, then the second element of the second iterable, and so on.

Note 1: The elements of the iterable objects in the iterator returned by the function must be in their original order.

Note 2: It is guaranteed that the iterable object passed to the function is not a set.
'''

from itertools import cycle

def take(iterable, n):
    for elem, _ in zip(iterable, range(n)):
        yield elem

def roundrobin(*iterables):
    non_empty = len(iterables)
    iterables = cycle(map(iter, iterables))
    while non_empty:
        try:
            for it in iterables:
                yield next(it)
        except StopIteration:
            non_empty -= 1
            iterables = cycle(take(iterables, non_empty))

# Check
numbers = [1, 2, 3]
letters = iter('beegeek')

print(*roundrobin(numbers, letters))
# output:
# 1 b 2 e 3 e g e e k