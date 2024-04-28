'''
Implement interleave() using generator expressions that takes an arbitrary number of positional arguments,
each of which is a sequence.

The function must return a generator that generates each element of all passed sequences: first the first element
of the first sequence, then the first element of the second sequence, and so on; after the second element of the
first sequence, then the second element of the second sequence, and so on.

Note 1: A sequence is a collection that supports indexing and has a length. For example, objects of type list, str,
tuple are sequences.
Note 2: It is guaranteed that all sequences passed to the function are of equal length.
'''

def interleave(*args):
    return (i for obj in zip(*args) for i in obj)
# Check
print(*interleave('bee', '123'))
# output:
# b 1 e 2 e 3