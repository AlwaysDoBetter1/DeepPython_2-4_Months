'''
Implement a get_min_max() function that takes one argument:

iterable - an iterable object whose elements are comparable to each other
The function must return a tuple in which the first element is the minimum element of the iterable object, and the
second element is the maximum element of the iterable object. If the iterable object is empty,
the function must return None.
'''

def get_min_max(iterable):
    iterr = iter(iterable)
    try:
        c = next(iterr)
        minn, maxx = c, c
        for i in iterable:
            if minn > i:
                minn = i
            if maxx < i:
                maxx = i
        return (minn, maxx)
    except:
        return None

# check
data = iter(range(100_000_000))

print(get_min_max(data))

# output:
# (0, 99999999)
