'''
Implement a function get_the_fastest_func() that takes two arguments in the following order:

funcs — list of arbitrary functions
arg - arbitrary object
The get_the_fastest_func() function should return the function from the list of funcs that took the
least amount of time to calculate the value when called with the arg argument.
'''

import time
def get_the_fastest_func(func, arg):
    res = 1000.0
    for i in func:
        start = time.perf_counter()
        yes = i(arg)
        endd = time.perf_counter() - start
        if res > endd:
            res = endd
            fastest_f = i
    return fastest_f

# for checking
def slow(arg):
    time.sleep(3)
def fast(arg):
    time.sleep(1)
funcs = [slow, fast]

print(get_the_fastest_func(funcs, 0))

