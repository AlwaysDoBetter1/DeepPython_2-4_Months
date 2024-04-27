'''
You have access to a data dictionary with an even number of elements. Complete the code below to output the
given dictionary, arranging its elements according to the following rule: first, last, second, penultimate,
third, and so on.

Note. For example, if the data dictionary looked like:

data = OrderedDict(key1='value1', key2='value2', key3='value3', key4='value4')
then the program should output:

OrderedDict([('key1', 'value1'), ('key4', 'value4'), ('key2', 'value2'), ('key3', 'value3')])
'''

from collections import OrderedDict

data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе',
                    'AdmArea': 'Центральный административный округ', 'District': 'район Правобережна',
                    'Address': 'город Киев, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})

a=[i%2 for i in range(len(data))]
res=OrderedDict()
for rule in a:
    name, grade = data.popitem(last=rule)
    res[name] = grade
print(res)
