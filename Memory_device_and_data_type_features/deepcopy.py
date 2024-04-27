'''
Deepcopy example
'''

from copy import deepcopy

data1 = [[1, 2], [3, 4]]
data2 = deepcopy(data1)

data1[0].append(10)
data2[1].append(20)

print(data1)
print(data2)

# output:
# [[1, 2, 10], [3, 4]]
# [[1, 2], [3, 4, 20]]


