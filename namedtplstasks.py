###6.4.10
# Вам доступен именованный кортеж Animal, который содержит данные о животном. Первым элементом именованного кортежа является имя животного, вторым — семейство, третьим — пол, четвертым — цвет. Также доступен файл data.pkl, содержащий сериализованный список таких кортежей.
#
# Дополните приведенный ниже код, чтобы для каждого кортежа из этого списка он вывел названия его полей и значения этих полей в следующем формате:
#
# name: <значение>
# family: <значение>
# sex: <значение>
# color: <значение>
# Между полями и значениями двух разных кортежей должна располагаться пустая строка.
#
# Примечание 1. Сначала должно следовать содержание первого кортежа из списка, затем второго, и так далее.
#
# Примечание 2. Например, если бы файл data.pkl содержал следующий сериализованный список:
#
# [Animal(name='Alex', family='dogs', sex='m', color='brown'), Animal(name='Nancy', family='dogs', sex='w', color='black')]
# то программа должна была бы вывести:
#
# name: Alex
# family: dogs
# sex: m
# color: brown
#
# name: Nancy
# family: dogs
# sex: w
# color: black

# import pickle
# from collections import namedtuple
#
# Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])
# with open('data.pkl','rb') as pkl:
#     data = pickle.load(pkl)
#
#     for i in data:
#         string = ''
#         for field,value in zip(Animal._fields, i):
#             string += f'{field}: {value}\n'
#         print(string)

# v2:
#         print(f'''name: {i.name}
# family: {i.family}
# sex: {i.sex}
# color: {i.color}''')


### 4.6.11
# Вам доступен именованный кортеж User, который содержит данные о пользователе некоторого ресурса. Первым элементом именованного кортежа является имя пользователя, вторым — фамилия, третьим — адрес электронной почты, четвертым — статус оформленной подписки. Также доступен список users, содержащий эти кортежи.
#
# Дополните приведенный ниже код, чтобы он вывел данные о каждом пользователе из этого списка, предварительно отсортировав их по статусу подписки от дорогой к дешевой, а при совпадении статусов — в лексикографическом порядке адресов электронных почт. Данные о каждом пользователе должны быть указаны в следующем формате:
#
# <имя> <фамилия>
#   Email: <адрес электронной почты>
#   Plan: <статус подписки>
# Между данными двух разных пользователей должна располагаться пустая строка.
#
# Примечание 1. Самой дорогой подпиской считается Gold, затем Silver, Bronze и Basic.
#
# Примечание 2. Начальная часть ответа выглядит так (в качестве отступов используйте два пробела):
#
# Kathleen Lyons
#   Email: balchen@att.net
#   Plan: Gold
#
# William Townsend
#   Email: kosact@verizon.net
#   Plan: Gold
#
# ...
#
#
# from collections import namedtuple
#
# User = namedtuple('User', ['name', 'surname', 'email', 'plan'])
#
# users = [User('Mary', 'Griffin', 'sonnen@yahoo.com', 'Basic'),
#          User('Brenda', 'Young', 'retoh@outlook.com', 'Silver'),
#          User('Kathleen', 'Lyons', 'balchen@att.net', 'Gold'),
#          User('Pamela', 'Hicks', 'corrada@sbcglobal.net', 'Silver'),
#          User('William', 'Townsend', 'kosact@verizon.net', 'Gold'),
#          User('Clayton', 'Morris', 'berserk@yahoo.com', 'Silver'),
#          User('Dorothy', 'Dennis', 'sequin@live.com', 'Gold'),
#          User('Tyler', 'Walker', 'noahb@comcast.net', 'Basic'),
#          User('Joseph', 'Moore', 'ylchang@sbcglobal.net', 'Silver'),
#          User('Kenneth', 'Richardson', 'tbusch@me.com', 'Bronze'),
#          User('Stephanie', 'Bush', 'neuffer@live.com', 'Gold'),
#          User('Gregory', 'Hughes', 'juliano@att.net', 'Basic'),
#          User('Tracy', 'Wallace', 'sblack@me.com', 'Silver'),
#          User('Russell', 'Smith', 'isaacson@comcast.net', 'Bronze'),
#          User('Megan', 'Patterson', 'hoangle@outlook.com', 'Basic')]
#
#
# new_lst = sorted(users,key=lambda x: (('Gold', 'Silver', 'Bronze', 'Basic').index(x.plan), x.email))
# for user in new_lst:
#     name, surname, email,subscription = user
#     print(name,surname)
#     print(f'  Email: {email}')
#     print(f'  Plan: {subscription}\n')

#4.6.12
# Вы кто такие? Я вас не звал
# У Тимура имеется немало друзей из других городов или стран, которые часто приезжают к нему в гости с целью увидеться и развлечься. Чтобы не забыть ни об одной встрече, Тимур записывает имена и фамилии друзей в csv файл, дополнительно указывая для каждого дату и время встречи. Вам доступен этот файл, имеющий название meetings.csv, в котором в первом столбце записана фамилия, во втором — имя, в третьем — дата в формате DD.MM.YYYY , в четвертом — время в формате HH:MM:
#
# surname,name,meeting_date,meeting_time
# Харисов,Артур,15.07.2022,17:00
# Геор,Гагиев,14.12.2022,18:00
# ...
# Напишите программу, которая выводит фамилии и имена друзей Тимура, предварительно отсортировав их по дате и времени встречи от самой ранней до самой поздней. Фамилии и имена должны быть расположены каждые на отдельной строке.
#
# Примечание 1. Начальная часть ответа выглядит так:
#
# Гудцев Таймураз
# Харисов Артур
# Базиев Герман
# ...
# Примечание 2. Гарантируется, что никакие две встречи не имеют одновременно одинаковые даты и время.
#
# Примечание 3. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.
#
# Примечание 4. Разделителем в файле meetings.csv является запятая, при этом кавычки не используются.
#
# Примечание 5. При открытии файла используйте явное указание кодировки UTF-8.

# import csv
# from collections import namedtuple
# from datetime import datetime
# date_pattern, time_pattern = '%d.%m.%Y', '%H:%M'
#
# with open('meetings.csv','r',encoding='UTF-8') as f:
#     header,*data = csv.reader(f)
#
# Friend = namedtuple('Friend', header)
# lst = sorted(list(Friend(*i) for i in data), key =lambda x:(datetime.strptime(x.meeting_date,date_pattern),datetime.strptime(x.meeting_time,time_pattern) ))
# for i in lst:
#     print(i.surname, i.name)


### examples
# import csv
# from datetime import datetime
#
# with open('meetings.csv', 'r', encoding='UTF-8') as file:
#     a = csv.DictReader(file)
#     normal = sorted(a, key= lambda x: (datetime.strptime(x['meeting_date'], '%d.%m.%Y'), x['meeting_time'],  '%H:%M'))
#
# [print(f'{i["surname"]} {i["name"]}') for i in normal]



