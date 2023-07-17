#6.9.22
# Зоопарк
# Вам доступен файл zoo.json, содержащий список JSON-объектов с данными об обитателях некоторого зоопарка. Ключом в каждом объекте является название животного, значением — их количество в зоопарке:
#
# [
#    {
#       "Axolotl": 11,
#       "Poison Frog": 12,
#       "Sonoran Toad": 6,
#       "Tiger Salamander": 16
#    },
#    {
#       "African Fish Eagle": 6,
#       "Andean Condor": 8,
#       "Black Vulture": 8,
#       "Bufflehead Duck": 9,
#       "Flamingo": 8,
#       "Great Horned Owl": 16,
#       "Hornbill": 1
#    },
#    ...
# ]
# Напишите программу, которая определяет, сколько всего животных обитает в зоопарке, и выводит полученный результат.
#
# Примечание 1. Гарантируется, что все ключи в JSON-объектах, различны.
#
# Примечание 2. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.
#
# Примечание 3. При открытии файла используйте явное указание кодировки UTF-8.
#
# import json
# from collections import ChainMap
# with open('zoo.json', 'r',encoding='UTF-8') as f:
#     data = json.load(f)
# res = sum(ChainMap(*data).values())
#
# print(res)


#6.9.23
#
# Булочный магнат
# После ухода сети Макдональдс из России Тимур решил открыть свою небольшую бургерную.
# Цена каждого бургера в его ресторане определяется количеством ингредиентов, которые выбирает сам посетитель.
# Вам доступны словари, в которых в качестве ключа указано название ингредиента, а в качестве значения — его цена.
# Все ингредиенты разбиты по категориям, например, овощи содержатся в одном словаре, соусы — в другом.
#
# Напишите программу, которая принимает на вход ингредиенты, выбранные посетителем, и определяет их общую стоимость.
#
# Формат входных данных
# На вход программе подается последовательность ингредиентов, разделенных запятой без пробелов.
#
# Формат выходных данных
# Программа должна определить общую стоимость введенных ингредиентов и вывести полученный результат в виде чека, в котором указаны ингредиенты в лексикографическом порядке, количество каждых и их общая стоимость, в следующем формате:
#
# <ингредиент 1> x <количество 1>
# <ингредиент 2> x <количество 2>
# ...
# -------------------------------
# ИТОГ: <общая стоимость>р
# Примечание 1. Программа должна добавлять нужное количество пробелов, если один ингредиент имеет меньшую длину, чем другие.
#
# Примечание 2. Длина пунктирной линии должна равняться длине самой длинной строки в чеке, включая строку с итоговой стоимостью.
#
# from collections import ChainMap, Counter
#
# bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
# meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
# sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
# vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
# toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}
#
# zakaz = sorted(input().split(','))
# data = Counter(zakaz)
# products = {}
# for i in zakaz:
#     products[i] = data[i]
# products_prices = ChainMap(bread,meat,sauce,vegetables,toppings)
# n = max(len(i) for i in zakaz)
# total_sum = 0
# result = []
# for k,v in products.items():
#     string = f'{k}{" "*(n-len(k))} x {v}'
#     print(string)
#     result.append(len(string))
#     total_sum += products_prices[k] * v
# footer = f'ИТОГ: {total_sum}р'
# result.append(len(footer))
# print('-'*max(result))
#
# print(footer)


###examples
# ings = ChainMap(bread, meat, sauce, vegetables, toppings)
# c = Counter(input().split(','))
# lines = [f'{i.ljust(len(max(c, key=len)))} x {j}' for i, j in sorted(c.items())]
# total = sum(ings[i] * j for i, j in c.items())
#
# print(*lines, '-' * len(max(lines, key=len)), f'ИТОГ: {total}р', sep='\n')

