#4.5.14
#Количество файлов
#Вам доступен архив workbook.zip, содержащий различные папки и файлы. Напишите программу, которая выводит единственное число — количество файлов в этом архиве.
#
#Примечание 1. Обратите внимание, что папка не считается файлом.
#
#Примечание 2. Указанный архив доступен по ссылке. Ответ на задачу доступен по ссылке.
# from zipfile import ZipFile
# with ZipFile('workbook.zip') as zip_file:
#     info = zip_file.infolist()
#     res = int(sum([1 for i in info if not i.is_dir()]))
#     print(res)

#4.5.15
# from zipfile import ZipFile
# with ZipFile('workbook.zip') as zip_file:
#     info = zip_file.infolist()
#     original = sum(i.file_size for i in info)
#     compressed = sum(i.compress_size for i in info)
#     print(f'Объем исходных файлов: {original} байт(а)')
#     print(f'Объем сжатых файлов: {compressed} байт(а)')
#
# ###examples
# from zipfile import ZipFile
#
# with ZipFile('workbook.zip') as myzip:
#     a, b = map(sum, zip(*[(f.file_size, f.compress_size) for f in myzip.infolist()]))
#     print(f'Объем исходных файлов: {a} байт(а)')
#     print(f'Объем сжатых файлов: {b} байт(а)')

#4.5.16
# Наилучший показатель
# Вам доступен архив workbook.zip, содержащий различные папки и файлы. Напишите программу, которая выводит название файла из этого архива, который имеет наилучший показатель степени сжатия.
# from zipfile import ZipFile
# with ZipFile('workbook.zip') as zip_file:
#     info = zip_file.infolist()
#     best = [-100,'']
#     for i in info:
#         if not i.is_dir():
#             comp_coef = (i.file_size / i.compress_size)*100
#             if comp_coef > best[0]:
#                 best = [comp_coef,i.filename]
#     print(best[1].split('/')[-1])
# ### examples
# from zipfile import ZipFile
#
# with ZipFile("workbook.zip") as zip_file:
#     filelist = zip_file.infolist()
#     t = ((f.filename, f.compress_size/f.file_size) for f in filelist
#          if f.file_size != 0)
#     print(min(t, key=lambda x: x[1])[0].split("/")[-1])
#
# ###
# from zipfile import ZipFile
#
# with ZipFile('workbook.zip') as zip_file:
#     info = [i for i in zip_file.infolist() if not i.is_dir()]
#     print(min(info,key=lambda x:(x.compress_size/x.file_size)*100).filename.split('/')[-1])

#
# from pathlib import Path
# import zipfile
#
# def get_coeff(zipped_file: zipfile.ZipInfo) -> float:
#     return zipped_file.compress_size / zipped_file.file_size
#
# with zipfile.ZipFile('workbook.zip') as zf:
#     print(Path(min(filter(lambda x: not x.is_dir(), zf.infolist()), key=get_coeff).filename).name)

#4.5.17
# Избранные
# Вам доступен архив workbook.zip, содержащий различные папки и файлы. Напишите программу, которая выводит названия файлов из этого архива, которые были созданы или изменены позднее 2021-11-30 14:22:00. Названия файлов должны быть расположены в лексикографическом порядке, каждое на отдельной строке.
# from zipfile import ZipFile
#
# with ZipFile('workbook.zip') as zip_file:
#     info = [i for i in zip_file.infolist() if not i.is_dir()]
#     res = []
#     for i in info:
#         if i.date_time > (2021, 11, 30, 14, 22, 0):
#             res.append(i.filename.split('/')[-1])
#     print(*sorted(res),sep = '\n')
#

