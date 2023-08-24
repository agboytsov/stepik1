
# 10.5.15
# Реализуйте генераторную функцию simple_sequence(), которая не принимает никаких аргументов.

# Функция должна возвращать генератор, порождающий бесконечную возрастающую последовательность натуральных чисел, в которой каждое число встречается столько раз, каково оно:

# 1,2,2,3,3,3,4,4,4,4,..
def simple_sequence():
    start = 1
    while True:
        for i in range(start):
            yield start
        start += 1


# 10.5.16
# Реализуйте генераторную функцию alternating_sequence(), которая принимает один аргумент:
#
# count — натуральное число, по умолчанию имеет значение None
# Если count имеет значение None, функция должна возвращать генератор, порождающий бесконечный знакочередующийся ряд натуральных чисел.
#
# Если count имеет в качестве значения натуральное число, функция должна возвращать генератор, порождающий первые count чисел знакочередующегося ряда натуральных чисел, а затем возбуждающий исключение StopIteration.
#
# Примечание 1. Знакочередующийся ряд натуральных чисел имеет вид:

# 1,−2,3,−4,5,−6,7,−8,9,−10,...

def alternating_sequence(count=0):
    number = 1
    while True:
        yield number * (1, -1)[number%2 ==0]
        number += 1
        if count+1 == number:
            return


# 10.5.17
# Реализуйте генераторную функцию primes(), которая принимает два аргумента в следующем порядке:
#
# left — натуральное число
# right — натуральное число
# Функция должна возвращать генератор, порождающий последовательность простых чисел от left до right включительно, а затем возбуждающий исключение StopIteration.
#
# Примечание 1. Гарантируется, что left <= right.
#
# Примечание 2. Простое число — натуральное число, имеющее ровно два различных натуральных делителя — единицу и самого себя. Единица простым числом не является.

def primes(left, right):
    def is_prime(x):
        if x == 1:
            return False
        for i in range(2, (x//2)+1):
            if x % i == 0:
                return False
        return True

    for num in range(left, right + 1):
        if is_prime(num):
            yield num

### examples

def primes(left, right):
    left = left if left != 1 else 2
    for n in range(left, right+1):
        if not any(n % i == 0 for i in range(2, n)):
            yield n


#10.5.18

# Реализуйте генераторную функцию reverse(), которая принимает один аргумент:
#
# sequence — последовательность
# Функция должна возвращать генератор, порождающий элементы последовательности sequence в обратном порядке, а затем возбуждающий исключение StopIteration.
#
# Примечание 1. Последовательностью является коллекция, поддерживающая индексацию и имеющая длину. Например, объекты типа list, str, tuple являются последовательностями.

def reverse(seq):
    for i in range(1, len(seq) + 1):
        yield seq[-i]

#10.5.19

# Реализуйте генераторную функцию dates(), которая принимает два аргумента в следующем порядке:
#
# start — дата, тип date
# count — натуральное число, по умолчанию имеет значение None
# Если count имеет значение None, функция должна возвращать генератор, порождающий последовательность из максимально допустимого количества дат (тип date), начиная с даты start.
#
# Если count имеет в качестве значения натуральное число, функция должна возвращать генератор, порождающий последовательность из count дат (тип date), начиная с даты start, а затем возбуждающий исключение StopIteration.

from datetime import date, timedelta

def dates(start, count=None):
    days = 0
    while True:
        try:
            yield start + timedelta(days=days)
            days += 1
            if count == days:
                return
        except OverflowError:
            return


### examples

from datetime import date, timedelta


def dates(start, count=None):
    count = count or (date.max - start).days + 1
    for i in range(count):
        yield start + timedelta(days=i)

###
from datetime import date, timedelta

def dates(start, count=None):
    if count is None:
        count = (date.max - start).days + 1
    yield from (start + timedelta(days=day) for day in range(count))






