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
# import json, csv
# with open('students.json','r',encoding='UTF-8') as f:
#     data = json.load(f)
# res = []
# for d in data:
#     if d['age'] >= 18 and d['progress'] >= 75:
#         res.append((d['name'], d['phone']))
#
# res = sorted(res, key=lambda x: x[0])
#
#
# out = 'datajsonout.csv'
# with open(out, 'w',encoding='UTF-8', newline='') as outf:
#     writer = csv.DictWriter(outf, fieldnames=['name','phone'], delimiter=',')
#     writer.writeheader()
#     for row in res:
#         writer.writerow({'name': row[0], 'phone': row[1]})


# 4.4.13
#
# Бассейны
# Тимур планирует пойти в бассейн. Среди всех бассейнов ему подходят те, которые открыты в понедельник в период с 10:00 до 12:00. Также ему нравится плавать по длинным дорожкам, поэтому из всех работающих в это время бассейнов нужно выбрать бассейн с наибольшей длиной дорожки, при равных значениях — c наибольшей шириной.
#
# Вам доступен файл pools.json, содержащий список JSON-объектов, которые представляют данные о крытых плавательных бассейнах:
#
# [
#    {
#       "ObjectName": "Физкультурно-оздоровительный комплекс с бассейном «ГБУ «СШОР № 82» Москомспорта»",
#       "AdmArea": "Северо-Восточный административный округ",
#       "District": "Алтуфьевский район",
#       "Address": "Инженерная улица, дом 5, корпус 1",
#       "WorkingHoursSummer": {
#          "Понедельник": "10:00-11:00",
#          "Вторник": "10:00-11:00",
#          "Среда": "10:00-11:00",
#          "Четверг": "10:00-11:00",
#          "Пятница": "10:00-11:00",
#          "Суббота": "10:00-11:00",
#          "Воскресенье": "09:00-15:00",
#       },
#       "DimensionsSummer": {
#          "Square": 350,
#          "Length": 25,
#          "Width": 14,
#          "Depth": 1.8
#       }
#    },
#    ...
# ]
# Под «бассейном» будем подразумевать один JSON-объект из этого списка. У бассейна имеются следующие атрибуты:
#
# ObjectName — название, будь то фитнес клуб или спортивный комплекс
# AdmArea — административный округ
# District — название района
# Address — адрес
# WorkingHoursSummer — график работы, время начала и закрытия указываются в формате HH:MM
# DimensionsSummer — размеры бассейна, где Square — площадь, Length — длина, Width — ширина, Depth — глубина
# Напишите программу, которая определяет бассейн, подходящий Тимуру. Программа должна вывести его размеры и адрес в следующем формате:
#
# <длина>x<ширина>
# <адрес>
# Примечание 1. Пример вывода:
#
# 25x16
# Писцовая улица, дом 12, строение 1
# Примечание 2. Бассейн должен быть открыт во время всего периода с 10:00 до 12:00. Например, если бассейн работает в 10:00, но не работает в 11:30, он не подходит.
#
# Примечание 3. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.
#
# Примечание 4. При открытии файла используйте явное указание кодировки UTF-8.

# import json, datetime
# with open('pools.json','r',encoding='UTF-8') as f:
#     data = json.load(f)
# res = []
# for i in data:
#     working_hours_monday = [datetime.datetime.strptime(j, '%H:%M').time() for j in i['WorkingHoursSummer']['Понедельник'].split('-')]
#     if working_hours_monday[0] <= datetime.time(10, 0) and working_hours_monday[1] >= datetime.time(12, 0):
#         res.append([i['Address'],(i['DimensionsSummer']['Length'],i['DimensionsSummer']['Width'])])
# res = sorted(res, key=lambda x: (x[1][0], x[1][1]), reverse=True)
#
# print(f'{res[0][1][0]}x{res[0][1][1]}\n{res[0][0]}')


