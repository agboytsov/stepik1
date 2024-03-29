#10.8.15

# Функция tabulate()
# Реализуйте функцию tabulate(), которая принимает один аргумент:
#
# func — произвольная функция
# Функция tabulate() должна возвращать итератор, генерирующий бесконечную последовательность возвращаемых значений
# функции func сначала с аргументом 1, затем 2, затем 3, и так далее.

def tabulate(func):
    counter = 1
    while True:
        yield func(counter)
        counter += 1

### examples

from itertools import count

def tabulate(func):
    return map(func, count(1))

from itertools import count

def tabulate(func):
    for i in count(1):
        yield func(i)

# 10.8.16

# Функция factorials()
# Реализуйте функцию factorials() с использованием функции accumulate(), которая принимает один аргумент:
#
# n — натуральное число
# Функция должна возвращать итератор, генерирующий последовательность из n чисел, каждое из которых является
# факториалом очередного натурального числа.


from itertools import accumulate
import operator

def factorials(n):
    yield from accumulate(range(1,n+1),operator.mul)

### examples
def factorials(n):
    yield from accumulate(range(1, n + 1), lambda x, y: x * y)

#10.8.17
# Функция alnum_sequence()
# Реализуйте функцию alnum_sequence(), которая не принимает никаких аргументов.
#
# Функция должна возвращать итератор, циклично генерирующий бесконечную последовательность натуральных чисел и заглавных
# латинских букв:

# 1,A,2,B,3,C,..,X,25,Y,26,Z
import string
from itertools import cycle


def alnum_sequence():

    letters = string.ascii_uppercase
    digits = range(1,27)
    all_lst = (elem for t in zip(digits, letters) for elem in t)
    yield from cycle(all_lst)


### examples
def alnum_sequence():
    for item in zip(cycle(range(1, 27)), cycle(ascii_uppercase)):
        yield from item

#10.8.17
# Функция roundrobin() 🌶️
# Реализуйте функцию roundrobin(), которая принимает произвольное количество позиционных аргументов, каждый из которых
# является итерируемым объектом.
#
# Функция должна возвращать итератор, генерирующий последовательность из элементов всех переданных итерируемых объектов:
# сначала первый элемент первого итерируемого объекта, затем первый элемент второго итерируемого объекта, и так далее;
# после второй элемент первого итерируемого объекта, затем второй элемент второго итерируемого объекта, и так далее.
#
# Примечание 1. Элементы итерируемых объектов в возвращаемом функцией итераторе должны располагаться в своем исходном
# порядке.
#
# Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.


from itertools import zip_longest

def roundrobin(*args):
    s = ''
    for i in  zip_longest(*args, fillvalue=s):
        for j in i:
            if j == s:
                continue
            yield j

### examples


from itertools import cycle

def take(iterable, n):
    for elem, _ in zip(iterable, range(n)):
        yield elem

def roundrobin(*iterables):
    non_empty = len(iterables)
    iterables = cycle(map(iter, iterables))
    while non_empty:
        try:
            for it in iterables:
                yield next(it)
        except StopIteration:
            non_empty -= 1
            iterables = cycle(take(iterables, non_empty))

###
def roundrobin(*args):
    iters = tuple(iter(a) for a in args)
    while True:
        err_counter = 0
        for i in iters:
            try: res = next(i)
            except: err_counter += 1
            else: yield res
        if err_counter == len(iters):
            break
###
from itertools import zip_longest

def roundrobin(*args):
    return (j for i in zip_longest(*args, fillvalue='') for j in i if j != '')

###

def roundrobin(*iterables):
    rez = [iter(i) for i in iterables]
    flag = True
    while flag:
        flag = False
        for it in rez:
            for i in it:
                yield i
                flag = True
                break


# 10.9.12
# Функция drop_while_negative()
# Реализуйте функцию drop_while_negative(), которая принимает один аргумент:
#
# iterable — итерируемый объект, элементами которого являются целые числа
# Функция должна возвращать итератор, генерирующий все числа итерируемого объекта iterable,
# начиная с первого неотрицательного числа.
#
# Примечание 1. Элементы итерируемого объекта в возвращаемом функцией итераторе должны располагаться
# в своем исходном порядке.
#
# Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