#6.10.13
#
#  Функция get_all_values()
# Реализуйте функцию get_all_values(), которая принимает два аргумента в следующем порядке:
#
# chainmap — объект типа ChainMap, элементами которого являются словари
# key — произвольный объект
# Функция должна возвращать множество, элементами которого являются все значения по ключу key из всех словарей в chainmap. Если ключ key отсутствует в chainmap, функция должна вернуть пустое множество.
#
# Примечание 1. Гарантируется, что передаваемый в функцию объект типа ChainMap содержит словари с хешируемыми значениями.
#
# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_all_values(), но не код, вызывающий ее.
#
# Примечание 3. Тестовые данные доступны по ссылкам:
#
# Архив с тестами
# GitHub
# Sample Input 1:
#
# chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
# result = get_all_values(chainmap, 'name')
#
# print(*sorted(result))
# Sample Output 1:
#
# Arthur Timur
# Sample Input 2:
#
# chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
# result = get_all_values(chainmap, 'age')
#
# print(result)
# Sample Output 2:
#
# set()
#
# from collections import ChainMap
# def get_all_values(chainmap, key):
#     res = set()
#     for mapping in chainmap.maps:
#         for k, v in mapping.items():
#             if k == key:
#                 res.add(v)
#     return res
# chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
# result = get_all_values(chainmap, 'age')
#
# print(result)


###examples
# from collections import ChainMap
#
# def get_all_values(chainmap, key):
#     return {d[key] for d in chainmap.maps if key in d}

#6.10.14
# Функция deep_update()
# Реализуйте функцию deep_update(), которая принимает три аргумента в следующем порядке:
#
# chainmap — объект типа ChainMap, элементами которого являются словари
# key — хешируемый объект
# value — произвольный объект
# Функция должна изменять все значения по ключу key во всех словарях в chainmap на value. Если ключ key отсутствует в chainmap, функция должна добавить пару key: value в первый словарь.
#
# Примечание 1. Функция должна изменять передаваемый объект типа ChainMap и возвращать значение None.
#
# Примечание 2. Гарантируется, что передаваемый в функцию объект типа ChainMap содержит хотя бы один словарь.
#
# Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию deep_update(), но не код, вызывающий ее.

# from collections import ChainMap
# def deep_update(chainmap, key, value):
#     all_keys = []
#     for mapping in chainmap.maps:
#         all_keys += [i for i in mapping.keys()]
#         if key in mapping.keys():
#             mapping[key] = value
#     if key not in all_keys:
#         chainmap[key] = value
#
#
#
# chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
# deep_update(chainmap, 'age', 20)
#
# print(chainmap)
#
#
# ###examples
# from collections import ChainMap
#
# def deep_update(chainmap, key, value):
#     if key in chainmap:
#         [dct.update({key: value}) for dct in chainmap.maps if key in dct]
#     else:
#         chainmap[key] = value

###
# from collections import ChainMap
# def deep_update(chainmap, key, value):
#     for i in chainmap.maps:
#         if key in i:
#             i[key] = value
#     chainmap.setdefault(key, value)


#6.10.15
# Функция get_value()
# Реализуйте функцию get_value(), которая принимает три аргумента в следующем порядке:
#
# chainmap — объект типа ChainMap, элементами которого являются словари
# key — произвольный объект
# from_left — булево значение, по умолчанию равное True
# Функция должна возвращать значение по ключу key из chainmap, причем:
#
# если from_left имеет значение True, поиск ключа в chainmap должен происходить от первого словаря к последнему
# если from_left имеет значение False, поиск ключа в chainmap должен происходить от последнего словаря к первому
# Если ключ key отсутствует в chainmap, функция должна вернуть значение None.
#
# Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_value(), но не код, вызывающий ее.

# from collections import ChainMap
# def get_value(chainmap, key, from_left=True):
#     if key not in chainmap:
#         return None
#     if from_left:
#         return chainmap[key]
#     else:
#         chainmap.maps.reverse()
#         return ChainMap(*chainmap.maps)[key]
#
# chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
#
# print(get_value(chainmap, 'name', False))
#
#
# ###examples
# from collections import ChainMap
#
# def get_value(chainmap, key, from_left=True):
#     if not from_left:
#         chainmap.maps.reverse()
#     return chainmap.get(key)