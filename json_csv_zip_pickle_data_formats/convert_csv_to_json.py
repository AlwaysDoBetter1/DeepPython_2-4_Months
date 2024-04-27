'''
You have access to the file exam_results.csv, which contains information about the passed exam in a certain
educational institution. The first column contains the student's name, the second - the last name, the
third - the exam grade, the fourth - the date and time of passing in the format YYYY-MM-DD HH:MM:SS,
the fifth - the email address:

name,surname,score,date_and_time,email
Jayson,Edwards,2,2021-11-10 10:00:00,sonnen@yahoo.com
April,Sims,3,2021-11-01 11:00:00,retoh@outlook.com
...
Each student has the right to retake the exam twice, so it can appear in the source file up to three times
with a different grade and a different date and time of delivery.

Write a program that determines for each student his maximum grade, as well as the date and time he received it.
The program should create a list of dictionaries, each containing the following key-value pairs:

name — student name
surname - student's last name
best_score — maximum score for the exam
date_and_time — date and time of obtaining the maximum score in the original format
email - email address
The program should write the resulting list to the file best_scores.json, and the dictionaries
in the list should be arranged in the lexicographic order of email names.
'''


import csv, json
from datetime import datetime

with open('exam_results.csv', encoding='utf8') as fi, open('best_scores.json', 'w') as fo:
    _, *rows = csv.reader(fi)
    best = lambda x: max(x, key=lambda y: (y[0], datetime.strptime(y[1], '%Y-%m-%d %H:%M:%S')))
    scores = {}

    [scores.setdefault(i[4], [i]).append((i[2], i[3])) for i in rows]
    [scores[i].append(best(scores[i][1:])) for i in scores]

    json.dump([{'name': i[0][0],
                'surname': i[0][1],
                'best_score': int(i[-1][0]),
                'date_and_time': i[-1][1],
                'email': i[0][4]} for s in sorted(scores) for i in [scores[s]]], fo, indent=3)