# #4.4.14
# Результаты экзамена 🌶️
# Вам доступен файл exam_results.csv, который содержит информацию о прошедшем экзамене в некотором учебном заведении. В первом столбце записано имя студента, во втором — фамилия, в третьем — оценка за экзамен, в четвертом — дата и время сдачи в формате YYYY-MM-DD HH:MM:SS, в пятом — адрес электронной почты:
#
# name,surname,score,date_and_time,email
# Jayson,Edwards,2,2021-11-10 10:00:00,sonnen@yahoo.com
# April,Sims,3,2021-11-01 11:00:00,retoh@outlook.com
# ...
# Каждый студент имеет право пересдать экзамен два раза, поэтому он может встречаться в исходном файле до трёх раз с различной оценкой и различными датой и временем сдачи.
#
# Напишите программу, которая для каждого студента определяет его максимальную оценку, а также дату и время ее получения. Программа должна создать список словарей, каждый из которых содержит следующие пары ключ-значение:
#
# name — имя студента
# surname — фамилия студента
# best_score — максимальная оценка за экзамен
# date_and_time — дата и время получения максимальной оценки в исходном формате
# email — адрес электронной почты
# Полученный список программа должна записать в файл best_scores.json, причем словари в списке должны быть расположены в лексикографическом порядке названий электронных почт.
#
# Примечание 1. Если при пересдаче студент получил такую же оценку, что и в прошлый раз, то в качестве даты следует указать дату пересдачи.
#
# Примечание 2. В качестве разделителя в файле exam_results.csv используется запятая, при этом кавычки не используются.
#
# Примечание 3. Начальная часть файла best_scores.json выглядит так:
#
# [
#    {
#       "name": "Stephen",
#       "surname": "Farley",
#       "best_score": 3,
#       "date_and_time": "2021-11-12 12:00:00",
#       "email": "aardo@mac.com"
#    },
#    {
#       "name": "Kaylen",
#       "surname": "Horne",
#       "best_score": 4,
#       "date_and_time": "2021-11-09 11:00:00",
#       "email": "aaribaud@att.net"
#    },
#    ...
# ]
# Примечание 4. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.
#
# Примечание 5. При открытии файла используйте явное указание кодировки UTF-8.

# import csv,datetime, json
#
# with open('exam_results.csv', 'r', encoding='UTF-8') as inp:
#
#     reader = list(csv.DictReader(inp, delimiter =','))
#
# all_students_emails = list(dict.fromkeys([i['email'] for i in reader]))
# res = [[email, {}] for email in all_students_emails]
#
# for student in reader:
#     idx = all_students_emails.index(student['email'])
#     is_student = res[idx][1].get('best_score', None)
#     if not is_student:
#         res[idx] =[student['email'], {"name": student['name'],
#                            "surname": student['surname'],
#                            "best_score": int(student['score']),
#                            "date_and_time": student['date_and_time'],
#                            "email": student['email']
#                            }]
#     else:
#         if int(student['score']) > res[idx][1].get('best_score', None):
#             res[idx][1]['best_score'] = int(student['score'])
#             res[idx][1]['date_and_time'] = student['date_and_time']
#
#         elif int(student['score']) == res[idx][1].get('best_score', None) and datetime.datetime.strptime(student['date_and_time'],'%Y-%m-%d %H:%M:%S') > datetime.datetime.strptime(res[idx][1].get('date_and_time', None),'%Y-%m-%d %H:%M:%S'):
#             res[idx][1]['date_and_time'] = student['date_and_time']
#
# res = [i[1] for i in sorted(res, key = lambda x:x[1]['email'])]
#
# with open('best_scores.json', 'w', encoding='UTF-8') as outf:
#     json.dump(res, outf, indent=3)


### examples
# import csv
# import json
#
# result = {}
# with open('exam_results.csv', encoding='utf-8') as ex_r:
#     rows = csv.DictReader(ex_r)  # 1
#     for row in rows:
#         row['best_score'] = int(row.pop('score'))  # 2
#         r = result.get(row['email'], row)  # 3
#         best_row = max(r, row, key=lambda item: (item['best_score'], item['date_and_time']))  # 4
#         result[row['email']] = best_row  # 5
#
# with open('best_scores.json', 'w', encoding='utf-8') as bs:
#     out = sorted(result.values(), key=lambda item: item['email'])  # 6
#     json.dump(out, bs, indent=3)  # 7



