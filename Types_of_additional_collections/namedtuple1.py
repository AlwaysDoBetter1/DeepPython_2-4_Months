'''
What data type will object obj have?
'''

from collections import namedtuple

unknowntype = namedtuple('Car', ['model', 'color', 'price'])

obj = unknowntype('Audi A5', 'white', 52900)
print(type(obj))

# output:
# Car

