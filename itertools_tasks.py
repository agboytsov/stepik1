#10.8.15

# Функция tabulate()
# Реализуйте функцию tabulate(), которая принимает один аргумент:
#
# func — произвольная функция
# Функция tabulate() должна возвращать итератор, генерирующий бесконечную последовательность возвращаемых значений функции func сначала с аргументом 1, затем 2, затем 3, и так далее.

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
# Функция должна возвращать итератор, генерирующий последовательность из n чисел, каждое из которых является факториалом очередного натурального числа.


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
# Функция должна возвращать итератор, циклично генерирующий бесконечную последовательность натуральных чисел и заглавных латинских букв:

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
# Реализуйте функцию roundrobin(), которая принимает произвольное количество позиционных аргументов, каждый из которых является итерируемым объектом.
#
# Функция должна возвращать итератор, генерирующий последовательность из элементов всех переданных итерируемых объектов: сначала первый элемент первого итерируемого объекта, затем первый элемент второго итерируемого объекта, и так далее; после второй элемент первого итерируемого объекта, затем второй элемент второго итерируемого объекта, и так далее.
#
# Примечание 1. Элементы итерируемых объектов в возвращаемом функцией итераторе должны располагаться в своем исходном порядке.
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
# Функция должна возвращать итератор, генерирующий все числа итерируемого объекта iterable, начиная с первого неотрицательного числа.
#
# Примечание 1. Элементы итерируемого объекта в возвращаемом функцией итераторе должны располагаться в своем исходном порядке.
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
# Функция должна возвращать итератор, генерирующий последовательность элементов итерируемого объекта iterable, начиная с элемента, не равного obj.
#
# Примечание 1. Элементы итерируемого объекта в возвращаемом функцией итераторе должны располагаться в своем исходном порядке.
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
# Функция first_true() должна возвращать первый по счету элемент итерируемого объекта iterable, для которого функция predicate вернула значение True. Если такого элемента нет, функция first_true() должна вернуть значение None.
#
# Примечание 1. Предикат — это функция, которая возвращает True или False в зависимости от переданного в качестве аргумента значения.
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
# Примечание 1. Элементы итерируемого объекта в возвращаемом функцией итераторе должны располагаться в своем исходном порядке.
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
import itertools as it


def first_largest(iterable, number):
    return next(it.dropwhile(lambda x: x[1] <= number, enumerate(iterable)), [-1])[0]

