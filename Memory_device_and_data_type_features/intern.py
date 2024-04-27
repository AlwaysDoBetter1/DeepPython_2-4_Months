'''
Intern example
'''

from sys import intern

a = intern('python++')
b = intern('python++')

print(a is b)

# output:
# True


