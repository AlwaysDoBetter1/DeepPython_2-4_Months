'''
There are letters in Russian and English that look the same. Here is a list of English letters
“AaBCcEeHKMOoPpTXxy”, and here are their Russian analogues “AaBCcEeNKMOoRRrTKHhu”. Write a program that,
for three letters from given lists of letters, determines whether they are Russian, English, or both
(a mixture of Russian and English letters).

Input format
The input to the program is given three letters from the sets of letters specified
in the condition, each on a separate line.

Output format
The program should output

ru, if all three letters are Russian
en if all three letters are English
mix, if the letters include both Russian and English
'''


en, count = 'AaBCcEeHKMOoPpTXxy', 0
for i in [input() for i in range(3)]:
    if i in en:
        count += 1
if count == 3: print('en')
if count == 0: print('ru')
if 0<count<3: print('mix')

# Input:
# T
# а
# B
# Output
# mix