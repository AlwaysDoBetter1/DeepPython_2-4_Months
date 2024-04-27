'''
You have access to the desktop.zip archive, which contains various folders and files. Write a program that displays its
file structure and the size of each file.

Input format
Nothing is supplied to the program as input.

Output format
The program should display the file structure of the desktop.zip archive and the size of each file in uncompressed form.
Since the archive has its own folder hierarchy, each nesting level must be separated by two spaces.
'''


from zipfile import ZipFile

def convert_file_size(size_in_bytes):
    kb = size_in_bytes / 1024
    mb = kb / 1024
    gb = mb / 1024

    if gb >= 1:
        return f"{round(gb)} GB"
    elif mb >= 1:
        return f"{round(mb)} MB"
    elif kb >= 1:
        return f"{round(kb)} KB"
    else:
        return f"{size_in_bytes} B"
with ZipFile("desktop.zip") as file:
    for i in file.infolist():
        if i.filename.endswith("/"):
            i.filename = i.filename[:-1]
        print("  " * (len(i.filename.split("/"))-1) + i.filename.split("/")[-1], end="")
        if i.file_size != 0:
            print(f" {convert_file_size(i.file_size)}")
        else:
            print()

