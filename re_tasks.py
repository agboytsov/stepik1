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