from itertools import dropwhile

def drop_while_negative(iterable):
    return dropwhile(lambda x: x < 0, iterable)


# 10.9.13
# Функция drop_this()
# Реализуйте функцию drop_this(), которая принимает два аргумента в следующем порядке:
#
# iterable — итерируемый объект
# obj — произвольный объект
# Функция должна возвращать итератор, генерирующий последовательность элементов итерируемого объекта iterable,
# начиная с элемента, не равного obj.
#
# Примечание 1. Элементы итерируемого объекта в возвращаемом функцией итераторе должны располагаться
# в своем исходном порядке.
#
# Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

from itertools import dropwhile
def drop_this(iterable, obj):
    return dropwhile(lambda x: x == obj, iterable)
### examples
drop_this = lambda iterable, obj: __import__('itertools').dropwhile(lambda x: x == obj, iterable)
###
from itertools import dropwhile

def drop_this(iterable, obj):
    yield from dropwhile(lambda x: x == obj, iterable)

# 10.9.14
# Функция first_true()
# Реализуйте функцию first_true(), которая принимает два аргумента в следующем порядке:
#
# iterable — итерируемый объект
# predicate — функция-предикат; если имеет значение None, то работает аналогично функции bool()
# Функция first_true() должна возвращать первый по счету элемент итерируемого объекта iterable, для которого функция
# predicate вернула значение True. Если такого элемента нет, функция first_true() должна вернуть значение None.
#
# Примечание 1. Предикат — это функция, которая возвращает True или False в зависимости от переданного
# в качестве аргумента значения.
#
# Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.


def first_true(iterable, func):
    if not func:
        func = bool
    for i in filter(func, iterable):
        return i


### examples
def first_true(iterable, func):
    return next(filter(func, iterable), None)


# 10.9.15
# Функция take()
# Реализуйте функцию take(), которая принимает два аргумента в следующем порядке:
#
# iterable — итерируемый объект
# n — натуральное число
# Функция должна возвращать итератор, генерирующий последовательность из первых n элементов итерируемого объекта iterable.
#
# Примечание 1. Элементы итерируемого объекта в возвращаемом функцией итераторе должны располагаться
# в своем исходном порядке.
#
# Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.
from itertools import islice

def take(iterable, n):
    return islice(iterable,n)
#
# from itertools import islice as take

# 10.9.16

# Функция take_nth()
# Реализуйте функцию take_nth(), которая принимает два аргумента в следующем порядке:
#
# iterable — итерируемый объект
# n — натуральное число

from itertools import islice
def take_nth(iterable, n):
    it = iter(iterable)
    for i in range(n):
        try:
            a = next(it)
            if i == n-1:
                return a
        except StopIteration:
            return

### examples

from itertools import islice

def take_nth(iterable, n):
    return next(islice(iterable, n-1, None), None)

###
from itertools import islice
def take_nth(iterable, n: int):
    try:
        return next(islice(iterable, n-1, n))
    except:
        return None

###
from itertools import compress
def take_nth(iterable,n):
    return next(compress(iterable,[False]*(n-1)+[True]),None)


#10.9.17

# Функция first_largest()
# Реализуйте функцию first_largest(), которая принимает два аргумента в следующем порядке:
#
# iterable — итерируемый объект, элементами которого являются целые числа
# number — произвольное число
# Функция должна возвращать индекс первого элемента итерируемого объекта iterable, который больше number.
# Если таких элементов нет, функция должна вернуть число −1.
#
# Примечание 1. Рассмотрим список чисел
# 10,2,14,7,7,18,20 из первого теста. Первым числом, превосходящим 11, является число
# 14, которое имеет индекс  2.
#
# Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

def first_largest(iterable, num):
    for i, el in enumerate(iterable):
        if el > num:
            return i
    return -1