#4.4.15
# Общественное питание 😥
# Вам доступен файл food_services.json, содержащий список JSON-объектов, которые представляют данные о заведениях общественного питания:
#
# [
#    {
#       "Name": "СМЕТАНА",
#       "IsNetObject": "нет",
#       "OperatingCompany": "",
#       "TypeObject": "кафе",
#       "AdmArea": "Северо-Восточный административный округ",
#       "District": "Ярославский район",
#       "Address": "город Москва, улица Егора Абакумова, дом 9",
#       "SeatsCount": 48
#    },
#    ...
# ]
# Под «заведением» будем подразумевать один JSON-объект из этого списка. У заведения имеются следующие атрибуты:
#
# Name — название
# IsNetObject — да\нет в зависимости от того, является ли заведение сетевым
# OperatingCompany — название сети
# TypeObject — вид (кафе, столовая, ресторан и т.д.)
# AdmArea — административная зона
# District — район
# Address — полный адрес
# SeatsCount — количество мест
# Напишите программу, которая:
#
# определяет район Москвы, в котором находится больше всего заведений, и выводит название этого района и количество заведений в нем
# определяет сеть с самым большим числом заведений и выводит название этой сети и количество заведений этой сети
# Полученные значения программа должна вывести в следующем формате:
#
# <район>: <количество заведений>
# <название сети>: <количество заведений>
# Примечание 1. Гарантируется, что искомая сеть единственная.
#
# Примечание 2. Пример вывода:
#
# район Метрогородок: 456
# Французская пекарня SeDelice: 144
# Примечание 3. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.
#
# Примечание 4. При открытии файла используйте явное указание кодировки UTF-8.
#
# import json
# with open('food_services.json','r',encoding='UTF-8') as f:
#     data = json.load(f)
# # Определяем район
# districts = {k:0 for k in set([i['District'] for i in data])}
# for i in data:
#     districts[i['District']] +=1
# maximum = max(districts.values())
#
# for k, v in districts.items():
#     if v == maximum:
#         print(f'{k}: {v}')
#         break
# # Определяем сеть
# nets = []
# for i in data:
#     if i['IsNetObject'] == "да":
#         nets.append(i['OperatingCompany'])
#
# biggest_net = [0,'']
# for i in set(nets):
#     count = nets.count(i)
#     if biggest_net[0] < count:
#         biggest_net = [count,i]
# print(f'{biggest_net[1]}: {biggest_net[0]}')


###examples
# import json, csv
# from datetime import datetime
#
# with open('food_services.json', 'r', encoding='utf-8') as file:
#     l = list(json.load(file))
# d1, d2 = {}, {} #d1 для районов, d2 для сети
# for i in l:
#     d1[i['District']] = d1.get(i['District'], 0)+1
#     if i['OperatingCompany']:
#         d2[i['OperatingCompany']] = d2.get(i['OperatingCompany'], 0)+1
#
# x1 = max(d1.items(), key=lambda x: x[1])
# x2 = max(d2.items(), key=lambda x: x[1])
#
# print(f'{x1[0]}: {x1[1]}')
# # print(f'{x2[0]}: {x2[1]}')
# #####
# import json
#
# with open("food_services.json", "r", encoding="utf-8") as f:
#     cafes = list(json.load(f))
#     dst = [i["District"] for i in cafes]
#     cmp = [i["OperatingCompany"] for i in cafes if i["OperatingCompany"]]
#     mfd, mfc = max(set(dst), key=dst.count), max(set(cmp), key=cmp.count)
#     print(f"{mfd}: {dst.count(mfd)}\n{mfc}: {cmp.count(mfc)}")

#
# #####
# with open('food_services.json', encoding='utf-8') as file:
#     d, d1, op, s = {}, {}, 'OperatingCompany', lambda x: max(x, key=x.get)
#     for i in __import__('json').load(file):
#         d[i['District']] = d.get(i['District'], 0) + 1
#         if i[op]:
#             d1[i[op]] = d1.get(i[op], 0) + 1
#     print(f'{s(d)}: {d[s(d)]}\n{s(d1)}: {d1[s(d1)]}')


