# -*- coding: utf-8 -*-

#6.5.19
# Вам доступен список кортежей data с данными о доходах некоторого образовательного ресурса. Первым элементом кортежа является название продукта, вторым — прибыль в долларах.
#
# Дополните приведенный ниже код, чтобы он определил, какой общий доход принес каждый продукт и вывел названия всех продуктов, указав для каждого соответствующую общую прибыль. Продукты должны быть расположены в лексикографическом порядке, каждый на отдельной строке, в следующем формате:
#
# <продукт>: $<общая прибыль>
# Примечание. Начальная часть ответа выглядит так:
#
# Books: $7969
# Courses: $2991
# ...
#
# from collections import defaultdict
#
# data = [('Books', 1343), ('Books', 1166), ('Merch', 616), ('Courses', 966), ('Merch', 1145), ('Courses', 1061), ('Books', 848), ('Courses', 964), ('Tutorials', 832), ('Merch', 642), ('Books', 815), ('Tutorials', 1041), ('Books', 1218), ('Tutorials', 880), ('Books', 1003), ('Merch', 951), ('Books', 920), ('Merch', 729), ('Tutorials', 977), ('Books', 656)]
# result = defaultdict(int)
#
# for i in data:
#     result[i[0]] += i[1]
#
# result = {k:v for k, v in sorted(result.items())}
# for k,v in result.items():
#     print(f'{k}: ${v}')


###examples
# result = defaultdict(int)
#
# for key, value in data:
#     result[key] += value
#
# for key, value in sorted(result.items()):
#     print(f'{key}: ${value}')

#6.5.20

# Вам доступен список кортежей staff с данными о сотрудниках некоторой компании. Первым элементом кортежа является название отдела, вторым — имя и фамилия сотрудника, работающего в этом отделе.
#
# Дополните приведенный ниже код, чтобы он определил, какое число сотрудников работает в каждом отделе и вывел названия всех отделов, указав для каждого соответствующее количество сотрудников. Отделы должны быть расположены в лексикографическом порядке, каждый на отдельной строке, в следующем формате:
#
# <отдел>: <количество сотрудников>
# Примечание. Начальная часть ответа выглядит так:
#
# Accounting: 17
# Developing: 7
# ...


from collections import defaultdict

staff = [('Sales', 'Robert Barnes'), ('Developing', 'Thomas Porter'), ('Accounting', 'James Wilkins'), ('Sales', 'Connie Reid'), ('Accounting', 'Brenda Davis'), ('Developing', 'Miguel Norris'), ('Accounting', 'Linda Hudson'), ('Developing', 'Deborah George'), ('Developing', 'Nicole Watts'), ('Marketing', 'Billy Lloyd'), ('Sales', 'Charlotte Cox'), ('Marketing', 'Bernice Ramos'), ('Sales', 'Jose Taylor'), ('Sales', 'Katie Warner'), ('Accounting', 'Steven Diaz'), ('Accounting', 'Kimberly Reynolds'), ('Accounting', 'John Watts'), ('Accounting', 'Dale Houston'), ('Developing', 'Arlene Gibson'), ('Marketing', 'Joyce Lawrence'), ('Accounting', 'Rosemary Garcia'), ('Marketing', 'Ralph Morgan'), ('Marketing', 'Sam Davis'), ('Marketing', 'Gail Hill'), ('Accounting', 'Michelle Wright'), ('Accounting', 'Casey Jenkins'), ('Sales', 'Evelyn Martin'), ('Accounting', 'Aaron Ferguson'), ('Marketing', 'Andrew Clark'), ('Marketing', 'John Gonzalez'), ('Developing', 'Wilma Woods'), ('Sales', 'Marie Cooper'), ('Accounting', 'Kay Scott'), ('Sales', 'Gladys Taylor'), ('Accounting', 'Ann Bell'), ('Accounting', 'Craig Wood'), ('Accounting', 'Gloria Higgins'), ('Marketing', 'Mario Reynolds'), ('Marketing', 'Helen Taylor'), ('Marketing', 'Mary King'), ('Accounting', 'Jane Jackson'), ('Marketing', 'Carol Peters'), ('Sales', 'Alicia Mendoza'), ('Accounting', 'Edna Cunningham'), ('Developing', 'Joyce Rivera'), ('Sales', 'Joseph Lee'), ('Sales', 'John White'), ('Marketing', 'Charles Bailey'), ('Sales', 'Chester Fernandez'), ('Sales', 'John Washington')]

result = defaultdict(int)

for worker in staff:
    result[worker[0]] += 1

for key in sorted(result.keys()):
    print(f'{key}: {result[key]}')