'''
You have access to the food_services.json file, which contains a list of JSON objects that represent data about
catering establishments. By “establishment” we mean one JSON object from this list. The establishment
has the following attributes:
Name - name
IsNetObject - yes/no depending on whether the establishment is a network one
OperatingCompany - network name
TypeObject - type (cafe, canteen, restaurant, etc.)
AdmArea - administrative zone
District - district
Address - full address
SeatsCount - number of seats

Write a program that identifies all types of establishments and for each type finds the largest establishment
of this type (has the largest number of seats). The program should display all types of establishments in
lexicographic order, indicating for each the largest establishment and the number of seats in it. Data about
establishments should be located each on a separate line, in the following format:
<type of establishment>: <name of establishment>, <number of seats>
'''


import json

with open("food_services.json", "r", encoding="utf-8") as file:
    data = json.load(file)

dic = {}
for i in data:
    if i["TypeObject"] in dic:
        if i["SeatsCount"] > dic[i["TypeObject"]][0]:
            dic[i["TypeObject"]] = [i["SeatsCount"], i["Name"]]
    else:
        dic[i["TypeObject"]] = [i["SeatsCount"], i["Name"]]
for j in sorted(dic):
    print(j + ": " + dic[j][1], dic[j][0], sep=", ")

