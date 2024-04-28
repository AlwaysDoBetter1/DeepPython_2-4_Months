'''
We will assume that a sequence of non-negative integers can be transformed into a segment if the difference between
adjacent elements of this sequence is equal to one. For example, the numbers 3,4,5,6,7,8 can be converted into the
segment [3;8]. The numbers 1,3,5,11,15,22 cannot be converted into a segment. A single number is transformed into a
segment in which itself is both the right and left boundary. For example, the number 1 can be converted
into the segment [1;1].

Implement a ranges() function that takes one argument:

numbers — a list of different natural numbers, arranged in ascending order
The function must convert numbers from the numbers list into segments, representing them as tuples, where the first
element of the tuple is the left border of the segment, the second element is the right border of the segment. The
function must return the resulting segment tuples as a list.
'''

from itertools import groupby

def ranges(numbers):
    lis = []
    res = [tuple(i[1]) for i in groupby(numbers, key=lambda x: numbers.index(x)-x)]
    for i in res:
        lis.append((i[0], i[-1]))
    return lis
# Check
numbers = [1, 2, 3, 4, 7, 8, 10]

print(ranges(numbers))
# output:
# [(1, 4), (7, 8), (10, 10)]