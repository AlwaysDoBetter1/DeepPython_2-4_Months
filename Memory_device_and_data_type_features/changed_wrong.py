'''
Changed datatype wrong
'''

def add_ten(data=[]):
    data.append(10)
    return data

print(add_ten())
print(add_ten())
print(add_ten())

# output:
#
# [10]
# [10, 10]
# [10, 10, 10]

