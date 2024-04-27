'''
Create Exception Class
'''


class NumberNotInRangeError(Exception):
    pass

try:
    number = int('3999')
    if not 4000 < number < 8000:
        raise NumberNotInRangeError('Number in invalid range')
    print(number)
except NumberNotInRangeError as e:
    print(e)

# Output:
# Number in invalid range