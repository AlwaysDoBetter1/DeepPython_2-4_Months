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


dict_names = {}
dict_size = {}
dict_dimension = {'B': 1, 'KB': 1024, 'MB': 1048576, 'GB': 1073741824}
with open("files.txt", 'r', encoding='utf-8') as file:
    for line in file.readlines():
        # divide into the words we need
        name, size, dimension = line.split()
        name, extension = name.split('.')
        # fill the dictionary with names by extensions
        dict_names[extension] = (dict_names.get(extension, []) +
                                 [name + '.' + extension])
        # fill the dictionary with sizes by extensions
        dict_size[extension] = (dict_size.get(extension, 0) +
                                 dict_dimension[dimension] * int(size))

    for extension in sorted(dict_names):
        print(*sorted(dict_names[extension]), sep='\n')
        print('----------')
        for key in dict_dimension:
            result = dict_size[extension] / dict_dimension[key]
            if result <= 1024:
                break
        print('Summary:', round(result), key)
        print()