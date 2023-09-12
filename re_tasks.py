#11.6.9

# Телефонные номера
# Вам доступен набор телефонных номеров, имеющих следующие форматы:

# <код страны>-<код города>-<номер>
# <код страны> <код города> <номер>
# в котором код страны и код города представлены последовательностями от одной до трех цифр включительно, а номер — последовательностью от четырех до десяти цифр включительно. Между кодом страны, кодом города и номером используется разделитель, которым служит либо символ дефис, либо пробел, причем одновременно оба вида разделителя в одном номере присутствовать не могут.

# Напишите программу, которая принимает произвольное количество телефонных номеров и для каждого выводит отдельно его код страны, код города и номер.

from re import match


def num_parser(num):
    parsed = match(r'(\d+)[ -]?(\d+)[ -]?(\d+)',num)
    country_code = parsed.group(1)
    city_code = parsed.group(2)
    number = parsed.group(3)
    
    return country_code, city_code, number
    
  
# for i in open(0):
#     codes = num_parser(i)
#     print(f'Код страны: {codes[0]}, Код города: {codes[1]}, Номер: {codes[2]}')

###examples
import re
import sys

pattern = r"(?P<country>\d{1,3})([ -]?)(?P<city>\d{1,3})\2(?P<number>\d{4,10})"
for number in map(str.rstrip, sys.stdin):
    match = re.fullmatch(pattern, number)
    groups = match.groupdict()
    print(f"Код страны: {groups['country']}, Код города: {groups['city']}, Номер: {groups['number']}")
###
import sys
from re import search

pattern=r'(\d{1,3})([ -])(\d{1,3})\2(\d{4,10})'
for c in map(str.strip, sys.stdin):
    country, city, number =search(pattern, c).group(1,3,4)
    print(f'Код страны: {country}, Код города: {city}, Номер: {number}')


# 11.6.10
# Онлайн-школа BEEGEEK
# В онлайн-школе BEEGEEK логин учетной записи определяется следующим образом:

# первым символом является символ нижнего подчеркивания _
# затем следуют одна или более цифр
# после записываются ноль или более латинских букв в произвольном регистре
# логин может иметь на конце необязательный символ нижнего подчеркивания _
# Напишите программу, которая принимает произвольное количество строк и определяет, какие из них представляют собой корректный логин онлайн-школы BEEGEEK.

from re import match

def right_login(login):
    pattern = r'^(_)\d+[a-zA-Z]*\1?$'
    
    test = match(pattern, login)
    
    return True if test is not None else False

# for login in open(0):
#     print(right_login(login))


### examples

# import re
# import sys

# reg = r'_\d+[a-zA-Z]*_?'

# for i in sys.stdin:
#     grou = re.fullmatch(reg, i.strip())
#     print(bool(grou))

###
# import re
# import sys

# pattern = r"_\d+[A-z]*_?"
# for login in map(str.rstrip, sys.stdin):
#     match = re.fullmatch(pattern, login)
#     print(bool(match))

# 11.6.11
# Одинаковые слоги
# Напишите программу, которая выводит слова, состоящие из двух одинаковых слогов.

# Формат входных данных
# На вход программе подается произвольное количество слов, каждое на отдельной строке.

# Формат выходных данных
# Программа должна из введенных слов вывести только те, которые состоят из двух одинаковых слогов. Слова должны быть расположены в своем исходном порядке, каждое на отдельной строке.

# Примечание 1. Словом будем считать любую непрерывную последовательность из одного или нескольких символов, соответствующих \w.


# from re import fullmatch

# for i in open(0):
#     if fullmatch(r'^([\w]{2,})\1$',i.strip()):
#         print(i, end = '')

### examples

# import sys
# import re

# for line in map(str.rstrip, sys.stdin):
#     if re.fullmatch(r'(\w+)\1', line):
#         print(line)

# 10.6.12


# Beegeek
# Напишите программу, определяющую:

# количество строк, в которых bee встречается в качестве подстроки не менее двух раз
# количество строк, в которых geek встречается в качестве слова хотя бы один раз
# Формат входных данных
# На вход программе произвольное количество строк, каждая из которых содержит набор произвольных символов.

# Формат выходных данных
# Программа должна вывести два числа:

