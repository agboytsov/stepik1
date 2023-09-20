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

# 10.6.19
# Уважение
# На электронную почту Тимура нередко приходят письма с предложением о сотрудничестве. Тимур ценит взаимное уважение и считает письмо достойным внимания, если оно начинается с одного из следующих выражений:

# Здравствуйте
# Доброе утро
# Добрый день
# Добрый вечер
# Напишите программу, которая определяет, является ли письмо достойным внимания Тимура.

# import re

# pattern = r'(^Здравствуйте.*)|(^Доброе утро.*)|(^Добрый день.*)|(^Добрый вечер.*)'

# print(True if re.match(pattern,input(), re.IGNORECASE) else False)


### examples
# import re

# message = input()
# pattern = r"^Здравствуйте|^Доброе утро|^Добрый (день|вечер).*"

# match = re.match(pattern, message, re.I)
# print(bool(match))

# ###
# import re

# print(bool(re.search(r'^здравствуйте|^доброе утро|^добрый день|^добрый вечер', input(), re.IGNORECASE)))

# 10.6.20
# Социальные сети
# Вам доступен набор популярных публикаций из социальной сети Твиттер, которые могут иметь следующий вид:

# Люблю курсы BEEGEEK!
# Когда курс по ООП? @timur_guev
# BEEGEEK, спасибо за курсы, вы лучшие! #python #BeeGeek
# и т.д.
# Напишите программу, которая определяет, в скольких публикациях содержится строка beegeek.

# Формат входных данных
# На вход программе подается произвольное число строк, каждая из которых представляет очередную публикацию.

# Формат выходных данных
# Программа должна определить, в скольких введенных строках содержится строка beegeek в произвольном регистре, и вывести полученный результат.

# import re

# count = 0 
# pattern = r'beegeek'

# for string in open(0):
#     if re.search(pattern, string, re.I):
#         count += 1

# print(count)  

# 11.7.10
# Вам доступна переменная article, содержащая некоторый многострочный текст. Дополните приведенный ниже код, чтобы он определил:

# количество строк, которые начинаются со слова Stepik (в произвольном регистре);
# количество строк, которые оканчиваются тремя точками ... или восклицательным знаком !.
# и вывел два соответствующих числа, каждое на отдельной строке.

# article = '''Stepik (до августа 2016 года Stepic) — это образовательная платформа и конструктор онлайн-курсов!

# Первые образовательные материалы были выпущены на Stepik 3 сентября 2013 года.
# В январе 2016 года Stepik выпустил мобильные приложения под iOS и Android. В 2017 году разработаны мобильные приложения для изучения ПДД в адаптивном режиме для iOS и Android...

# На октябрь 2020 года на платформе зарегистрировано 5 миллионов пользователей!
# Stepik позволяет любому зарегистрированному пользователю создавать интерактивные обучающие уроки и онлайн-курсы, используя видео, тексты и разнообразные задачи с автоматической проверкой и моментальной обратной связью. 

# Проект сотрудничает как с образовательными учреждениями, так и c индивидуальными преподавателями и авторами.  
# Stepik сегодня предлагает онлайн-курсы от образовательных организаций, а также индивидуальных авторов!

# Система автоматизированной проверки задач Stepik была использована в ряде курсов на платформе Coursera, включая курсы по биоинформатике от Калифорнийского университета в Сан-Диего и курс по анализу данных от НИУ «Высшая школа экономики»...

# Stepik также может функционировать как площадка для проведения конкурсов и олимпиад, среди проведённых мероприятий — отборочный этап Олимпиады НТИ (2016—2020) (всероссийской инженерной олимпиады школьников, в рамках программы Национальная технологическая инициатива), онлайн-этап акции Тотальный диктант в 2017 году, соревнования по информационной безопасности StepCTF-2015...'''

# pat1 = r'^([Ss]tepik)'

# stepik = re.findall(pat1, article, re.I|re.MULTILINE)
# print(len(stepik))

