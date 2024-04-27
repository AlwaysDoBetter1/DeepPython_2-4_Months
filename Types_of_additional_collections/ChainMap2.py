'''
Implement a get_value() function that takes three arguments in the following order:

chainmap - an object of type ChainMap, the elements of which are dictionaries
key - arbitrary object
from_left — boolean value, defaults to True
The function must return the value of the key from the chainmap, and:

if from_left is True, the key lookup in the chainmap must proceed from the first dictionary to the last
if from_left is False, the key lookup in the chainmap must proceed from the last dictionary to the first
If key is not present in the chainmap, the function should return None.
'''

from collections import ChainMap

def get_value(chainmap, key, from_left=True):
    if from_left: step = 1
    else: step = -1
    for i in chainmap.maps[::step]:
        if key in i:
            return i[key]

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'name'))

# Output:
# Arthur