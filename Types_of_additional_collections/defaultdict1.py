'''
You have access to a list of data tuples with data on the income of some educational resource.
The first element of the tuple is the product name, the second is the profit in dollars.

Determine how much total revenue each product brought in and list the names of all the products, indicating
the corresponding total profit for each. Products must be arranged in lexicographical order, each on a separate line,
in the following format:

<product>: $<total profit>
'''

from collections import defaultdict

data = [('Books', 1343), ('Books', 1166), ('Merch', 616), ('Courses', 966), ('Merch', 1145), ('Courses', 1061),
        ('Books', 848), ('Courses', 964), ('Tutorials', 832), ('Merch', 642), ('Books', 815), ('Tutorials', 1041),
        ('Books', 1218), ('Tutorials', 880), ('Books', 1003), ('Merch', 951), ('Books', 920), ('Merch', 729),
        ('Tutorials', 977), ('Books', 656)]

res = defaultdict(int)
for i in data:
    res[i[0]] += i[1]
for i in sorted(res):
    print(f"{i}: ${res[i]}")

