'''
Implement a custom_sort() function that takes two arguments in the following order:

ordered_dict — OrderedDict dictionary
by_values - boolean value, defaults to False
The function should sort the ordered_dict dictionary:

by keys if by_values is False
by values if by_values is True
'''

from collections import OrderedDict

def custom_sort(ordered_dict, by_values=False):
    for i in sorted(list(ordered_dict.items()), key = lambda x: x[by_values]):
        ordered_dict.move_to_end(i[0])

data = OrderedDict(Dustin=29, Anabel=17, Brian=40, Carol=16)
custom_sort(data)

print(data)

# output:
# OrderedDict([('Anabel', 17), ('Brian', 40), ('Carol', 16), ('Dustin', 29)])