### examples
from itertools import compress, count

first_largest = lambda it, n: next(compress(count(), (i>n for i in it)), -1)

###
#import itertools as it


def first_largest(iterable, number):
    return next(it.dropwhile(lambda x: x[1] <= number, enumerate(iterable)), [-1])[0]


###
#from itertools import starmap, pairwise

#numbers = [1, 2, 3, 4, 5]

#print(*starmap(lambda a, b: a + b, pairwise(numbers)))

#10.10.13
# Функция sum_of_digits()
# Реализуйте функцию sum_of_digits(), которая принимает один аргумент:
#
# iterable — итерируемый объект, элементами которого являются натуральные числа
# Функция должна возвращать единственное число — сумму цифр всех чисел, присутствующих в итерируемом объекте iterable.
#
# Примечание 1. Рассмотрим набор чисел
#
# 13,20,41,2,2,5 из первого теста. Сумма цифр всех представленных чисел будет равна:
#
# 1+3+2+0+4+1+2+2+5=20


from itertools import chain

def sum_of_digits(iterable):
    return sum(map(int,chain.from_iterable(map(str, iterable))))


### examples

from itertools import chain


def sum_of_digits(iterable):
    strings = map(str, iterable)
    all_elements = chain.from_iterable(strings)
    int_digits = map(int, all_elements)
    return sum(int_digits)


#10.10.14

#   Функция is_rising()
# Реализуйте функцию is_rising(), которая принимает один аргумент:
#
# iterable — итерируемый объект, элементами которого являются числа
# Функция должна возвращать True, если элементы итерируемого объекта расположены строго по возрастанию, или False
# в противном случае.


#from itertools import pairwise  #python 3.10

def is_rising(iterable):
    new = pairwise(iterable)
    func = lambda x: x[0] < x[1]
    return all(map(func, new))


### examples
# def is_rising(iterable):
#     return all(a < b for a, b in pairwise(iterable))
#
# ###
# from itertools import pairwise, starmap
# def is_rising(iterable):
#     return all(starmap(lambda a, b: a < b, pairwise(iterable)))



# 10.10.15
#
# Функция max_pair()
# Реализуйте функцию max_pair(), которая принимает один аргумент:
#
# iterable — итерируемый объект, элементами которого являются числа
# Функция должна возвращать единственное число — максимальную сумму двух соседних чисел итерируемого объекта iterable.
#
# Примечание 1. Рассмотрим список чисел
# 1,8,2,4,3 из первого теста. Из данной последовательности можно получить следующие пары соседних элементов:
# 1 и 8,
# 8 и 2,
# 2 и 4,
# 4 и 3. Максимальную сумму имеет вторая пара — 10.


def max_pair(iterable):
    new = pairwise(iterable)
    func = lambda x: x[0] + x[1]
    return max(map(func, new))


### examples

def max_pair(iterable):
    return max(map(sum, pairwise(iterable)))

def max_pair(iterable):
    return max(sum(x) for x in pairwise(iterable))


# 10.10.16

# Функция ncycles()
# Реализуйте функцию ncycles(), которая принимает два аргумента в следующем порядке:
#
# iterable — итерируемый объект
# times — натуральное число
# Функция должна возвращать итератор, генерирующий последовательность элементов итерируемого объекта iterable,
# зацикленных times раз.

from itertools import tee, chain
def ncycles(iterable, times):
    a = tee(iterable, times)
    return chain.from_iterable(a)

#10.10.17

# Функция grouper()
# Реализуйте функцию grouper(), которая принимает два аргумента в следующем порядке:
#
# iterable — итерируемый объект
# n — натуральное число
# Функция должна возвращать итератор, генерирующий последовательность, элементами которой являются
# объединенные в кортежи по n элементов соседние элементы итерируемого объекта iterable.
# Если у элемента не достаточно соседей, то ими становится значение None.

from itertools import zip_longest

def grouper(iterable, n):
    args = [iter(iterable)] * n
    return zip_longest(*args)


### examples

