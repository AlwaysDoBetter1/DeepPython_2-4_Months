'''
Tail recursion example
'''


def bee(n):
    if n >= 7:
        print('bee')
    else:
        print(n)
        bee(n + 1)


bee(4)

# Output:
# 4
# 5
# 6
# bee