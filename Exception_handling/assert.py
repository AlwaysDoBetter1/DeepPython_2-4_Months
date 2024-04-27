'''
Assert example
'''

numbers = [1, 2, 3, 4, 5]

def append_zero():
    numbers.append(0)

append_zero()

assert len(numbers) <= 5, 'Длина списка должна быть не больше пяти'
# Output:
# AssertionError