# pat2 = r'(\.{3})|(\!)'

# tochki = re.findall(pat2, article, re.MULTILINE)
# print(len(tochki))

# 11.7.11
# Подслова
# Напишите программу, которая принимает на вход строку текста и некоторое слово и определяет, сколько раз данное слово встречается как подслово в введенном тексте.

# Формат входных данных
# На вход программе на первой строке подается текст, на второй — слово.

# Формат выходных данных
# Программа должна определить, сколько раз данное слово встречается как подслово в введенном тексте, и вывести полученный результат.

# Примечание 1. Словом будем считать последовательность символов, соответствующих \w, окруженную символами, соответствующими \W. Подсловом же будет являться последовательность символов, соответствующих \w, окруженную символами, соответствующими \w. Например, is является подсловом optimist, а age не является подсловом ageless.

# Примечание 2. Программа должна учитывать регистр. То есть, например, слова Python и python считаются разными.

# import re
# string, to_find = input(), input()

# pat = f'\B{to_find}\B'

# result = re.findall(pat,string)
# print(len(result))

# 11.7.12
# Слова
# Напишите программу, которая принимает на вход строку текста и некоторое слово и определяет, сколько вхождений данного слова содержится в введенном тексте.

# Формат входных данных
# На вход программе на первой строке подается текст, на второй — слово.

# Формат выходных данных
# Программа должна определить, сколько вхождений данного слова содержится в веденном тексте, и вывести полученный результат.

# Примечание 1. Словом будем считать последовательность символов, соответствующих \w, окруженную символами, соответствующими \W.

# Примечание 2. Рассмотрим первый тест, в котором содержится 
# 6
# 6 вхождений слова foo:

# foo bar (foo) bar foo-bar foo_bar foo'bar bar-foo bar, foo.
# foo_bar же является самостоятельным словом.


# import re

# string, to_find = input(), input()

# pattern = fr'\b{to_find}\b'
# result = re.findall(pattern,string)
# print(len(result))


# 11.7.13
# Одинаковые и разные 🍕
# Американский английский и Британский английский языки имеют несколько различий, одно из которых наблюдается в написании слов. Например, слова, написанные на Американском английском языке и имеющие суффикс ze, в Британском варианте языка часто записываются с использованием суффикса se. 

# Напишите программу, которая определяет, сколько раз слово встречается в тексте, учитывая его Британско-Американское написание.

# Формат входных данных
# На вход программе на первой строке подается слово, которое может быть записано как в Британском, так в Американском варианте, а на следующей — текст.

# Формат выходных данных
# Программа должна определить, сколько раз введенное слово встречается в тексте, учитывая его Британско-Американское написание, и вывести полученный результат.

# Примечание 1. Словом будем считать последовательность символов, соответствующих \w, окруженную символами, соответствующими \W.

# Примечание 2. Программа должна игнорировать регистр. То есть, например, слова Python и python считаются одинаковыми.

to_find, string  = input(), input()
to_find = to_find[:-2]
pattern = fr'\b({to_find}[zs]e)\b'
result = re.findall(pattern,string, re.I)
print(len(result))

# 11.7.14
# Одинаковые и разные ☕️
# В одной из предыдущих задач мы уже наблюдали различие в написании Британских и Американских слов. Еще одно различие заключается в том, что Британия сохранила использование сочетания букв our в своих словах, в то время как Америка отказалась от буквы u и использует лишь or.

# Напишите программу, которая определяет, сколько раз слово встречается в тексте, учитывая его Британско-Американское написание.

# Формат входных данных
# На вход программе на первой строке подается слово, которое записано в Британском варианте, а на следующей — текст.

# Формат выходных данных
# Программа должна определить, сколько раз введенное слово встречается в тексте, учитывая его Британско-Американское написание, и вывести полученный результат.

# Примечание 1. Словом будем считать последовательность символов, соответствующих \w, окруженную символами, соответствующими \W.

