#4.6.16
# Одинокая функция
# Дан pickle файл, содержащий единственную сериализованную функцию. Напишите программу, которая вызывает данную функцию с заданными аргументами и выводит возвращаемое значение функции.
#
# Формат входных данных
# На вход программе в первой строке подается название pickle файла, в котором содержится единственная сериализованная функция. Далее подается произвольное количество строк, каждая из которых содержит позиционный аргумент для этой функции.
#
# Формат выходных данных
# Программа должна вызвать функцию из указанного pickle файла со всеми введенными строковыми аргументами, и вывести возвращаемое значение функции. Причем аргументы должны быть переданы в том порядке, в котором они были введены.
#
# Примечание 1. Аргументы, передаваемые в функцию, должны иметь тип str.
#
# Примечание 2. Рассмотрим первый тест. Сначала подается название файла — func.pkl, в котором содержится сериализованная функция:
#
# def func(*args):
#     return ' '.join(args)
# затем аргументы для этой функции: Hello,, how, are, you и today?.
#
# Программа выводит результат следующего вызова:
#
# func('Hello,', 'how', 'are', 'you', 'today?')
# Примечание 3. Для считывания произвольного количества строк используйте потоковый ввод sys.stdin.
#
# Примечание 4. Считайте, что вводимый файл находится в папке с программой.
#
# Примечание 5. В этой задаче за кулисами реализовано две функции с именами func и add. Не используйте эти имена для именования своих переменных во избежание ошибок.

# import pickle
#
# filename, *arg_list = [i.strip('\n') for i in open(0)]
#
# with open(filename, 'rb') as file:
#     fun = pickle.load(file)
#     print(fun(*arg_list))

#4.6.17
# Ты не пройдешь
# Реализуйте функцию filter_dump(), которая принимает три аргумента в следующем порядке:
#
# filename — название pickle файла, например, data.pkl
# objects — список произвольных объектов
# typename — тип данных
# Функция должна создавать pickle файл с названием filename, который содержит сериализованный список только тех объектов из списка objects, тип которых равен typename.
#
# Примечание 1. Например, вызов функции filter_dump() следующим образом:
#
# filter_dump('numbers.pkl', [1, '2', 3, 4, '5'], int)
# должен создавать файл numbers.pkl, содержащий сериализованный список [1, 3, 4].
#
# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию filter_dump(), но не код, вызывающий ее.
#
# def filter_dump(filename, objects, typename):
#     import pickle
#     new_lst = []
#     for object in objects:
#         if type(object) is typename:
#             new_lst.append(object)
#     with open(filename, 'wb') as f:
#         pickle.dump(new_lst,f)
#
# ### examples
# def filter_dump(filename, objects, typename):
#     with open(filename, 'wb') as f:
#         __import__('pickle').dump([i for i in objects if type(i) is typename], f)
###
# def filter_dump(filename, objects, typename):
#     with open(filename, 'wb') as out:
#         l = list(filter(lambda x: type(x) is typename, objects))
#         __import__('pickle').dump(l, out)


#4.6.18
#
# Контрольная сумма
# По каналу связи передаются pickle файл, содержащий сериализованный словарь или список, и целое число — контрольная сумма, которая вычисляется по следующему правилу:
#
# для словаря — сумма всех целочисленных ключей (тип int)
# для списка — произведение минимального и максимального целочисленных элементов (тип int)
# Напишите программу, которая вычисляет контрольную сумму для объекта, содержащегося в pickle файле, и сравнивает ее с данным целым числом.
#
# Формат входных данных
# На вход программе в первой строке подается название pickle файла, в котором содержится сериализованный словарь или список, в следующей — целое число.
#
# Формат выходных данных
# Программа должна вычислить контрольную сумму для объекта, который содержится в данном pickle файле, и
#
# если она совпадает с введенным числом, вывести текст:
# Контрольные суммы совпадают
# если она не совпадает с введенным числом, вывести текст:
# Контрольные суммы не совпадают
# Примечание 1. Если список (словарь) не содержит целочисленных элементов (ключей), то считайте, что контрольная сумма равна
# 0
# 0.
#
# Примечание 2. Рассмотрим первый тест. Подается название файла — data.pkl, в котором содержится сериализованный список:
#
# ['a', 'b', 3, 4, 'f', 'g', 7, 8]
# затем число —
# 3023
# 3023. Контрольная сумма для данного списка равна
# 3
# ⋅
# 8
# =
# 24
# 3⋅8=24. Так как
# 3023
# ≠
# 24
# 3023
# 
# =24, программа выводит:
#
# Контрольные суммы не совпадают
# Примечание 3. Подробнее про контрольную сумму можно почитать тут.
#
# Sample Input 1:
#
# data.pkl
# 3023
# Sample Output 1:
#
# Контрольные суммы не совпадают
# Sample Input 2:
#
# data2.pkl
# 3319
# Sample Output 2:
#
# Контрольные суммы совпадают

# import pickle
# filename, hash_sum = str(input()), int(input())
# with open(filename,'rb') as pkl:
#     data = pickle.load(pkl)
#     res = []
#
#     if type(data) is list:
#         for i in data:
#             if type(i) is int:
#                 res.append(i)
#         res_bool = (min(res,default=0)* max(res,default=0)) == hash_sum
#     elif type(data) is dict:
#         for i in data.keys():
#             if type(i) is int:
#                 res.append(i)
#         res_bool = (sum(res,start=0)) == hash_sum
#
# print('Контрольные суммы не совпадают' if not res_bool else 'Контрольные суммы совпадают')

# ###examples
# import pickle
#
# name, sm = input(), int(input())
# with open(name, 'rb') as f:
#     obj = pickle.load(f)
#     lst = [i for i in obj if type(i) == int] or [0]
#     check = sum(lst) if type(obj) == dict else max(lst)*min(lst)
#     print(['Контрольные суммы не совпадают', 'Контрольные суммы совпадают'][sm == check])

# ###
# with open(input(), 'rb') as file:
#     f, sum_ = __import__('pickle').load(file), int(input())
#     if type(f) is dict:
#         l = sum([i for i in f if type(i) is int])
#     else:
#         l = sorted(filter(lambda x: type(x) is int, f)) or [0]
#         l = l[0] * l[-1]
#     print(f'Контрольные суммы {("не ", "")[l == sum_]}совпадают')

# import pickle
#
# filename = input()
# checksum = int(input())
#
# with open(filename, 'rb') as file:
#     data = pickle.load(file)
#
#     if isinstance(data, dict):
#         tmp = [key for key in data if type(key) is int]
#         res = sum(tmp) if tmp else 0
#     elif isinstance(data, list):
#         tmp = list(filter(lambda x: type(x) is int, data))
#         res = min(tmp) * max(tmp) if tmp else 0
#
# print('Контрольные суммы совпадают' if res == checksum else 'Контрольные суммы не совпадают')