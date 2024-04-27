'''
Copy example
'''

from copy import copy

data1 = [[1, 2], [3, 4]]
data2 = copy(data1)

data1[0].append(10)
data2[1].append(20)

print(data1)
print(data2)

# output:
# [[1, 2, 10], [3, 4, 20]]
# [[1, 2, 10], [3, 4, 20]]


