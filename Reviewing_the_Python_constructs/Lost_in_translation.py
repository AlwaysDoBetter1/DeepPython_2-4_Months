'''
It is often impossible to translate TV series without losing the original meaning, especially due to wordplay.
A crazy director wants to make a series in which he would experimentally use as many languages as possible to take
advantage of the beauty of each of them. However, if you use too many languages, the series will become
incomprehensible to absolutely everyone, so the director gets random people on the street and asks them what
languages they know, so he will use the languages that all of them know.

Write a program that determines which languages will be used in the series.

Input format
The input to the program in the first line is the number n - the number of people the director is pestering.
Each of the next n lines contains a list of languages that the person knows, separated by commas and spaces.

Output format
The program should output a list of languages for the series in lexicographical order. If such a list cannot be
compiled, you need to display the text:

"The series will not be filmed"
'''


dict, lis, n = {}, [], int(input())

for i in range(n):
    for j in input().replace(",", "").split():
       dict[j] = dict.get(j, 0) + 1

for i in sorted(dict):
    if dict[i] == n:
        lis.append(i)
if lis:
    print(*lis, sep=", ")
else:
    print("The series will not be filmed")

# Input:
# 6
# испанский, португальский, эсперанто, французский
# французский, испанский, эсперанто
# португальский, эсперанто, французский, испанский
# французский, английский, болгарский, испанский, эсперанто
# эсперанто, английский, русский, испанский, французский
# python, испанский, эсперанто, латышский, польский, французский
# Output:
# испанский, французский, эсперанто