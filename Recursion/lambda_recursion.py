'''
Example of lambda recursion
'''


# Define a lambda function that returns a named function
factorial = (lambda f: (lambda x: 1 if x == 0 else x * f(f)(x - 1)))(lambda f: (lambda x: 1 if x == 0 else x * f(f)(x - 1)))

# Example usage
print(factorial(5))  # Output: 120
