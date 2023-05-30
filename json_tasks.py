#4.4.1

# import json
#
# countries = {'Monaco': 'Monaco', 'Iceland': 'Reykjavik', 'Kenya': 'Nairobi', 'Kazakhstan': 'Nur-Sultan',
#              'Mali': 'Bamako', 'Colombia': 'Bogota', 'Finland': 'Helsinki', 'Costa Rica': 'San Jose',
#              'Cuba': 'Havana', 'France': 'Paris', 'Gabon': 'Libreville', 'Liberia': 'Monrovia',
#              'Angola': 'Luanda', 'India': 'New Delhi', 'Canada': 'Ottawa', 'Australia': 'Canberra'}
#
# countries_json = json.dumps(countries, separators=(',', ' - '), indent='   ',sort_keys=True)
#
# print(countries_json)

#4.4.2
# import json
#
# words = {
#          frozenset(["tap", "telephone"]): ("tæp", "telifəun"),
#          "travel": "trævl",
#          ("hello", "world"): ("həˈləʊ", "wɜːld"),
#          "moonlight": "muːn.laɪt",
#          "sunshine": "ˈsʌn.ʃaɪn",
#          ("why", "is", "so", "difficult"): ("waɪ", "ɪz", "səʊ", "ˈdɪfɪkəlt"),
#          "adventure": "ədˈventʃər",
#          "beautiful": "ˈbjuːtɪfl",
#          frozenset(["spoon", "block"]): ("spu:n", "blɔk"),
#          "bicycle": "baisikl",
#          ("pilot", "fly"): ("pailət", "flai")
#         }
#
# data_json = json.dumps(words,skipkeys=True)
#
# print(data_json)
#4.4.3
# import json
#
# club1 = {"name": "FC Byern Munchen", "country": "Germany", "founded": 1900,
#          "trainer": "Julian Nagelsmann", "goalkeeper": "M. Neuer", "league_position": 1}
#
# club2 = {"name": "FC Barcelona", "country": "Spain", "founded": 1899,
#          "trainer": "Xavier Creus", "goalkeeper": "M. Ter Stegen", "league_position": 7}
#
# club3 = {"name": "FC Manchester United", "country": "England", "founded": 1878,
#          "trainer": "Michael Carrick", "goalkeeper": "D. De Gea", "league_position": 8}
#
# my_list = [club1,club2, club3]
# with open('data.json', 'w', encoding='UTF-8') as file:
#     json.dump(my_list, file, indent=3)

#4.4.4.
# import json
#
# specs = {
#          'Модель': 'AMD Ryzen 5 5600G',
#          'Год релиза': 2021,
#          'Сокет': 'AM4',
#          'Техпроцесс': '7 нм',
#          'Ядро': 'Cezanne',
#          'Объем кэша L2': '3 МБ',
#          'Объем кэша L3': '16 МБ',
#          'Базовая частота': '3900 МГц'
#         }
#
# specs_json = json.dumps(specs, ensure_ascii=False,indent=3)
#
# print(specs_json)


#4.4.5.
# Функция is_correct_json()
# Реализуйте функцию is_correct_json(), которая принимает один аргумент:
#
# string — произвольная строка
# Функция должна возвращать True, если строка string удовлетворяет формату JSON, или False в противном случае.
#
# Примечание 1. Вспомните про конструкцию try-except из урока.
#
# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_correct_json(), но не код, вызывающий ее.

def is_correct_json(string):
    import json
    try:
        l = json.loads(string)
        return True
    except:
        return False

#4.4.6
# Элементы JSON
# Напишите программу, которая принимает на вход описание одного объекта в формате JSON и выводит все пары ключ-значение этого объекта.
#
# Формат входных данных
# На вход программе подается корректное описание одного объекта в формате JSON.
#
# Формат выходных данных
# Программа должна вывести все пары ключ-значение введенного объекта, разделяя ключ и значение двоеточием, каждую на отдельной строке. Если значением ключа является список, то все его элементы должны быть выведены через запятую.
#
# Примечание 1. Пары ключ-значение при выводе должны располагаться в своем исходном порядке.
#
# Примечание 2. Для считывания произвольного числа строк используйте потоковый ввод sys.stdin.

# import json
#
# string = json.loads(''.join([i for i in open(0)]))   #data = json.loads(sys.stdin.read())
# for k, v in string.items():
#     if isinstance(v, list):
#         v = ', '.join(map(str, v))
#
#     print(f'{k}: {v}')

