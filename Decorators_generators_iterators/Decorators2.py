'''
Implement a retry decorator that takes one argument:

times — natural number
The decorator must retry calling the decorated function if an error occurs during its execution.
The decorator must call it until it runs out of times, at which point it must throw a MaxRetriesException.

The decorator must also store the name and docstring of the function being decorated.
'''

import functools

class MaxRetriesException(Exception):
    pass


def retry(times):
    def typ(func):
        @functools.wraps(func)
        def wrapper(*args1, **kwargs):
            for i in range(times):
                try:
                    return func(*args1, **kwargs)
                except:
                    pass
            raise MaxRetriesException
        return wrapper
    return typ

# Check
@retry(8)
def beegeek():
    beegeek.calls = beegeek.__dict__.get('calls', 0) + 1
    if beegeek.calls < 5:
        raise ValueError
    print('beegeek')


beegeek()

# Output:
# beegeek