'''
Example of using finally
'''


def beegeek():
    numbers = [1, 2, 3, 4]
    try:
        numbers.append(numbers[4])
        return numbers
    except:
        numbers.append(numbers[3])
        return numbers
    finally:
        numbers.append(numbers[2])


print(beegeek())

# Output:
# [1, 2, 3, 4, 4, 3]