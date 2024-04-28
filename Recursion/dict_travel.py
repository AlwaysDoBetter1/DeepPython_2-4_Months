'''
Implement a function dict_travel() that takes one argument:

nested_dicts - a dictionary containing numbers, strings or dictionaries as values, which, in turn, also contain numbers,
strings or dictionaries as values; nesting can be arbitrary
The function should print all the key-value pairs of the nested_dicts dictionary, as well as the values of all
its child dictionaries. When displaying the values of child dictionaries, it is necessary to list the names of
all keys, starting from the top level, separating them with dots.

For example, in the dictionary:

{'name': 'Arthur', 'grades': {'math': 4, 'chemistry': 3}}
the value 4 should be output in the following format:

grades.math: 4
All key-value pairs must be in lexicographic order, each on a separate line.

Note 1. It is guaranteed that the keys in the dictionary supplied to the function are strings containing only
lowercase Latin letters.

Note 2: It is guaranteed that no key in the dictionary supplied to the function is a sequence of other keys.
'''


def dict_travel(n):
    resl = []

    def klin(current, path=""):
        for key, value in current.items():
            new_path = f"{path}{key}."
            if isinstance(value, dict):
                klin(value, new_path)
            else:
                resl.append(f"{new_path[:-1]}: {value}")
                new_path = ".".join(new_path.split(".")[:-1])

    klin(n)
    for i in sorted(resl):
        print(i)

# input:
# data = {'a': 1, 'b': {'c': 30, 'a': 10, 'b': 20}}
#
# dict_travel(data)

# output:
# a: 1
# b.a: 10
# b.b: 20
# b.c: 30