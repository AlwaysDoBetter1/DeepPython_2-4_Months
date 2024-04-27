'''
ChainMap example
'''

from collections import ChainMap

animals = ChainMap({'alligator': 3, 'jaguar': 2},
                   {'eagle': 5, 'zebra': 2},
                   {'bear': 2, 'alligator': 1},
                   {'lemur': 7, 'elephant': 3})

print(len(animals))