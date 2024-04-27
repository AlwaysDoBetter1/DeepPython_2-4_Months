'''
You have access to the file 'name_log.csv', which contains logs of username changes. The first column
records the changed username, the second column the email address, and the third column the date and
time of the change. In this case, the user cannot change the email, only the name:

username,email,dtime
rare_charles6,charlesthompson@inbox.ru,15/11/2021 08:15
busy_patricia5,patriciasmith@bk.ru,07/11/2021 08:07
...
Write a program that selects only the most recent entries for each user from the name_log.csv file and writes
them to the new_name_log.csv file. In the new_name_log.csv file, the first line should be the same column
headings as in the name_log.csv file. The logs in the final file should be located in the lexicographic order
of the names of user email accounts.
'''


import csv
from datetime import datetime

with open("name_log.csv", "r", encoding="utf-8") as file, open("new_name_log.csv", "w", encoding="utf-8") as meta:
    dic = {}
    rows= csv.reader(file, delimiter=",")
    next(rows)
    for i in rows:
        d = datetime.strptime(i[-1], "%d/%m/%Y %H:%M")
        if i[1] not in dic:
            dic[i[1]] = [i[0], d]
        else:
            if dic[i[1]][1] < d:
                dic[i[1]] = [i[0], d]
    meta.write("username,email,dtime\n")
    for i in sorted(dic.keys()):
        print(dic[i][0], i, dic[i][1].strftime("%d/%m/%Y %H:%M"), sep=",", file=meta)

