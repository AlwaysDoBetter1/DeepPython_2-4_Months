'''
Not tail recursion example
'''


def bee(n):
    if n >= 7:
        print('bee')
    else:
        bee(n + 1)
        print(n)
bee(4)

# Output:
# bee
# 6
# 5
# 4