#4.4.7
# Разные типы
# Вам доступен файл data.json, содержащий список различных объектов:
#
# [
#    "nwkWXma",
#    null,
#    {
#       "ISgHT": "dIUbf"
#    },
#    "Pzt",
#    "BXcbGVTE",
#    ...
# ]
# Напишите программу, которая создает список, элементами которого являются объекты из списка, содержащегося в файле data.json, измененные по следующим правилам:
#
# если объект является строкой, в его конец добавляется восклицательный знак
# если объект является числом, он увеличивается на единицу
# если объект является логическое значением, он инвертируется
# если объект является списком, он удваивается
# если объект является JSON-объектом (словарем), в него добавляется новая пара "newkey": null
# если объект является пустым значением (null), он не добавляется
# Полученный список программа должна записать в файл updated_data.json.
#
# Примечание 1. Например, если бы файл data.json имел вид:
#
# ["Hello", 179, true, null, [1, 2, 3], {"key": "value"}]
# то программа должна была бы создать файл updated_data.json со следующим содержанием:
#
# ["Hello!", 180, false, [1, 2, 3, 1, 2, 3], {"key": "value", "newkey": null}]

# import json
#
# with open('data.json', 'r',  encoding='UTF-8') as file:
#     jdata = json.load(file)
#
# res =[]
# for i in jdata:
#
#     if isinstance(i,str):
#         temp = i + '!'
#         res.append(temp)
#     elif isinstance(i, bool):
#         temp = not i
#         res.append(temp)
#     elif isinstance(i,int) or isinstance(i,float):
#         temp =  i + 1
#         res.append(temp)
#     elif isinstance(i, list):
#         temp = i * 2
#         res.append(temp)
#     elif isinstance(i, dict):
#         temp = i
#         temp['newkey'] = None
#         res.append(temp)
#     elif i is None:
#         continue
#
# with open('updated_data.json','w',encoding='UTF-8') as file:
#     json.dump(res,file,indent=3)

###examples
# import json
#
# opers = {'str': lambda x: x + '!',
#          'int': lambda x: x + 1,
#          'float': lambda x: x + 1,
#          'bool': lambda x: not x,
#          'list': lambda x: x * 2,
#          'dict': lambda x: x | {'newkey': None}}
#
# with open('data.json', encoding='utf8') as fi, open('updated_data.json', 'w', encoding='utf8') as fo:
# 	json.dump([opers[type(i).__name__](i) for i in json.load(fi) if type(i).__name__ in opers], fo, indent=3)


# import json
#
# with open('data.json', encoding='utf-8') as file, open('updated_data.json', 'w', encoding='utf-8') as new_file:
#     data = json.load(file)
#     conv_values = {
#         str: lambda x: x + '!',
#         int: lambda x: x + 1,
#         bool: lambda x: not x,
#         list: lambda x: x * 2,
#         dict: lambda x: {**x, "newkey": None},
#     }
#     new_data = []
#     for d in data:
#         if type(d) in conv_values:
#             new_data.append(conv_values[type(d)](d))
#     json.dump(new_data, new_file, indent=2)


#4.4.8
# Объединение объектов
# Вам доступны два файла data1.json и data2.json, каждый из которых содержит по единственному JSON-объекту:
#
# {
#    "Holly-Anne": [
#       33,
#       "failed"
#    ],
#    "Caty": [
#       36,
#       "failed"
#    ],
#    ...
# }
# Напишите программу, которая объединяет два данных JSON-объекта в один JSON-объект, причем если пары из первого и второго объектов имеют совпадающие ключи, то значение следует взять из второго объекта. Полученный JSON-объект программа должна записать в файл data_merge.json.
#
# Примечание 1. Например, если бы файлы data1.json и data2.json имели вид:
#
# {
#    "Timur": 99,
#    "Anri": 97
# }
# {
#    "Dima": 99,
#    "Anri": 100
# }
# то программа должна была бы создать файл data_merge.json со следующим содержанием:
#
# {
#    "Anri": 100,
#    "Dima": 99,
#    "Timur": 99
# }
# Примечание 2. Элементы в результирующем JSON-объекте могут располагаться в произвольном порядке.
#
# Примечание 3. Указанные файлы доступны по ссылке и ссылке. Ответ на задачу доступен по ссылке.
#
# Примечание 4. При открытии файла используйте явное указание кодировки UTF-8.

# import json
#
# with open('data1.json', 'r',encoding='UTF-8') as f1:
#     data1 = json.load(f1)
#
# with open('data2.json', 'r', encoding='UTF-8') as f2:
#     data2 = json.load(f2)
#
# new_dict ={**data1, **data2}
# with open('data_merge.json','w',encoding='UTF-8') as file:
#     json.dump(new_dict, file, indent=3)

