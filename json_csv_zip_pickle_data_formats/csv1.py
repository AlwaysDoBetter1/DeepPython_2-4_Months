'''
Dima really wants to eat, but he doesn’t have much money. Help him identify the cheapest product and the store
that sells it. You have access to the file "prices.csv", which contains information about the prices of products
in various stores. The first column contains the name of the store, and the subsequent columns contain the price
of the corresponding product in this store:

Shop;Cottage cheese;Buckwheat;Rice;Borodinsky bread;Apples;Dumplings;Oatmeal cookies;Spaghetti;Baked beans;Ice
cream;Miced meat;Dumplings;Potatoes;Bar
Pyaterochka;69;133;129;83;141;90;72;123;149;89;88;106;54;84
Magnet;102;87;95;75;109;112;97;82;101;134;69;61;141;79
...
Write a program that determines and displays the cheapest product and the name of the store that sells it,
in the following format:

<product name>: <store name>
If there are several cheapest products, then you should display the product whose name is lower in the lexicographic
comparison. If one product is sold in several stores at the same minimum price, then you should display the store
whose name is lower in the lexicographic comparison.
'''

import csv

with open('prices.csv', encoding='UTF-8') as f:
    h, *rows = csv.reader(f, delimiter=';')

goods = [(r[0], h[x], r[x]) for r in rows for x in range(1, len(h))]
cheapest = min(goods, key=lambda x: (int(x[2]), x[1], x[0]))

print(f'{cheapest[1]}: {cheapest[0]}')


