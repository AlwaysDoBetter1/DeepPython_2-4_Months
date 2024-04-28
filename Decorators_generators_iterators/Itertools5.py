'''
You have access to the items list, which contains a set of items. Each item is presented as a named tuple and has
three parameters - name, mass (in grams) and value (in rubles). There is also a backpack with a certain carrying
capacity.

Write a program that determines which items from a given set should be taken in order to construct a backpack
with the maximum value of the items inside, while respecting the weight limit of the backpack.

Input format
The input to the program in the first line is a number - the carrying capacity of the backpack (in grams).

Output format
The program must determine which items from the presented set should be taken in order to assemble a backpack
with the maximum value of the items inside, while respecting the weight limit of the backpack, and display
the names of the received items in lexicographic order, each on a separate line. If the backpack does not allow
you to take any item, the program should display the text:

"The backpack cannot be assembled"
'''

from collections import namedtuple
from itertools import combinations

Item = namedtuple('Item', ['name', 'mass', 'price'])

items = [Item('Wedding ring', 7, 49_000),
         Item('Mobile phone', 200, 110_000),
         Item('Laptop', 2000, 150_000),
         Item('Parker pen', 20, 37_000),
         Item('Oscar statuette', 4000, 28_000),
         Item('Headphones', 150, 11_000),
         Item('Guitar', 1500, 32_000),
         Item('Gold coin', 8, 140_000),
         Item('Camera', 720, 79_000),
         Item('Limited edition sneakers', 300, 80_000)]

max_mass = int(input())
result_set = set()

for i in range(len(items) + 1):
    for j in combinations(items, i):
        if sum(item.mass for item in j) <= max_mass:
            result_set.add(j)

resl = max(result_set, key=lambda x: sum(item.price for item in x))
if resl:
    print(*sorted(list(i.name for i in resl)), sep="\n")
else:
    print("Unable to assemble the backpack")

# Check
# Input
# 500

# output:
# gold coin
# Mobile phone
# Headphones
# Wedding ring
# Parker pen