# ###examples

# import json
#
# with open('data1.json', encoding='Utf-8') as file1, \
#      open('data2.json', encoding='utf-8') as file2, \
#      open('data_merge.json', 'w') as outer:
#     data1, data2=json.load(file1), json.load(file2)
#     json.dump(data1|data2, outer)


#4.4.9.
#
# Восстановление недостающих ключей
# Вам доступен файл people.json, содержащий список JSON-объектов. Причем у различных объектов может быть различное количество ключей:
#
# [
#    {
#       "age": 33,
#       "country": "Lesotho",
#       "phone": "(927) 316-2249",
#       "family_status": "married",
#       "email": "neonatus@outlook.com"
#    },
#    {
#       "age": 25,
#       "country": "Guinea",
#       "name": "Dorey",
#       "children": "yes",
#       "email": "ismail@gmail.com",
#       "university": "Khalifa University",
#       "family_status": "married"
#    },
#    ...
# ]
# Напишите программу, которая добавляет в каждый JSON-объект из данного списка все недостающие ключи, присваивая этим ключам значение null. Ключ считается недостающим, если он присутствует в каком-либо другом объекте, но отсутствует в данном. Программа должна создать список с обновленными JSON-объектами и записать его в файл updated_people.json.
#
# Примечание 1. JSON-объекты в создаваемом программой списке должны располагаться в своем исходном порядке. Порядок ключей в JSON-объектах не важен.
#
# Примечание 2. Например, если бы файл people.json имел вид:
#
# [
#    {
#       "age": 33,
#       "country": "Lesotho"
#    },
#    {
#       "age": 25,
#       "country": "Guinea",
#       "name": "Dorey"
#    }
# ]
# то программа должна была создать файла updated_people.json со следующим содержанием:
#
# [
#    {
#       "age": 33,
#       "country": "Lesotho"
#       "name": null
#    },
#    {
#       "age": 25,
#       "country": "Guinea",
#       "name": "Dorey"
#    }
# ]

#
# import json
#
# with open('people.json','r',encoding='UTF-8') as f:
#     data = json.load(f)
# res = []
# key_list = []
# for i in data:
#     for j in i.keys():
#         if j not in key_list:
#             key_list.append(j)
# for i in data:
#     temp_dict = {k:None for k in key_list}
#     temp_dict = temp_dict | i
#     res.append(temp_dict)
# with open('updated_people.json','w',encoding='UTF-8') as file:
#     json.dump(res,file,indent=3)
#
# ### examples
# import json
#
# with open('people.json', encoding='utf8') as fi, open('updated_people.json', 'w') as fo:
#     people = json.load(fi)
#     d = {k: None for i in people for k in i.keys()}
#     json.dump([d | i for i in people], fo)


#
# ####
# import json
#
#
# with open('people.json', encoding='utf-8') as js:
#     content = json.load(js)
#
# keys = set()
# for data in content:
#     keys |= data.keys()
#
# for data in content:
#     data |= dict.fromkeys(keys - data.keys())
#
# with open('updated_people.json', 'w') as js:
#     json.dump(content, js, indent=3)

# 4.4.10

# Я исповедую Python, а ты?
# Вам доступен файл countries.json, содержащий список JSON-объектов c информацией о странах и исповедуемых в них религиях:
# 
# [
#    {
#       "country": "Afghanistan",
#       "religion": "Islam"
#    },
#    {
#       "country": "Albania",
#       "religion": "Islam"
#    },
#    ...
# ]
# Каждый объект из этого списка содержит два атрибута:
# 
# country — страна
# religion — исповедуемая религия
# Напишите программу, которая создает единственный JSON-объект, имеющий в качестве ключа название религии, а в качестве значения — список стран, в которых исповедуется данная религия. Полученный JSON-объект программа должна записать в файл religion.json.
# 
# Примечание 1. Страны в списках должны располагаться в своем исходном порядке.
# 
# Примечание 2. Начальная часть файла religion.json выглядит так:
# 
# {
#    "Islam":[
#       "Afghanistan",
#       "Albania",
#       "Algeria",
#       ...
#    ],
#    ...
# }
# Примечание 3. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.
# 
# Примечание 4. При открытии файла используйте явное указание кодировки UTF-8.

#
# import json
#
# with open('countries.json','r',encoding='UTF-8') as f:
#     data = json.load(f)
# religions = {}
# for i in data:
#     if i['religion'] not in religions.keys():
#         religions[i['religion']] = []
# for i in data:
#     religions[i['religion']] += [i['country']]
#
# with open('religion.json', 'w') as out:
#     json.dump(religions, out, indent=3)
# ###examples
# import json
#
# with open("countries.json") as file_in, open("religion.json", "w") as file_out:
#
#     d = {}
#     datas = json.load(file_in)
#     for data in datas:
#         d[data['religion']] = d.get(data['religion'], []) + [data['country']]
#
#     json.dump(d, file_out)