# Примечание 2. Гарантируется, что введенное слово состоит из 
# 4
# 4 или более букв.

# Примечание 3. Программа должна игнорировать регистр. То есть, например, слова Python и python считаются одинаковыми.

# import re

# to_find, string  = input(), input()
# to_find = to_find[:-3]

# pattern = fr'\b{to_find}(our|or)\b'
# result = re.findall(pattern,string, re.I)
# print(len(result))

# 11.7.15

# Функция abbreviate()
# Аббревиатура — слово, образованное сокращением слова или словосочетания и читаемое по алфавитному названию начальных букв или по начальным звукам слов, входящих в него.

# Реализуйте функцию abbreviate(), которая принимает один аргумент:

# phrase — фраза
# Функция должна создавать из фразы phrase аббревиатуру в верхнем регистре и возвращать её.

# Примечание 1. В аббревиатуре должны присутствовать как начальные буквы слов, так и начальные буквы подслов, начинающихся с заглавной буквы, например, JavaScript Object Notation -> JSON.

# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию abbreviate(), но не код, вызывающий ее.

# import re

# def abbreviate(phrase):
#     result = re.findall(r'(\b.)|([A-Z])',phrase)
#     string = ''
#     for i in result:
#         for j in i:
#             if j and j != ' ':
#                 string += j.upper()
#     return string  


### examples
# def abbreviate(phrase):
#     return ''.join(re.findall(r'[A-Z]|\b\w',phrase)).upper()

# ###
# import re
# from itertools import chain

# def abbreviate(phrase):
#     return ''.join(chain.from_iterable(re.findall(r'\b(\w[A-Z]*)|\w([A-Z]+)', phrase))).upper()

#11.7.16
# HTML 🌶️
# HTML-элементы — основа языка HTML. Каждый HTML-элемент обозначается начальным (открывающим) и конечным (закрывающим) тегами. Открывающий и закрывающий теги содержат имя элемента. Открывающий тег может содержать дополнительную информацию — атрибуты и значения атрибутов. Гиперссылки в языке HTML создаются с помощью тега <a></a>. Внутрь помещается текст, который будет отображаться на веб-странице. Обязательной составляющей тега <a></a> является атрибут href, который задает URL-адрес веб-страницы:

# <a href="https://stepik.org">Stepik</a>  
# Гиперссылка состоит из двух частей — указателя (Stepik) и адресной части (https://stepik.org). Указатель ссылки представляет собой фрагмент текста или изображение, видимые для пользователя. Адресная часть ссылки пользователю не видна, она представляет собой адрес ресурса, к которому необходимо перейти. Иногда указатель может быть окружен различными тегами (<b></b>, <h1></h1>):

# <a href="https://stepik.org"><b><h1>Stepik</h1></b></a>
# Напишите программу, которая находит во фрагменте HTML-страницы все гиперссылки и выводит их составляющие — адресные части и указатели.

# Формат входных данных
# На вход программе подается произвольное количество строк, которые образуют фрагмент HTML-страницы.

# Формат выходных данных
# Программа должна найти в введенном фрагменте HTML-страницы все гиперссылки и вывести их составляющие — адресные части и указатели, в следующем формате:
# <адресная часть>, <указатель>
# ...
# Примечание 1. Порядок следования данных об очередной гиперссылке должен совпадать с порядком их следования в введенном фрагменте HTML-страницы.


# import re

# link = r'<a href=\"(.*)">(.*)</a>'
# for string in open(0):
#     res = re.findall(link, string)
#     if res:
#         print(f'{res[0][0]}, {res[0][1]}')


### examples
# import sys
# import re

# text = sys.stdin.read()
# pattern = r'<a href="(.+)">(.+)</a>'

# for address, pointer in re.findall(pattern, text):
#     print(f'{address}, {pointer}')


###
# import re

# for i in open(0):
#     a = re.search(r'<a href="(.*)">(.*)</a', i.strip())
#     if a:
#         print(a.group(1) + ', ' +  a.group(2))