from itertools import repeat, zip_longest

def grouper(iterable, n):
    return zip_longest(*repeat(iter(iterable), n))


def grouper(iterable, n):
    it = iter(iterable)
    return ((elem, *(next(it, None) for i in range(n-1))) for elem in it)


#10.11.10
#
# Вам доступен именованный кортеж Person, который содержит данные о человеке. Первым элементом именованного кортежа
# является имя человека, вторым — возраст, третьим — рост. Также доступен список persons, содержащий эти кортежи.
#
# Дополните приведенный ниже код, чтобы он сгруппировал людей из данного списка по их росту и вывел полученные группы.
# Для каждой группы сначала должен быть указан рост, а затем через запятую перечислены имена людей,
# имеющих соответствующий рост. Группы должны быть расположены в порядке увеличения роста, каждая на отдельной строке,
# имена в группах — в алфавитном порядке, в следующем формате:
#
# <рост>: <имя>, <имя>, ...
# Примечание. Начальная часть ответа выглядит так:
#
# 158: Ariana, Eva
# 172: Mark
# ...


# from collections import namedtuple
# from itertools import groupby
#
# Person = namedtuple('Person', ['name', 'age', 'height'])
#
# persons = [Person('Tim', 63, 193), Person('Eva', 47, 158),
#            Person('Mark', 71, 172), Person('Alex', 45, 193),
#            Person('Jeff', 63, 193), Person('Ryan', 41, 184),
#            Person('Ariana', 28, 158), Person('Liam', 69, 193)]
#
# result = groupby(sorted(persons, key=lambda x: (x.height, x.name)), key= lambda x: x.height)
#
# for key, values in result:
#     print(f'{key}: {", ".join([i.name for i in values])}')

#10.11.11

# Вам доступен именованный кортеж Student, который содержит данные об ученике. Первым элементом именованного кортежа
# является фамилия ученика, вторым — имя, третьим — класс. Также доступен список students, содержащий эти кортежи.
#
# Дополните приведенный ниже код, чтобы он вывел наиболее часто встречаемое имя среди учеников из данного списка.
#
# Примечание. Гарантируется, что искомое имя единственное.

#
# from collections import namedtuple
# from itertools import groupby
#
# Student = namedtuple('Student', ['surname', 'name', 'grade'])
#
# students = [Student('Гагиев', 'Александр', 10), Student('Дедегкаев', 'Илья', 11), Student('Кодзаев', 'Георгий', 10),
#             Student('Набокова', 'Алиса', 11), Student('Кораев', 'Артур', 10), Student('Шилин', 'Александр', 11),
#             Student('Уртаева', 'Илина', 11), Student('Салбиев', 'Максим', 10), Student('Капустин', 'Илья', 11),
#             Student('Гудцев', 'Таймураз', 11), Student('Перчиков', 'Максим', 10), Student('Чен', 'Илья', 11),
#             Student('Елькина', 'Мария', 11),Student('Макоев', 'Руслан', 11), Student('Албегов', 'Хетаг', 11),
#             Student('Щербак', 'Илья', 10), Student('Идрисов', 'Баграт', 11), Student('Гапбаев', 'Герман', 10),
#             Student('Цивинская', 'Анна', 10), Student('Туткевич', 'Юрий', 11), Student('Мусиков', 'Андраник', 11),
#             Student('Гадзиев', 'Георгий', 11), Student('Белов', 'Юрий', 11), Student('Акоева', 'Диана', 11),
#             Student('Денисов', 'Илья', 11), Student('Букулова', 'Диана', 10), Student('Акоева', 'Лера', 11)]
#
# names_grouped = groupby(sorted([student.name for student in students]))
# max_result = max(names_grouped, key=lambda tpl: sum(1 for i in tpl[1]))
# print(max_result[0])


### examples
#
# group_iter = groupby(sorted(students, key=lambda x: x.name), key=lambda x: x.name)
# max_result = max(group_iter, key=lambda tpl: sum(1 for i in tpl[1]))
# print(max_result[0])