# первое — количество строк, в которых bee встречается в качестве подстроки не менее двух раз
# второе — количество строк, в которых geek встречается в качестве слова хотя бы один раз
# каждое на отдельной строке.

# Примечание 1. Словом будем считать любую непрерывную последовательность из одного или нескольких символов, соответствующих \w.

# Примечание 2. Строка может одновременно удовлетворять обоим условиям.

# Примечание 3. В первой строке первого теста bee встречается в качестве подстроки 
# 3 раза:

# beebee bee
# Во второй строке bee встречается в качестве подстроки лишь один раз, а слово geek отсутствует.

# В третьей строке bee встречается в качестве подстроки 
# 2 раза, geek в качестве слова — 
# 1 раз:

# bee geek bee


# # put your python code here
# from re import match

# bee = 0
# geek = 0

# pat1 = r'.*(bee).*\1.*'
# pat2 = r'(.*)?\bgeek\b(.*)?'

# for word in open(0):
#     if match(pat1,word):
#         bee += 1
#     if match(pat2,word):
#         geek += 1

# print(bee,geek, sep='\n')


### EXAMPLES

# import re
# import sys

# bee_pattern = r".*(bee).*\1.*"
# geek_pattern = r".*\bgeek\b.*"
# bee_counter, geek_counter = 0, 0
# for bg in map(str.rstrip, sys.stdin):
#     bee_match = re.fullmatch(bee_pattern, bg)
#     geek_match = re.fullmatch(geek_pattern, bg)
#     bee_counter += int(bool(bee_match))
#     geek_counter += int(bool(geek_match))
# print(bee_counter)
# print(geek_counter)


# ###
# import sys
# import re

# bee = geek = 0

# for line in sys.stdin:
#     if re.search(r'bee.*bee', line):
#         bee += 1
#     if re.search(r'\bgeek\b', line):
#         geek += 1
        
# print(bee)
# print(geek)


# 10.6.13
# Популярность
# В онлайн-школе BEEGEEK мы всегда следим за тем, насколько растет наша популярность. Для этого мы собираем публикации из различных соцсетей, которые содержат вхождения строки beegeek в нижнем регистре. Мы оцениваем публикацию:

# в 3 балла, если она начинается и заканчивается строкой beegeek
# в 2 балла, если она только начинается или только заканчивается строкой beegeek
# в 1 балл, если она содержит строку beegeek только внутри
# в 0 баллов, если она не содержит строку beegeek
# Напишите программу, которая определяет популярность онлайн-школы BEEGEEK путем суммирования баллов всех публикаций.

# Формат входных данных
# На вход программе подается произвольное число строк, каждая из которых представляет очередную публикацию.

# Формат выходных данных
# Программа должна определить, во сколько баллов оценивается каждая введенная публикация, и вывести сумму всех полученных баллов.

# Примечание 1. Если публикация представляет собой просто строку beegeek, то она оценивается в 2 балла.

# import re

# def count_beegeek(string):
#     if re.match(r'^(beegeek).*\1$',string):
#         return 3
#     elif re.match(r'(^beegeek.*)|(.*beegeek$)',string) or re.match(r'beegeek',string) :
#         return 2
#     elif re.match(r'.*beegeek.*',string):
#         return 1
#     else:
#         return 0
# total = 0
# for string in [i.strip() for i in open(0)]:

#     total += count_beegeek(string)

# print(total)

### examples
# import re
# import sys

# patterns = [
#     r"^beegeek.*beegeek$",
#     r"^beegeek.*|.*beegeek$",
#     r".*beegeek.*"
# ]

# def get_score(text: str) -> int:
#     for score, pattern in enumerate(patterns, start=-3):
#         match = re.search(pattern, text)
#         if match:
#             return abs(score)
#     return 0

# scores = 0
# for text in map(str.rstrip, sys.stdin):
#     scores += get_score(text)
# print(scores)


###
# import sys
# import re

# rating = 0

# for line in map(str.rstrip, sys.stdin):
#     if re.fullmatch(r'beegeek.*beegeek', line):
#         rating += 3
#     elif re.fullmatch(r'^beegeek.*|.*beegeek$', line):
#         rating += 2
#     elif re.fullmatch(r'.+beegeek.+', line):
#         rating += 1
        
# print(rating)

