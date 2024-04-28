'''
Implement an ignore_exception decorator that takes an arbitrary number of positional arguments—exception
types—and outputs the text:

Exception <exception type> handled
if during execution of the decorated function an exception belonging to one of the passed types was raised.

If the exception thrown is not one of the passed types, it must be thrown again.

The decorator must also store the name and docstring of the function being decorated.

Note 1. Do not forget that the decorator should not consume the return value of the function being decorated,
and should also be able to decorate functions with an arbitrary number of positional and named arguments.
'''

import functools

def ignore_exception(*args):
    def typ(func):
        @functools.wraps(func)
        def wrapper(*args1, **kwargs):
            try:
                return func(*args1, **kwargs)
            except Exception as e:
                if isinstance(e, args):
                    print(f"Exception {e.__class__.__name__} handled")
                else:
                    raise e
        return wrapper
    return typ

# check
@ignore_exception(ZeroDivisionError, TypeError, ValueError)
def f(x):
    return 1 / x

f(0)

# Output:
# Exception ZeroDivisionError handled