# students.sort(key=lambda x: x.name)
# data = groupby(students, key=lambda x: x.name)
# print(max(data, key=lambda x: sum(1 for _ in x[1]))[0])


#10.11.12

# Группы слов
# Напишите программу, которая группирует слова по их длине.
#
# Формат входных данных
# На вход программе подается последовательность слов, разделенных пробелом. Каждое слово записано строчными латинскими
# буквами.
#
# Формат выходных данных
# Программа должна сгруппировать введенные слова по их длине и вывести полученные группы. Для каждой группы должна
# быть указана длина, а затем через запятую перечислены слова, имеющие соответствующую длину. Группы должны быть
# расположены в порядке увеличения длины, каждая на отдельной строке, слова в группах — в алфавитном порядке,
# в следующем формате: <длина> -> <слово>, <слово>, ...
#
# from itertools import groupby
# lst = sorted(input().split(), key=lambda x: (len(x), x))
# lst = groupby(lst, key=len)
# for k, v in lst:
#     print(f'{k} -> {", ".join(v)}')
#
# ### examples
# for k, v in groupby(sorted(input().split(), key = len), key = len):
#     print(f'{k} -> {", ".join(sorted(v))}')

#10.11.13
# Нет дел
# Каждый день Тимур записывает в блокнот дела, которые ему нужно выполнить. Каждое дело он разбивает на несколько действий.
#
# Вам доступен список tasks, в котором записаны все дела Тимура. Каждый элемент списка представляет собой кортеж из трех
# элементов: первый — название дела, второй — действие, третий — очередность.
#
# Дополните приведенный ниже код, чтобы он вывел все дела Тимура в алфавитном порядке, указав для каждого набор
# соответствующих действий в правильной очередности, в следующем формате:
#
# <дело>:
#     1. <действие>
#     2. <действие>
#     ...
# Между двумя делами должна быть расположена пустая строка.
#
# Примечание 1. Начальная часть ответа выглядит так (в качестве отступов используйте четыре пробела):
#
# ЕГЭ Математика:
#     1. доделать курс по параметрам
#
# Курс по ооп:
#     1. обсудить темы
#     2. обсудить задачи
#
# ...
from itertools import groupby

tasks = [('Отдых', 'поспать днем', 3),
        ('Ответы на вопросы', 'ответить на вопросы в дискорде', 1),
        ('ЕГЭ Математика', 'доделать курс по параметрам', 1),
        ('Ответы на вопросы', 'ответить на вопросы в курсах', 2),
        ('Отдых', 'погулять вечером', 4),
        ('Курс по ооп', 'обсудить темы', 1),
        ('Урок по groupby', 'добавить задачи на программирование', 3),
        ('Урок по groupby', 'написать конспект', 1),
        ('Отдых', 'погулять днем', 2),
        ('Урок по groupby', 'добавить тестовые задачи', 2),
        ('Уборка', 'убраться в ванной', 2),
        ('Уборка', 'убраться в комнате', 1),
        ('Уборка', 'убраться на кухне', 3),
        ('Отдых', 'погулять утром', 1),
        ('Курс по ооп', 'обсудить задачи', 2)]

# sorted_tasks = sorted(tasks, key=lambda x:(x[0],x[2]))
# grouped_tasks = groupby(sorted_tasks, key=lambda x: x[0])
#
# for key, task_iter in grouped_tasks:
#     print(f'{key}:')
#     for task in task_iter:
#         print(f'    {task[2]}. {task[1]}')
#     print()



#10.11.14

# Функция group_anagrams()
# Анаграммы — это слова, которые состоят из одинаковых букв. Например:
#
# адаптер — петарда
# адресочек — середочка
# азбука — базука
# аистенок — осетинка
# Реализуйте функцию group_anagrams(), которая принимает один аргумент:
#
# words — список слов
# Функция должна группировать в кортежи слова из списка words, являющиеся анаграммами, и возвращать список полученных
# кортежей.
#
# Примечание 1. Порядок кортежей в возвращаемом функцией списке, а также порядок элементов в этих кортежах, не важен.

