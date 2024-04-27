'''
In the BEEGEEK online school, a student's name is considered correct if it begins with a capital Latin letter
followed by lowercase Latin letters. For example, the names Timur and Yo are considered correct, but the names
timyrik, Yo17, TimuRRR are not. Each student also has an identification number, represented by a natural number,
which is issued upon admission to school. For example, if there are 10 students in a school, then a new arriving
student will receive an identification number of 11.

Implement a get_id() function that takes two arguments:

names - list of names of students studying at the school
name — name of the incoming student
The function should return the identification number that the student entering the school will receive, while

if the student name is not a string (type str), the function should raise an exception:
TypeError('Name is not a string')
if the student's name name is a string (type str) but is not a valid name, the function should raise an exception:
ValueError('Name is not valid')
'''


def get_id(names, name):
    if not isinstance(name, str):
        raise TypeError('Name is not a string')
    elif not name.isalpha() or name != name.capitalize():
        raise ValueError('Name is not valid')
    return len(names) + 1

names = ['Timur', 'Anri', 'Dima']
name = 'Arthur'

print(get_id(names, name))
# Output:
# 4