# 4.5.18
# Форматированный вывод
# Вам доступен архив workbook.zip, содержащий различные папки и файлы. Напишите программу, которая выводит названия всех файлов из этого архива в лексикографическом порядке, указывая для каждого его дату изменения, а также объем до и после сжатия, в следующем формате:
#
# <название файла>
#   Дата модификации файла: <дата изменения>
#   Объем исходного файла: <объем до сжатия> байт(а)
#   Объем сжатого файла: <объем после сжатия> байт(а)
# Между данными о двух файлах должна располагаться пустая строка.
#
# Примечание 1. Если файл находится в папке, вывести следует только название без пути.
#
# Примечание 2. Начальная часть ответа выглядит так (в качестве отступов используйте два пробела):
#
# Alexandra Savior – Crying All the Time.mp3
#   Дата модификации файла: 2021-11-30 13:27:02
#   Объем исходного файла: 5057559 байт(а)
#   Объем сжатого файла: 5051745 байт(а)
#
# Hollow Knight Silksong.exe
#   Дата модификации файла: 2013-08-22 08:20:06
#   Объем исходного файла: 805992 байт(а)
#   Объем сжатого файла: 494930 байт(а)
#
# from zipfile import ZipFile
# from datetime import datetime
# with ZipFile('workbook.zip') as zip_file:
#     info = sorted([[i.filename.split('/')[-1],i.date_time, i.file_size,i.compress_size] for i in zip_file.infolist() if not i.is_dir()],key = lambda x:x[0])
#     for i in info:
#         print(i[0])
#         print(f'  Дата модификации файла: {datetime(*i[1])}')
#         print(f'  Объем исходного файла: {i[2]} байт(а)')
#         print(f'  Объем сжатого файла: {i[3]} байт(а)')
#         print()
#
# ###examples
# #
# #
# # Поздеев Константин Викторович
# # 10 месяцев назад
# # os.path.basename заменяет все манипуляции с путем файла. Получается удобно
#
# Верное решение #718055053
# Python 3
# from zipfile import ZipFile
# import os
# import datetime
#
# with ZipFile('workbook.zip') as zip_file:
#     info = [i for i in zip_file.infolist() if not i.is_dir()]
#
#     for i in sorted(info, key=lambda x: os.path.basename(x.filename).lower()):
#         print(f"""{os.path.basename(i.filename)}
#   Дата модификации файла: {datetime.datetime(*i.date_time)}
#   Объем исходного файла: {i.file_size} байт(а)
#   Объем сжатого файла: {i.compress_size} байт(а)
# """)
#
# from zipfile import ZipFile, ZipInfo
# from datetime import datetime
#
# def about_file(file: ZipInfo):
#     return "\n".join((
#         f"{file.filename.split('/')[-1]}",
#         f"  Дата модификации файла: {datetime(*file.date_time)}",
#         f"  Объем исходного файла: {file.file_size} байт(а)",
#         f"  Объем сжатого файла: {file.compress_size} байт(а)"
#     ))
#
# with ZipFile("workbook.zip", "r") as zip_file:
#     data = [about_file(file) for file in zip_file.infolist() if not file.is_dir()]
#     print(*sorted(data), sep="\n\n")


#4.5.19
# Вам доступен набор различных файлов, названия которых представлены в списке file_names. Дополните приведенный ниже код, чтобы он создал архив files.zip и добавил в него все файлы из данного списка.

# from zipfile import ZipFile
#
# # file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
# #               'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
# #               'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']
#
# file_names = ['name_log.csv','pools.json']
#
# with ZipFile('files.zip', mode='w') as zip_file:
#     for i in file_names:
#         zip_file.write(i)

#4.5.20
# Вам доступен набор различных файлов, названия которых представлены в списке file_names. Также вам доступен архив files.zip.
# Дополните приведенный ниже код, чтобы он добавил в архив files.zip только те файлы из списка file_names, объем которых не превышает
# 100 байт.
#
# Примечание 1. Получить объем файла в байтах позволяет функция getsize() из модуля os.path.
# Данная функция принимает в качестве аргумента путь к файлу и возвращает размер указанного файла в байтах.
#
# Например, вычислить объем архива files.zip в байтах и сохранить его в переменную size можно следующим образом:
#
# import os.path
# from zipfile import ZipFile
#
# # # file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
# # #               'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
# # #               'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']
# #
# file_names = ['name_log.csv','pools.json']
#
# with ZipFile('files.zip', mode='a') as zip_file:
#     for i in file_names:
#         if os.path.getsize(i) < 100:
#             zip_file.write(i)
#
# ### examples
# from zipfile import ZipFile
#
# file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
#               'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
#               'Alexandra Savior – Crying All the Time.mp3', 'homework.py','test.py']
#
# with ZipFile('files.zip', mode='w') as zip_file:
#     for file_name in file_names:
#         with open(file_name, 'rb') as bite_file:
#             size = len(bite_file.read())
#         if size < 100:
#             zip_file.write(file_name, file_name)

