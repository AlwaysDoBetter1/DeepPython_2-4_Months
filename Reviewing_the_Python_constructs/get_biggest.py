'''
Implement a get_biggest() function that takes one argument:

numbers — list of non-negative integers
The function must return the largest number that can be made from the numbers in the numbers list.
If the list numbers is empty, the function should return the number −1.

Note 1. Consider the first test with a list of numbers [1, 2, 3], from which the following numbers can be made:
123,132,213,231,312,321
The largest of those presented is 321.
'''


def get_biggest(numbers):
    if not numbers:
        return -1

    li = [str(i) for i in numbers]
    lenght = len(li)

    for i in range(lenght):
        index = i
        for j in range(i + 1, lenght):
            if li[j] + li[index] > li[index] + li[j]:
                index = j
        li[i], li[index] = li[index], li[i]

    return int(''.join(li))

# Input:
# print(get_biggest([61, 228, 9, 3, 11]))
# Output
# 961322811