'''
Students at the BEEGEEK online school decided to find out which of them could solve their math homework the fastest.
To do this, each student recorded the start and end time of solving their homework.

You have access to a data dictionary containing student results. The key in the dictionary is the name of the student,
and the value is a tuple, the first element of which is the start time of the solution, the second element is the
end time of the solution. Complete the code below to display the name of the student who spent the least amount of
time solving the homework problem.

Note 1. It is guaranteed that the student you are looking for is unique.
'''

from datetime import datetime

data = {'Dima': ('03.11.2021 09:31:18', '03.11.2021 11:41:28'),
        'Geor': ('01.11.2021 09:03:04', '01.11.2021 12:40:35'),
        'Anna': ('02.11.2021 04:41:54', '02.11.2021 05:39:40'),
        'Ilina': ('02.11.2021 01:36:40', '02.11.2021 04:48:27'),
        'German': ('04.11.2021 07:51:19', '04.11.2021 09:53:53'),
        'Ruslan': ('01.11.2021 11:26:06', '01.11.2021 12:56:24'),
        'Lera': ('03.11.2021 11:09:41', '03.11.2021 14:37:41'),
        'Egor': ('03.11.2021 05:29:38', '03.11.2021 06:01:59'),
        'Maxim': ('05.11.2021 13:05:03', '05.11.2021 14:27:41'),
        'Sasha': ('03.11.2021 04:14:26', '03.11.2021 05:10:58'),
        'Marina': ('05.11.2021 15:21:06', '05.11.2021 18:33:46')}
for i in data:
    data[i] = datetime.strptime(data[i][0], "%d.%m.%Y %H:%M:%S") - datetime.strptime(data[i][1], "%d.%m.%Y %H:%M:%S")
print(max(data, key=data.get))

# Output:
# Egor