#11.7.17

# HTML 🌶️🌶️
# HTML-элементы — основа языка HTML. Каждый HTML-элемент обозначается начальным (открывающим) и конечным (закрывающим) тегами. Открывающий и закрывающий теги содержат имя элемента. Открывающий тег может содержать дополнительную информацию — атрибуты и значения атрибутов:

# <b>BeeGeek</b>
# <a href="https://stepik.org">Stepik</a>
# В примере выше тег <b> не содержит никаких атрибутов, а тег <a> содержит атрибут href со значением https://stepik.org.

# Напишите программу, которая находит во фрагменте HTML-страницы все атрибуты каждого тега.

# Формат входных данных
# На вход программе подается произвольное количество строк, которые образуют фрагмент HTML-страницы.

# Формат выходных данных
# Программа должна найти в введенном фрагменте HTML-страницы все теги и вывести их, указав для каждого соответствующие атрибуты. Теги вместе со всеми атрибутами должны быть расположены каждый на отдельной строке, в следующем формате:

# <тег>: <атрибут>, <атрибут>, ...
# Теги, а также атрибуты тегов, должны быть расположены в лексикографическом порядке.

# import re


# def tag_parse(line):
#     all_dict = {}
   
#     start = re.search(r'<(\w+).*?>',line)
        
#     while start:
#         tag = re.match(r'.?<(\w+)',start.group()).group(1)
#         end = re.search(rf'</{tag}>', line)
#         tag_attrs = re.findall(r' (\S+)=', line[start.span()[0]:start.span()[1]])
#         line = line[start.span()[1]:]

#         if all_dict.get(tag):
#             all_dict[tag] += tag_attrs
#         else:
#             all_dict[tag] = tag_attrs
            
#         start = re.search(r'<(\w+).*?>',line, re.M)
        
#         if not start:
            
#             break

#     return all_dict

# result = {}

# string = [i.strip() for i in open(0)]
# string = "".join(string)

# result = tag_parse(string)

# for res in sorted(result):
#     tag_attrs = ', '.join(sorted(set(result[res])))
#     print(f'{res}: {tag_attrs}')

### examples
# import re

# res = {}
# for line in open(0):
#     for tag, params in re.findall(r'<(\w+)(.*?)>', line):
#         res.setdefault(tag, set()).update(re.findall(r'([\w-]+)=', params))

# for key in sorted(res):
#     print(f'{key}: {", ".join(sorted(res[key]))}')

###

# import sys
# from bs4 import BeautifulSoup

# soup = BeautifulSoup(sys.stdin.read(), 'html.parser')
# dct = {i.name: i.attrs.keys() for i in soup.find_all(True)}

# for k, v in sorted(dct.items()):
#     print(f'{k}: {", ".join(sorted(v))}')


###
# import re

# data = re.findall(r'<(\w+)(.*?)>', open(0).read())
# d = {}

# for teg, items in data:
#     items = re.findall(r' (.+?)=".*?"', items) or ['']
#     [d.setdefault(teg, set()).add(item) for item in items]
    
# for k in sorted(d):
#     print(f'{k}: {", ".join(sorted(filter(None, d[k])))}')


# 11.8.9
# Функция normalize_jpeg()
# Реализуйте функцию normalize_jpeg(), которая принимает один аргумент:

# filename — название файла, имеющее расширение jpeg или jpg, которое может быть записано буквами произвольного регистра
# Функция должна возвращать новое название файла с нормализованным расширением — jpg.

# import re

# def normalize_jpeg(filename):
#     result = re.sub(r'(.*)\.jpe?g',r'\1.jpg',filename, flags=re.I)
#     return result

# 11.8.10
# Функция normalize_whitespace()
# Реализуйте функцию normalize_whitespace(), которая принимает один аргумент:

# string — произвольная строка
# Функция должна заменять все множественные пробелы в строке string на единственный пробел и возвращать полученный результат.

import re

def normalize_whitespace(string):
    return re.sub(r'( ){2,}', r' ', string)

# 11.8.11

# Ключевые слова
# В Python существуют ключевые слова, которые нельзя использовать для названия переменных, функций и классов. Для получения списка всех ключевых слов можно воспользоваться атрибутом kwlist из модуля keyword.

# Приведенный ниже код:

# import keyword

# print(keyword.kwlist)
# выводит:

# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# Напишите программу, которая принимает строку текста и заменяет в ней все ключевые слова на <kw>.

# Формат входных данных
# На вход программе подается строка.

# Формат выходных данных
# Программа должна в введенном тексте заменить все ключевые слова (в любом регистре) на строку <kw> и вывести полученный результат.



# import keyword, re

# string = input()

# for kw in keyword.kwlist:
#     string = re.sub(rf'\b{kw}\b', r'<kw>', string, flags=re.I)
    
# print(string)


### examples
# import re
# import keyword

# keys = '|'.join(keyword.kwlist)

# print(re.sub(fr"\b({keys})\b", r'<kw>', input(), flags=re.I))


# ###
# import keyword, re

# print(re.sub(fr'\b({"|".join(reversed(keyword.kwlist))})\b', '<kw>', input(), flags=re.I))

# 11.8.12
# Первые буквы
# Напишите программу, которая меняет местами первые две буквы в каждом слове, состоящем из двух или более букв.

# Формат входных данных
# На вход программе подается строка, содержащая слова.

# Формат выходных данных
# Программа должна в введенной строке заменить первые две буквы в каждом слове, состоящем из двух или более букв, и вывести полученный результат.

# Примечание 1. Словом будем считать последовательность символов, соответствующих \w, окруженную символами, соответствующими \W.

# import re

# string = input()

# pattern = r'\b(\w)(\w)(\w*)'

# print(re.sub(pattern, r'\2\1\3', string))

### examples
from re import sub

print(sub(r'\b(\w)(\w)', r'\2\1', input()))

# 11.8.13

# Умножение строк
# Назовем умножением строки на число запись в формате n(string), где n — неотрицательное целое число, а string — строка, которая должна быть записана n раз. Раскрытием умножения будем считать развернутый вариант данной записи, например, строка ti2(Be)3(Ge) после раскрытия в ней всех умножений будет иметь вид tiBeBeGeGeGe.

# Напишите программу, которая раскрывает все умножения в тексте и выводит полученный результат.

# Формат входных данных
# На вход программе подается одна строка, содержащая строчные латинские буквы, числа и скобки.

# Формат выходных данных
# Программа должна вывести строку, в которой раскрыты все умножения с учетом приоритетности операций.

# Примечание 1. Гарантируется, что умножение в подаваемой строке всегда записано корректно, то есть строго в формате n(string). Записи вида 4(2), 3q, (fg)7 не корректны.

# Примечание 2. Рассмотрим третий тест. С учетом приоритетности операций сначала раскрываем умножение 2(a) и получаем промежуточную строку bbbb10(aa)bbb, далее раскрываем умножение 10(aa) и получаем конечный результат в виде строки bbbbaaaaaaaaaaaaaaaaaaaabbb.

# Примечание 3. Строка, в которой раскрыты все умножения, всегда содержит исключительно строчные латинские буквы.

# Примечание 4. Максимальная длина результирующей строки не превосходит 
# 450000 символов.

# put your python code here
import re

def expand_multiplications(text):
    pattern = r'(\d+)\(([^()]+)\)'  

    def replace(match):
        count = int(match.group(1)) 
        string = match.group(2)  
        return expand_multiplications(string) * count

    while True:
        expanded_text, num_replacements = re.subn(pattern, replace, text)  
        if num_replacements == 0:
            break 
        text = expanded_text

    return text

                            
        

    
print(expand_multiplications(input()))


### examples

