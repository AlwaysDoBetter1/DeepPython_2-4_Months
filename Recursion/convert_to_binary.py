'''
Implement the to_binary() function using recursion that takes one argument:

number — non-negative integer
The function must return a string representation of the number 'number' in the binary number system.
'''


def to_binary(n):
    if n == 1:
        return "1"
    elif n == 0:
        return "0"
    else:
        return str(to_binary(n//2))+str(n%2)