#4.4.16
#
# Общественное питание 😰
# Вам доступен файл food_services.json, содержащий список JSON-объектов, которые представляют данные о заведениях общественного питания:
#
# [
#    {
#       "Name": "СМЕТАНА",
#       "IsNetObject": "нет",
#       "OperatingCompany": "",
#       "TypeObject": "кафе",
#       "AdmArea": "Северо-Восточный административный округ",
#       "District": "Ярославский район",
#       "Address": "город Москва, улица Егора Абакумова, дом 9",
#       "SeatsCount": 48
#    },
#    ...
# ]
# Под «заведением» будем подразумевать один JSON-объект из этого списка. У заведения имеются следующие атрибуты:
#
# Name — название
# IsNetObject — да\нет в зависимости от того, является ли заведение сетевым
# OperatingCompany — название сети
# TypeObject — вид (кафе, столовая, ресторан и т.д.)
# AdmArea — административная зона
# District — район
# Address — полный адрес
# SeatsCount — количество посадочных мест
# Напишите программу, которая определяет все виды заведений и для каждого вида находит самое большое заведение этого вида (имеет наибольшее количество посадочных мест). Программа должна вывести все виды заведений в лексикографическом порядке, указав для каждого самое большое заведение и количество посадочных мест в нем. Данные о заведениях должны быть расположены каждые на отдельной строке, в следующем формате:
#
# <вид заведения>: <название заведения>, <количество посадочных мест>
# Примечание 1. Начальная часть ответа выглядит так:
#
# бар: Барное объединение ПРОФСОЮЗ, 800
# буфет: СТОЛОВАЯ - КАНТИНАСИТИ, 320
# закусочная: Бургерная FARШ, 74
# ...
# Примечание 2. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.
#
# Примечание 3. При открытии файла используйте явное указание кодировки UTF-8.


import json, time
start=time.perf_counter()
with open('food_services.json','r',encoding='UTF-8') as f:
    data = json.load(f)

food_places = {}
for i in data:
    food_places.setdefault(i["TypeObject"], {}).setdefault(i['Address'], (i["SeatsCount"], i['Name']))

food_places = dict(sorted(food_places.items(), key=lambda item: item[0]))

for k, v in food_places.items():
    maximum = sorted(v.values(), key = lambda x: x[0], reverse=True)[0]
    print(f'{k}: {maximum[1]}, {maximum[0]}')
print(time.perf_counter()-start)
##examples
# import json,time
# start = time.perf_counter()
#
# with open('food_services.json', 'r', encoding='utf-8') as f1:
#     data = json.load(f1)
#     d = {i['TypeObject']: f"{i['Name']}, {i['SeatsCount']}" for i
#          in sorted(data, key=lambda x:(x['TypeObject'], x['SeatsCount']))}
#     for item in d.items():
#         print(f'{item[0]}: {item[1]}')
# print(time.perf_counter()-start)
# ###
# import json, time
#
# start = time.perf_counter()
#
# with open('food_services.json', encoding='utf-8') as file:
#     data = json.load(file)
#     res = {}
#     for restaurant in data:
#         if restaurant['TypeObject'] not in res or restaurant['SeatsCount'] > res[restaurant['TypeObject']][1]:
#             res[restaurant['TypeObject']] = (restaurant['Name'], restaurant['SeatsCount'])
#
#     for key, value in sorted(res.items()):
#         print(f'{key}: {value[0]}, {value[1]}')
# print(time.perf_counter() - start)
# ###
# import json,time
# start = time.perf_counter()
#
# with open('food_services.json', encoding='utf-8') as f1:
#     js_lst, itog, f = json.load(f1), {}, lambda x: x[1]
#     for el in js_lst:
#         itog.setdefault(el['TypeObject'], []).append([el["Name"], el["SeatsCount"]])
#
#     for k, v in sorted(itog.items()):
#         print(f'{k}: {max(v, key=f)[0]}, {max(v, key=f)[1]}')
#
# print(time.perf_counter() - start)