'''
Implement a takes_positive decorator that checks that all arguments passed to the function being decorated
are positive integers.

If at least one argument does not satisfy this condition, the decorator must raise an exception:

TypeError if argument is not an integer
ValueError if argument is an integer but negative or zero
'''


def takes_positive(func):
    def wrapper(*args, **kwargs):
        summ = tuple(args+tuple(kwargs.values()))
        for i in summ:
            if not isinstance(i, int):
                raise TypeError
        for i in summ:
            if i <= 0:
                raise ValueError
        return func(*args, **kwargs)
    return wrapper

#check
@takes_positive
def positive_sum(*args):
    return sum(args)


try:
    print(positive_sum(-3, -2, -1, 0, 1, 2, 3))
except Exception as err:
    print(type(err))

# Output:
# <class 'ValueError'>