# ###
# from zipfile import ZipFile
#
# def check_size(file_name, max_size=100):
#     with open(file_name, 'rb') as file:
#         chunk = file.read(120)
#     return len(chunk) < max_size
#
# file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
#               'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
#               'Alexandra Savior – Crying All the Time.mp3', 'homework.py','test.py']
#
# with ZipFile('files.zip', 'w') as zip_file:
#     [*map(lambda file: zip_file.write(file), filter(check_size, file_names))]


#4.5.21
# Функция extract_this()
# Реализуйте функцию extract_this(), которая принимает один или более аргументов в следующем порядке:
#
# zip_name — название zip архива, например, data.zip
# *args — переменное количество позиционных аргументов, каждый из которых является названием некоторого файла
# Функция должна извлекать файлы *args из архива zip_name в папку с программой. Если в функцию не передано ни одного названия файла для извлечения, то функция должна извлечь все файлы из архива.
#
# Примечание 1. Например, следующий вызов функции
#
# extract_this('workbook.zip', 'earth.jpg', 'exam.txt')
# должен извлечь из архива workbook.zip файлы earth.jpg и exam.txt в папку с программой.
#
# Вызов функции
#
# extract_this('workbook.zip')
# должен извлечь из архива workbook.zip все файлы в папку с программой.
#
# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию extract_this(), но не код, вызывающий ее.

#
# def extract_this(zip, *args):
#     from zipfile import ZipFile
#     with ZipFile(zip, 'r') as zip_file:
#         if args:
#             for i in args:
#                 zip_file.extract(i)
#         else:
#             zip_file.extractall()
#
#
# # ###examples
# # from zipfile import ZipFile
# #
# #
# # def extract_this(zip_name: str, *args):
# #     if not args:
# #         args = None
# #     with ZipFile(zip_name) as zf:
# #         zf.extractall(members=args)
#
# ###
# from zipfile import ZipFile
#
#
# def extract_this(zip_name: str, *args):
#     with ZipFile(zip_name) as zf:
#         zf.extractall(members=args or None)


#4.5.22
# Шахматы были лучше 🌶️
# Вам доступен архив data.zip, содержащий различные папки и файлы. Среди них есть несколько JSON файлов, каждый из которых содержит информацию о каком-либо футболисте:
#
# {
#    "first_name": "Gary",
#    "last_name": "Cahill",
#    "team": "Chelsea",
#    "position": "Defender"
# }
# У футболиста имеются следующие атрибуты:
#
# first_name — имя
# last_name — фамилия
# team — название футбольного клуба
# position — игровая позиция
# Напишите программу, которая обрабатывает только данные JSON файлы и выводит имена и фамилии футболистов, выступающих за футбольный клуб Arsenal. Футболисты должны быть расположены в лексикографическом порядке имен, а при совпадении — в лексикографическом порядке фамилий, каждый на отдельной строке.
#
# Примечание 1. Обратите внимание, что наличие у файла расширения .json не гарантирует, что он является корректным текстовым файлом в формате JSON. Для того чтобы определить, является ли файл корректным текстовым файлом в формате JSON, воспользуйтесь конструкцией try-except и функцией is_correct_json() из предыдущего урока.
#
# Примечание 2. Начальная часть ответа выглядит так:
#
# Alex Iwobi
# Alexis Sanchez
# ...