#4.4.11
# Спортивные площадки
# Вам доступен файл playgrounds.csv с информацией о спортивных площадках Москвы. В первом столбце записан тип площадки,  во втором — административный округ, в третьем — название района, в четвертом — адрес:
#
# ObjectName;AdmArea;District;Address
# Парк, озелененная городская территория «Лианозовский парк культуры и отдыха»;Северо-Восточный административный округ;район Лианозово;Угличская улица, дом 13
# ...
# Напишите программу, создающую JSON-объект, ключом в котором является административный округ, а значением — JSON-объект, в котором, в свою очередь, ключом является название района, относящийся к этому административному округу, а значением — список адресов всех площадок в этом районе. Полученный JSON-объект программа должна записать в файл addresses.json.
#
# Примечание 1. Адреса в списках должны располагаться в своем исходном порядке.
#
# Примечание 2. Разделителем в файле playgrounds.csv является точка с запятой, при этом кавычки не используются.
#
# Примечание 3. Начальная часть файла addresses.json выглядит так:
#
# {
#    "Северо-Восточный административный округ": {
#       "район Лианозово": [
#          "Угличская улица, дом 13",
#          "Алтуфьевское шоссе, дом 147А"
#       ],
#       "район Отрадное": [
#          "Алтуфьевское шоссе, дом 20А",
#          "Юрловский проезд, дом 8, строение 1",
#          "Юрловский проезд, дом 8, строение 1"
#       ],
#       ...
#    },
#    ...
# }
# Примечание 4. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.
#
# Примечание 5. При открытии файла используйте явное указание кодировки UTF-8.
# import csv,json
# with open('playgrounds.csv', 'r', encoding='UTF-8') as inp:
#
#     reader = list(csv.DictReader(inp, delimiter =';'))
#
# admareas = [str(i['AdmArea']) for i in reader]
#
# res = {i: {reader[j]['District']:[reader[k]['Address'] for k in range(len(reader)) if reader[k]['District'] == reader[j]['District'] ] for j in range(len(reader)) if reader[j]['AdmArea'] == i } for i in [str(i['AdmArea']) for i in reader]}
# with open('addresses.json','w', encoding='UTF-8') as out:
#     json.dump(res, out, indent=3, ensure_ascii=False)




#4.4.12
# Студенты курса
# Вам доступен файл students.json, содержащий список JSON-объектов, которые представляют данные о студентах некоторого курса:
#
# [
#    {
#       "name": "Holly-Anne",
#       "city": "Abilene",
#       "age": 29,
#       "progress": 85,
#       "phone": "(802) 983-9126"
#    },
#    ...
# ]
# Под «студентом» мы будем подразумевать один JSON-объект из этого списка. У студента имеются следующие атрибуты:
#
# name — имя
# city — город проживания
# age — возраст
# progress — прогресс по курсу в процентах
# phone— контактный номер
# Напишите программу, которая определяет студентов, удовлетворяющих следующим условиям:
#
# возраст
# 18
# 18 лет или более
# прогресс по курсу
# 75
# %
# 75% или более
# Программа должна создать файл data.csv с двумя столбцами — name (имя) и phone (номер), и записать в него данные выбранных студентов, расположив их в лексикографическом порядке имён. В качестве разделителя в файле data.csv должна быть использована запятая.
#
# Примечание 1. Гарантируется, что все студенты имеют различные имена.
#
# Примечание 2. Начальная часть файла data.csv выглядит так:
#
# name,phone
# Cary,(580) 476-8517
# Catarina,(237) 608-2757
# Catherin,(876) 215-3666
# ...
# Примечание 3. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.
#
# Примечание 4. При открытии файла используйте явное указание кодировки UTF-8.
import json, csv
with open('students.json','r',encoding='UTF-8') as f:
    data = json.load(f)
res = []
for d in data:
    if d['age'] >= 18 and d['progress'] >= 75:
        res.append((d['name'], d['phone']))

res = sorted(res, key=lambda x: x[0])


out = 'datajsonout.csv'
with open(out, 'w',encoding='UTF-8', newline='') as outf:
    writer = csv.DictWriter(outf, fieldnames=['name','phone'], delimiter=',')
    writer.writeheader()
    for row in res:
        writer.writerow({'name': row[0], 'phone': row[1]})