from itertools import groupby
def group_anagrams(words: list):
    temp = groupby(sorted(words, key=lambda x: sorted(x)),key=lambda x: sorted(x))
    result = []
    for k, v in temp:
        result.append(tuple([*v]))
    return result


### examples

def group_anagrams(words):
    return (tuple(i) for _, i in groupby(sorted(words, key=sorted), key=sorted))



#10.11.15
# Функция ranges() 🌶️
# Будем считать, что последовательность целых неотрицательных чисел можно преобразовать в отрезок, если разница между
# соседними элементами этой последовательности равна единице. Например, числа
# 3,4,5,6,7,8 можно преобразовать в отрезок
# [3;8]. Числа 1,3,5,11,15,22 в отрезок преобразовать нельзя. Одиночное число преобразуется в отрезок, в котором и
# правой,
# и левой границей является оно само. Например, число
#
# 1 можно преобразовать в отрезок
# [1;1].
#
# Реализуйте функцию ranges(), которая принимает один аргумент:
#
# numbers — список различных натуральных чисел, расположенных в порядке возрастания
# Функция должна преобразовывать числа из списка numbers в отрезки, представляя их в виде кортежей, где первый элемент
# кортежа является левой границей отрезка, второй элемент — правой границей отрезка. Полученные кортежи-отрезки функция
# должна возвращать в виде списка.
#
# Примечание 1. Числа в возвращаемом функцией списке должны располагаться в своем исходном порядке.

from itertools import groupby


def ranges(lst):
    grouped = groupby(lst, key=lambda x: numbers.index(x) - x)
    result = []

    for k, values in grouped:
        values = list(values)
        result.append((values[0], values[-1]))

    return result

#10.12.11
# Перестановки
# Напишите программу, которая выводит все перестановки символов строки без дубликатов.
#
# Формат входных данных
# На вход программе подается произвольная строка из строчных латинских букв, длина которой не превышает
# 10 символов.


# from itertools import permutations
#
#
# perm = permutations(input())
# perm = sorted(set(perm))
# for i in perm:
#     print(''.join(i))

### examples
# for tpl in sorted(set(permutations(input()))):
#     print(''.join(tpl))

#10.12.12
#
# Тимур пришел в книжный магазин, чтобы приобрести новую книгу по математике, стоимость которой равна
#
# 100$. У него в кошельке имеется множество купюр различного номинала, которые представлены в списке wallet.
# Например, Тимур может расплатиться одной купюрой в
#
# 100$ или двумя по
# 50$.
#
# Дополните приведенный ниже код, чтобы он вывел количество способов, которыми Тимур может приобрести книгу стоимостью
#
# 100$.
#
# Примечание. Способы расплатиться наборами купюр вида
# 50,20,20,10 и
#
# 20,10,50,20 считаются одинаковыми и не должны учитываться повторно.