#
# def is_correct_json(string):
#     import json
#     try:
#         l = json.loads(string)
#         return True
#     except:
#         return False
# import json
# from zipfile import ZipFile
#
# with ZipFile('data.zip') as zip_file:
#     jsons =  [i for i in zip_file.infolist() if not i.is_dir() and i.filename.endswith('.json')]
#     res = []
#     for i in jsons:
#         with zip_file.open(i.filename) as file:
#
#             try:
#                 string = file.read().decode('utf-8')
#                 data = json.loads(string)
#                 if data['team'] == 'Arsenal':
#                     res.append((data['first_name'],data['last_name']))
#
#             except Exception as ex:
#                 continue
# for i in sorted(res,key = lambda x:(x[0],x[1])):
#     print(i[0], i[1])
#
# ### examples
# from zipfile import ZipFile
# import json
#
# def jsloads(z, n):
#     try:
#         with z.open(n) as f:
#             return json.loads(f.read().decode('utf-8'))
#     except:
#         return {'team': ''}
#
# with ZipFile('data.zip') as z:
#     names = [n for n in z.namelist() if n[-5:] == '.json']
#     n = {i['first_name'] + ' ' + i['last_name'] for n in names for i in [jsloads(z, n)] if i['team'] == 'Arsenal'}
#     print(*sorted(n), sep='\n')

#4.5.23
# Структура архива 🌶️🌶️
# Вам доступен архив desktop.zip, содержащий различные папки и файлы. Напишите программу, которая выводит его файловую структуру и объем каждого файла.
#
# Формат входных данных
# На вход программе ничего не подается.
#
# Формат выходных данных
# Программа должна вывести файловую структуру архива desktop.zip и объем каждого файла в несжатом виде. Так как архив имеет собственную иерархию папок, каждый уровень вложенности должен быть выделен двумя пробелами.
#
# Примечание 1. Вывод на примере архива test.zip из конспекта:
#
# test
#   Картинки
#     1.jpg 88 KB
#     avatar.png 19 KB
#     certificate.png 43 KB
#     py.png 33 KB
#     World_Time_Zones_Map.png 2 MB
#     Снимок экрана.png 11 KB
#   Неравенства.djvu 5 MB
#   Программы
#     image_util.py 5 KB
#     sort.py 61 B
#   Разные файлы
#     astros.json 505 B
# Примечание 2. Объем файла записывается в самых крупных единицах измерения с округлением до целых.
#
# Примечание 3. Значения единиц измерения такие же, какие приняты в информатике:
#
# 1 KB = 1024 B
# 1 MB = 1024 KB
# 1 GB = 1024 MB
# from zipfile import ZipFile
# def convert_bytes(size):
#     """Конвертер байт в большие единицы"""
#     if size < 1024:
#         return f'{size} B'
#     elif 1024 <= size < 1024**2:
#         return f'{round(size / 1024)} KB'
#     elif 1024**2 <= size < 1024**3:
#         return f'{round(size / 1024**2)} MB'
#     else:
#         return f'{round(size / 1024**3)} GB'
#
# with ZipFile('desktop.zip') as zip_file:
#     info = zip_file.infolist()
#     for i in info:
#         lst = i.filename.split('/')
#         name = ''
#         if lst[-1]:
#             name = lst[-1]
#             spaces = "  " * (len(lst)-1)
#         else:
#             spaces = "  "*(len(lst)-2)
#         print(f'{spaces}{name if name else lst[len(lst)-2]} {convert_bytes(i.file_size) if not i.is_dir() else ""}')
#
#
# ### examples
# from zipfile import ZipFile
#
# def hr_size(n, k = 0):
#     return f"{round(n)} {['B', 'KB', 'MB', 'GB', 'TB'][k]}" if n < 1024 else hr_size(n / 1024, k + 1)
#
# with ZipFile('workbook.zip') as z:
#     for i in z.infolist():
#         p = i.filename.strip('/').split('/')
#         print('  ' * (len(p) - 1) + p[-1] + ('' if i.is_dir() else ' ' + hr_size(i.file_size)))
# from zipfile import ZipFile
#
#
# def convert_bytes(size, counter=0):
#     sort_units = ('B', 'KB', 'MB', 'GB')
#     while size > 1023:
#         size /= 1024
#         counter += 1
#     return f' {round(size)} {sort_units[counter]}' if size else ''
#
#
# with ZipFile('desktop.zip') as zip_file:
#     for f in zip_file.infolist():
#         name = f.filename.strip('/').split('/')
#         spaces = (len(name) - 1) * '  '
#         print(spaces + name[-1] + convert_bytes(f.file_size))