from re import subn

s, n = input(), 1

while n:
    s, n = subn(r'(\d+)\((\w*)\)', lambda m: m[2] * int(m[1]), s)

print(s)


###


import re


def mult_string(match):
    n, string = match.group(1, 2)
    return string * int(n)


def unpuck_string(string):
    res = re.sub(r'(\d+)\((\w+?)\)', mult_string, string)
    if string == res:
        return res
    else:
        return unpuck_string(res)


print(unpuck_string(input()))


###

import re

s = input()

while '(' in s:
    s = re.sub(r'(\d+)\((\w+)\)', lambda match_onj: int(match_onj[1]) * match_onj[2], s)

print(s)


# 11.8.14
# Повторяющиеся слова 🌶️
# Напишите программу, которая заменяет все повторяющиеся рядом стоящие слова на одно слово.

# Формат входных данных
# На вход программе подается строка, содержащая слова.

# Формат выходных данных
# Программа должна в введенной строке заменить все повторяющиеся рядом стоящие слова на одно слово и вывести полученный результат.

# Примечание 1. Программа должна быть чувствительной к регистру, то есть, например, слова python и Python считаются различными.

# Примечание 2. Словом будем считать последовательность символов, соответствующих \w, окруженную символами, соответствующими \W.
import re

def remove_dpl_words(text):
    pattern = r'\b(\w+)\W+\1\b'  

    while re.search(pattern, text):
        text = re.sub(pattern, r'\1', text) 

    return text

print(remove_dpl_words(input()))


### examples 
from re import sub

pattern = r'(\b\w+\b)(\W+\1\b)+'

print(sub(pattern, r'\1', input()))


###
import re

s = input()
regex = r'\b(\b\w+\b)\W+\1\b'

while re.search(regex, s):
    s = re.sub(regex, r'\1', s)

print(s)



### 11.9.10
# Точка с запятой
# Напишите программу, которая разбивает строку по символам точки, запятой и точки с запятой.
import re

result = re.split(r'\s*[,;.]\s*', input())

print(*result)


# 11.9.11
# Логическое выражение
# Дано логическое выражение, состоящее из переменных, а также операторов |, &, and или or. Напишите программу, которая разбивает данную строку по указанным операторам.

import re

result = re.split(r'\s*\|\s*|\s*\&\s*|\s*or\s*|\s*and\s*\b', input())

print(*result, sep=', ')


# 11.9.12

# Функция multiple_split()
# Реализуйте функцию multiple_split(), которая принимает два аргумента:

# string — строка
# delimiters — список строк
# Функция должна разбивать строку string на подстроки, используя в качестве разделителей строки из списка delimiters, и возвращать полученный результат в виде списка.

# Примечание 1. Другими словами, функция multiple_split() должна работать аналогично строковому методу split(), за тем исключением, что delimiters может содержать не единственный разделитель, а целый набор разделителей.


import re

def multiple_split(string, delimiters):
    delimiters = [re.escape(i) for i in delimiters]
    result = re.split(rf'{"|".join(delimiters)}', string)
    return result


# 11.9.19
# Сумма чисел
# Напишите программу, которая складывает все натуральные числа в строке, находящиеся в указанном диапазоне индексов.

# Формат входных данных
# На вход программе сначала подаются два целых числа 
# �
# a и 
# �
# b, больших или равных 
# 0
# 0, разделенные пробелом, а затем — строка.

# Формат выходных данных
# Программа должна вывести сумму всех натуральных чисел в введенной строке, находящихся в диапазоне индексов от 
# �
# a (включительно) до 
# �
# b (не включительно). Если в указанном диапазоне нет ни одного числа, программа должна вывести 
# 0
# 0.

# put your python code her
a, b = (int(i) for i in input().split())
import re

regex_obj = re.compile(r'\d+')

string = input()
result = sum((int(i) for i in regex_obj.findall(string, pos=a,endpos=b)))
print(result)

    