from itertools import combinations
wallet = [100, 100, 50, 50, 50, 50, 20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
combs = []

#
# for i in range(1,len(wallet)+1):
#     combinations_100 = [comb for comb in combinations(wallet, i) if sum(comb) == 100]
#     for comb in combinations_100:
#         combs.append(comb)
# print(len(set(combs)))

### examples

# s = 0
# for i in range(0,21):
#     s += sum([1 for p in set(combinations(wallet, i)) if sum(p) ==100])
# print(s)


###
#
# from collections import Counter
# from itertools import product
#
# wallet = [
#     100, 100, 50, 50, 50, 50, 20, 20, 20,
#     10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1
# ]
#
# """Сводится к поиску числа комбинаций коэффициентов перед
# номиналами - таких, что сумма произведений дает 100."""
# wallet = Counter(wallet)
# coeffs = product(*[range(val+1) for val in wallet.values()])
# matmul = (sum(qual * qty for qual, qty
#               in zip(wallet.keys(), comb)) for comb in coeffs)
# print(sum(1 for val in matmul if val == 100))

###

# res = set()
# for i in range(1, len(wallet)):
#     res.update(x for x in it.combinations(wallet, i) if sum(x) == 100)
# print(len(res))


#10.12.13

# Тимур пришел в книжный магазин, чтобы приобрести новую книгу по математике, стоимость которой равна
#
# 100$. У него в кошельке имеется неограниченное количество купюр, номиналы которых представлены в списке wallet. Другими словами, Тимур может использовать купюру одного номинала произвольное количество раз. Например, он может расплатиться пятью купюрами по
#
# 20$ или десятью по
#
# 10$.
#
# Дополните приведенный ниже код, чтобы он вывел количество способов, которыми Тимур может приобрести книгу стоимостью
#
# 100$.
#
# Примечание. Способы расплатиться наборами купюр вида
#
# 50,20,20,10 и
#
# 20,10,50,20 считаются одинаковыми и не должны учитываться повторно.


# from itertools import combinations_with_replacement
#
# wallet = [100, 50, 20, 10, 5]
# res = set()
# for i in range(21):
#     res.update(x for x in combinations_with_replacement(wallet, i) if sum(x) == 100)
# print(len(res))


### examples

# def gen_100():  # быстрее, чем combinations_with_replacement
#     for x1 in range(0, 101, 100):
#         for x2 in range(0, 101, 50):
#             for x3 in range(0, 101, 20):
#                 for x4 in range(0, 101, 10):
#                     for x5 in range(0, 101, 5):
#                         yield x1 + x2 + x3 + x4 + x5
#
# print(sum(1 for x in gen_100() if x == 100))


###
# from itertools import combinations_with_replacement as cmb_wr
#
# wallet = [100, 50, 20, 10, 5]
#
# res = set()
# for r in range(4, 21):
#     for tup in cmb_wr(wallet, r=r):
#         if sum(tup) == 100:
#             res.add(tup)
# print(len(res) + 2)

###
# wallet = [100, 50, 20, 10, 5]
# SUM = 100
# def dinamic(n, stor):
#     parts = [1] + [0] * n
#     for c in stor:
#         for i, x in enumerate(range(c, n + 1)):
#             parts[x] += parts[i]
#     return parts[n]
# print(dinamic(SUM, wallet))


#10.12.14
# # Задача о рюкзаке
# # Вам доступен список items, содержащий набор предметов. Каждый предмет представлен в виде именованного кортежа и имеет три параметра — название, массу (в граммах) и ценность (в рублях). Также имеется рюкзак определённой грузоподъёмности.
# #
# # Напишите программу, которая определяет, какие предметы из представленного набора следует взять, чтобы собрать рюкзак с максимальной ценностью предметов внутри, соблюдая при этом весовое ограничение рюкзака.
# #
# # Формат входных данных
# # На вход программе в первой строке подается число — грузоподъемность рюкзака (в граммах).
# #
# # Формат выходных данных
# # Программа должна определить какие предметы из представленного набора следует взять, чтобы собрать рюкзак с максимальной ценностью предметов внутри, соблюдая при этом весовое ограничение рюкзака, и вывести названия полученных предметов в лексикографическом порядке, каждое на отдельной строке. Если рюкзак не позволяет взять ни один предмет, программа должна вывести текст:
# #
# # Рюкзак собрать не удастся
# # Примечание 1. Рюкзак не обязательно должен быть наполнен полностью.
# Примечание 2. Подробнее с задачей о рюкзаке можно ознакомиться по ссылке. https://ru.wikipedia.org/wiki/Задача_о_рюкзаке

from collections import namedtuple
import itertools as it

Item = namedtuple('Item', ['name', 'mass', 'price'])

items = [Item('Обручальное кольцо', 7, 49_000),
         Item('Мобильный телефон', 200, 110_000),
         Item('Ноутбук', 2000, 150_000),
         Item('Ручка Паркер', 20, 37_000),
         Item('Статуэтка Оскар', 4000, 28_000),
         Item('Наушники', 150, 11_000),
         Item('Гитара', 1500, 32_000),
         Item('Золотая монета', 8, 140_000),
         Item('Фотоаппарат', 720, 79_000),
         Item('Лимитированные кроссовки', 300, 80_000)]

def rukzak(items, mass):
    max_value = 0
    selected = []
    for i in range(1,len(items)+1):
        for comb in it.combinations(items, i):
            total_weight = sum(item.mass for item in comb)
            total_value = sum(item.price for item in comb)
            if total_weight <= mass and total_value > max_value:
                max_value = total_value
                selected = list(comb)
    return selected

# mass = int(input())
# selected_items = rukzak(items, mass)
# selected_items = list(sorted(selected_items, key = lambda x: x.name))
# if selected_items:
#     for item in selected_items:
#         print(item.name)
# else:
#     print('Рюкзак собрать не удастся')

### examples
# value = int(input())

# if min(items, key=lambda x: x.mass).mass > value:
#     print('Рюкзак собрать не удастся')
# else:
#     data = chain.from_iterable(combinations(items, r=i) for i in range(1, 11))
#     data_filtered = filter(lambda x: value >= sum(i.mass for i in x), data)
#     result = max(data_filtered, key=lambda x: sum(i.price for i in x))
#     print(*sorted(i.name for i in result), sep='\n')


###
bag_weight = int(input())
bag_price = -1
bag_items = None

for i in range(1, 11):
    for comb in combinations(items, i):
        comb_price = sum(item.price for item in comb)
        comb_weight = sum(item.mass for item in comb)
        if comb_price > bag_price and comb_weight <= bag_weight:
            bag_items = comb
            bag_price = comb_price

if bag_items:
    for item in sorted(bag_items):
        print(item.name)
else:
    print('Рюкзак собрать не удастся')

# 10.12.20
# Вам доступна программа, которая выводит все обозначения полей шахматной доски в алфавитном порядке через пробел.

# Перепишите данную программу с использованием функции product(), чтобы она выполняла ту же задачу.


# from string import ascii_lowercase
# from itertools import product

# letters = ascii_lowercase[:8]
# digits = [1, 2, 3, 4, 5, 6, 7, 8]


# #for letter in letters:
# #    for digit in digits:
# #        print(letter, digit, sep='', end=' ')

# board = (f'{i[0]}{i[1]}' for i in product(letters, digits))
# print(*list(board))


# ### examples
# for card in product(letters, digits):
#     print(*card, sep='', end=' ')

# ###
# print(*(f"{letter}{digit}" for letter, digit in product(letters, digits)), sep=' ')

# 10.12.21
# Функция password_gen()
# Вам доступна функция password_gen(), которая возвращает генератор, порождающий все трехсимвольные строковые пароли в порядке возрастания, составленные из цифр от 
# 0 до 9 включительно.
# Перепишите данную функцию с использованием функции product(), чтобы она выполняла ту же задачу.

#task
def password_gen():
    for i in range(10):
        for j in range(10):
            for k in range(10):
                yield str(i) + str(j) + str(k)

# solution
from itertools import product                
def password_gen():
    yield from (f'{i[0]}{i[1]}{i[2]}' for i in product(range(10), repeat=3))


### examples
def password_gen():
    for i, j, k in product(range(10), repeat=3):
        yield f'{i}{j}{k}'
 ###
def password_gen():
    for i in product(range(10),repeat = 3):
        yield ''.join(map(str,i))

#10.12.22
# напишите программу, которая генерирует в системе счисления 
# n все числа длины m.

# Формат входных данных
# На вход программе в первой строке подается натуральное число n≤16 — основание системы счисления, а затем натуральное число m — длина генерируемых чисел.

# Формат выходных данных
# Программа должна сгенерировать в системе счисления n все числа длины m и вывести их в порядке возрастания через пробел.
from itertools import product

n,m = int(input()), int(input())
yo = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

all_combinations = product(yo[:n], repeat=m)

for combination in all_combinations:
    print(''.join(combination), end=' ')
