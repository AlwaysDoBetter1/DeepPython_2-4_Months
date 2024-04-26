'''
You have access to the text file files.txt, which contains information about the files. Each line of the file
contains three values, separated by a space character - the file name, its size (integer) and units of measurement:

cant-help-myself.mp3 7 MB
keep-yourself-alive.mp3 6 MB
bones.mp3 5 MB
...
Write a program that groups these files by extension, determining the total size of the files in each group,
and displays the resulting groups of files, indicating the total size for each. Groups must be arranged in the
lexicographic order of extension names, files in groups - in the lexicographic order of their names.

Note 1: For example, if the files.txt file looked like:

input.txt 3000 B
scratch.zip 300 MB
output.txt 1 KB
temp.txt 4 KB
boy.bmp 2000 KB
mario.bmp 1 MB
data.zip 900 MB

then the program should output:
boy.bmp
mario.bmp
----------
Summary: 3 MB

input.txt
output.txt
temp.txt
----------
Summary: 8 KB

data.zip
scratch.zip
----------
Summary: 1 GB
'''


# just one string solving but it's impossible to read
[print(*a if isinstance(a, list) else [a.strip()], sep='\n') for i in [[[el[0] + '.' + key for el in val], '----------', f'Summary: {str(round(sum([a[2] for a in val]) / 1_073_741_824)) + " GB" if sum([a[2] for a in val]) >= 1_073_741_824 else str(round(sum([a[2] for a in val]) / 1_048_576)) + " MB" if sum([a[2] for a in val]) >= 1_048_576 else str(round(sum([a[2] for a in val]) / 1024)) + " KB"}', '\n'] for key, val in {i[1]: list(filter(lambda x: x[1] == i[1], [i if i[3] not in ['KB', 'MB', 'GB'] else [i[0], i[1], i[2] * {'KB': 1024, 'MB': 1_048_576, 'GB': 1_073_741_824}[i[3]]] for i in sorted([[i.strip().split()[0][:i.strip().split()[0].index('.')], i.strip().split()[0][i.strip().split()[0].index('.') + 1:], int(i.strip().split()[1]), i.strip().split()[2]] for i in open('files.txt', 'r', encoding='utf-8').readlines()], key=lambda x: (x[1], x[0]))])) for i in [i if i[3] not in ['KB', 'MB', 'GB'] else [i[0], i[1], i[2] * {'KB': 1024, 'MB': 1_048_576, 'GB': 1_073_741_824}[i[3]]] for i in sorted([[i.strip().split()[0][:i.strip().split()[0].index('.')], i.strip().split()[0][i.strip().split()[0].index('.') + 1:], int(i.strip().split()[1]), i.strip().split()[2]] for i in open('files.txt', 'r', encoding='utf-8').readlines()], key=lambda x: (x[1], x[0]))]}.items()] for a in i]