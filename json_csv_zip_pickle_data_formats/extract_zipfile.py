'''
Implement a function extract_this() that takes one or more arguments in the following order:

zip_name — name of the zip archive, for example, data.zip
*args - a variable number of positional arguments, each of which is the name of a file
The function should extract *args files from the zip_name archive into the program folder. If no file
name is passed to the function to extract, then the function must extract all files from the archive.

Note 1: For example, the following function call

extract_this('workbook.zip', 'earth.jpg', 'exam.txt')
must extract the files earth.jpg and exam.txt from the workbook.zip archive into the folder with the program.

Calling a function
extract_this('workbook.zip')
must extract all files from the workbook.zip archive into the folder with the program.
'''

from zipfile import ZipFile


def extract_this(zip_name: str, *args):
    with ZipFile(zip_name) as zf:
        zf.extractall(members=args or None)


