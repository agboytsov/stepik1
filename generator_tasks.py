
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

# 10.5.21
# Функция card_deck()
# Реализуйте генераторную функцию card_deck(), которая принимает один аргумент:
#
# suit — одна из четырех карточных мастей: пик, треф, бубен, червей
# Функция должна возвращать генератор, циклично порождающий колоду игральных карт без масти suit. Каждая карта должна представлять собой строку в следующем формате:
#
# <номинал> <масть>
# Например, 7 пик, валет треф, дама бубен, король червей, туз пик.
#
# Примечание 1. Карты, генерируемые итератором, должны располагаться сначала по величине номинала, затем масти.
#
# Примечание 2. Старшинство мастей по возрастанию: пики, трефы, бубны, червы. Старшинство карт в масти по возрастанию: двойка, тройка, четверка, пятерка, шестерка, семерка, восьмерка, девятка, десятка, валет, дама, король, туз.
#
# Примечание 3. Масти не требуют склонения и независимо от номинала должны сохранять следующее написание: пик, треф, бубен, червей.


def card_deck(suit):
    count = 0
    suits_count = 0
    card_values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
    card_suits = [s for s in ["пик", "треф", "бубен", "червей"] if s != suit]

    while True:
        yield f"{card_values[count % 13]} {card_suits[suits_count // 13]}"

        suits_count += 1
        count += 1

        if count % 13 > 12:
            count = 0

        if suits_count // 13 > 2:
            suits_count = 0


### examples

def card_deck(suit: str):
    suits = ['пик', 'треф', 'бубен', 'червей']
    face_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
    suits.remove(suit)
    while True:
        for suit_ in suits:
            for face_value in face_values:
                yield f'{face_value} {suit_}'


def card_deck(suit):
    return (f'{j} {i}'
            for _ in iter(lambda: 1, 0)
            for i in 'пик треф бубен червей'.split()
            for j in '2 3 4 5 6 7 8 9 10 валет дама король туз'.split()
            if i != suit)


# 10.6.15

# Вам доступна генераторная функция cubes_of_odds(), принимающая в качестве аргумента итерируемый объект, элементами которого являются целые числа, и возвращающая генератор, порождающий последовательность нечетных чисел переданного итерируемого объекта, возведенных в третью степень.

# Перепишите данную функцию с использованием генераторного выражения, чтобы она выполняла ту же задачу.

# Примечание 1. Если генераторное выражение становится достаточно большим, его можно записать в виде нескольких строк.

def cubes_of_odds(iterable):
    for number in iterable:
        if number % 2:
            yield number ** 3
            
def cubes_of_odds(iterable):
    return (number ** 3 for number in iterable if number % 2)


# 10.6.16
# # Реализуйте функцию is_prime() с использованием генераторных выражений, которая принимает один аргумент:

# # number — натуральное число
# # Функция должна возвращать True, если число number является простым, или False в противном случае.

# Примечание 1. Простое число — натуральное число, имеющее ровно два различных натуральных делителя — единицу и самого себя.

# Примечание 2. В задаче удобно воспользоваться функциями all() или any(). 

def is_prime(num):
    return sum(i for i in range(1,num+1) if num % i == 0) == num + 1

# 10.6.17
# Реализуйте функцию count_iterable() с использованием генераторных выражений, которая принимает один аргумент:

# iterable — итерируемый объект
# Функция должна возвращать единственное число — количество элементов итерируемого объекта iterable.

# Примечание 1. Гарантируется, что передаваемый в функцию итерируемый объект является конечным.

def count_iterable(it):
    return sum(1 for _ in it)

#10.6.18

# Реализуйте функцию all_together() с использованием генераторных выражений, которая принимает произвольное количество позиционных аргументов, каждый из которых является итерируемым объектом.

# Функция должна возвращать генератор, порождающий каждый элемент всех переданных итерируемых объектов: сначала все элементы первого итерируемого объекта, затем второго, и так далее.

# Примечание 1. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

def all_together(*args):
    #for arg in args:
     #   for i in arg:
      #      yield i
    return (i for arg in args for i in arg)

# 10.6.19
# 
# Реализуйте функцию interleave() с использованием генераторных выражений, которая принимает произвольное количество позиционных аргументов, каждый из которых является последовательностью.

# Функция должна возвращать генератор, порождающий каждый элемент всех переданных последовательностей: сначала первый элемент первой последовательности, затем первый элемент второй последовательности, и так далее; после второй элемент первой последовательности, затем второй элемент второй последовательности, и так далее.

# Примечание 1. Последовательностью является коллекция, поддерживающая индексацию и имеющая длину. Например, объекты типа list, str, tuple являются последовательностями.

# Примечание 2. Гарантируется, что все последовательности, передаваемые в функцию, имеют равные длины.

# Примечание 3. Гарантируется, что в функцию всегда подается хотя бы одна последовательность.

def interleave(*args):
    res = zip(*args)
    return (i for r in res for i in r)

#10.7.5
# Вам доступен именованный кортеж Person, который содержит данные о человеке. Первым элементом именованного кортежа является имя и фамилия человека, вторым — национальность, третьим — пол, четвертым — год рождения, пятым — год смерти. Если человек жив, год смерти считается равным 
# 0
# 0. Также доступен список persons, содержащий эти кортежи.

# Дополните приведенный ниже код с использованием конвейеров генераторов, чтобы он вывел имя и фамилию самого молодого живого мужчины (male) из Швеции (Swedish).

# Примечание 1. Пример вывода:

# Goran Aslin
# Примечание 2. Гарантируется, что искомый человек единственный.

from collections import namedtuple

Person = namedtuple('Person', ['name', 'nationality', 'sex', 'birth', 'death'])

persons = [Person('E. M. Ashe', 'American', 'male', 1867, 1941),
           Person('Goran Aslin', 'Swedish', 'male', 1980, 0),
           Person('Erik Gunnar Asplund', 'Swedish', 'male', 1885, 1940),
           Person('Genevieve Asse', 'French', 'female', 1949, 0),
           Person('Irene Adler', 'Swedish', 'female', 2005, 0),
           Person('Sergio Asti', 'Italian', 'male', 1926, 0),
           Person('Olof Backman', 'Swedish', 'male', 1999, 0),
           Person('Alyson Hannigan', 'Swedish', 'female', 1940, 1987),
           Person('Dana Atchley', 'American', 'female', 1941, 2000),
           Person('Monika Andersson', 'Swedish', 'female', 1957, 0),
           Person('Shura_Stone', 'Russian', 'male', 2000, 0),
           Person('Jon Bale', 'Swedish', 'male', 2000, 0)]

alive = (i for i in persons if i.death == 0)
male = (i for i in alive if i.sex == 'male')
swedish = (i for i in male if i.nationality == 'Swedish')

#print(max(swedish, key=lambda x: x.birth).name)


# 10.6.6.

# Назовем диапазоном запись двух натуральных чисел через дефис a-b, где a — левая граница диапазона, b — правая граница диапазона, причем a <= b. Диапазон содержит в себе все числа от a до b включительно. Например, диапазон 1-4 содержит числа 

# 1, 2, 3 и 4.

# Реализуйте генераторную функцию parse_ranges(), которая принимает один аргумент:

# ranges — строка, в которой через запятую указаны диапазоны чисел
# Функция должна возвращать генератор, порождающий последовательность чисел, содержащихся в диапазонах ranges.

def parse_ranges(string):
    pairs = (i for i in string.split(','))
    for i in pairs:
        a, b = (int(x) for x in i.split('-'))
        yield from range(a, b+1)


# 10.6.7
# Реализуйте генераторную функцию filter_names(), которая принимает три аргумента в следующем порядке:

# names — список имен
# ignore_char — одиночный символ
# max_names — натуральное число
# Функция должна возвращать генератор, порождающий max_names имён из списка names, игнорируя имена, которые

# начинаются на ignore_char (в любом регистре)
# содержат хотя бы одну цифру
# Если max_names больше количества имен в списке names, то генератор должен породить все возможные имена из данного списка. 

# Примечание 1. Имена в возвращаемом функцией генераторе должны располагаться в своем исходном порядке.        


def filter_names(names: list, char: str, max_names: int):
    counter = 0
    for i in names:
        if not i.startswith(char.upper()) and i.isalpha():
            yield i
            counter += 1
        if counter == max_names:
            break

### examples
def filter_names(names, ignore_char, max_names):
    ignore_char = ignore_char.lower()
    filtred_char = (name for name in names if not name.lower().startswith(ignore_char))
    filtred_dig = (name for name in filtred_char if name.isalpha())
    return (name for idx, name in enumerate(filtred_dig) if idx < max_names)


def filter_names(names, ignore_char, max_names):
    f1 = (i for i in names if not i.lower().startswith(ignore_char.lower()) )
    f2 = (i for i in f1 if not any(map(str.isdigit, i)))
    f3 = (i for i in range(max_names))
    return (i[1] for i in zip(f3, f2))

#10.6.8
# 
# Вам доступен файл data.csv, который содержит информацию об инвестициях в различные стартапы. В первом столбце записано название компании (стартапа), во втором — инвестируемая сумма в долларах, в третьем — раунд инвестиции:

# company,raisedAmt,round
# LifeLock,6850000,b
# LifeLock,6000000,a
# LifeLock,25000000,c
# MyCityFaces,50000,seed
# Flypaper,3000000,a
# ...
# Напишите программу с использованием конвейеров генераторов, определяющую общую сумму, которая была инвестирована в раунде а, и выводящую полученный результат.

# Примечание 1. Разделителем в файле data.csv является запятая, при этом кавычки не используются.    


# filename = 'data/data.csv'
# with open(filename, 'r', encoding='UTF-8') as file:
#     file_lines = (line for line in file)
#     line_values = (line.rstrip().split(',') for line in file_lines)
#     file_headers = next(line_values)
#     line_dicts = (dict(zip(file_headers, data)) for data in line_values)
#     round_a = (int(line['raisedAmt']) for line in line_dicts if 'a' == line['round'])
#     print(sum(round_a))


#10.6.9

# Реализуйте генераторную функцию years_days(), которая принимает один аргумент:

# year — натуральное число
# Функция должна возвращать генератор, порождающий последовательность всех дат (тип date) в году year.

# Примечание 1. Возьмем в качестве примера 
# 2022
# 2022 год. В январе этого года 
# 31
# 31 день, в феврале — 
# 28
# 28, в марте — 
# 31
# 31, и так далее. Тогда генератор, полученный при вызове years_days(2022), должен порождать сначала все даты с 
# 1
# 1 по 
# 31
# 31 января, затем с 
# 1
# 1 по 
# 28
# 28 февраля, и так далее до 
# 31
# 31 декабря.

from datetime import date, timedelta
def years_days(year):
    start = date(year,1,1)
    max_days = date(year+1,1,1) - start
    return (start + timedelta(days=x) for x in range(0, max_days.days))

#10.6.10

# Реализуйте генераторную функцию nonempty_lines(), которая принимает один аргумент:

# file — название текстового файла, например, data.txt
# Функция должна возвращать генератор, порождающий последовательность всех непустых строк файла file с убранным символом переноса строки \n. Если строка содержит более 

# 25 символов, она заменяется многоточием ....


def nonempty_lines(file):
    with open(file, 'r', encoding='UTF-8') as f:
        lines = (line.strip() for line in f if not line.isspace())
        for line in lines:
            if len(line) <= 25:
                yield line
            else:
                yield "..."   

#10.6.11

# Вам доступен файл planets.txt, содержащий информацию о различных планетах. В первых четырех строках указаны характеристики первой планеты, после чего следует пустая строка, затем характеристики второй планеты, и так далее:

# Name = Mercury
# Diameter = 4879.4
# Mass = 3.302×10^23
# OrbitalPeriod = 0.241

# Name = Venus
# Diameter = 12103.6
# Mass = 4.869×10^24
# OrbitalPeriod = 0.615

# ...
# Реализуйте генераторную функцию txt_to_dict(), которая не принимает никаких аргументов.

# Функция должна возвращать генератор, порождающий последовательность словарей, каждый из которых содержит информацию об очередной планете из файла planets.txt, а именно ее название, диаметр, массу и орбитальный период. Например:

# {'Name': 'Mercury', 'Diameter': '4879.4', 'Mass': '3.302×10^23', 'OrbitalPeriod': '0.241'}
# Примечание 1. Указанный файл доступен по ссылке.

# Примечание 2. При открытии файла используйте явное указание кодировки UTF-8.



def txt_to_dict():
    filename = 'data/planets.txt'
    with open(filename,'r',encoding='UTF-8') as file:
        lines = (line.strip() for line in file)
        dct = {}
        for line in lines:
            if not line:
                yield dct
                dct = {}
            else:
                key, value = line.split(' = ')
                dct[key] = value
        if dct:
            yield dct



### examples
def planet_features(file):
    features = {}
    for _ in range(4):
        key, value = file.readline().strip().split(' = ')
        features[key] = value
    return features

def txt_to_dict():
    with open('planets.txt') as file:
        line = 'lets some yield'
        while line:
            yield planet_features(file)
            line = file.readline()

###
def txt_to_dict():
    with open('planets.txt', 'r', encoding='utf-8') as file:
        items = (i.split('\n') for i in file.read().split('\n\n'))
        return (dict(i.split(' = ') for i in planet) for planet in items)



# 10.7.19
#
# Реализуйте генераторную функцию, которая принимает один аргумент:
#
# iterable — итерируемый объект
# Функция должна возвращать генератор, порождающий последовательность элементов итерируемого объекта iterable без дубликатов.
#
# Примечание 1. Элементы итерируемого объекта в возвращаемом функцией генераторе должны располагаться в своем исходном порядке.
#
# Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

def unique(it):
    res = []
    for i in it:
        if i not in res:
            res.append(i)
            yield i
        else:
            continue


### examples
def unique(iterable):
    res = ({i:1 for i in iterable})
    yield from res


def unique(numbers):
    yield from (dict.fromkeys(numbers))


def unique(iterable):
    yield from {i: 0 for i in iterable}


# 10.7.20
# Функция stop_on()
# Реализуйте генераторную функцию, которая принимает два аргумента в следующем порядке:
#
# iterable — итерируемый объект
# obj — произвольный объект
# Функция должна возвращать генератор, порождающий последовательность элементов итерируемого объекта iterable до тех пор, пока не будет достигнут элемент, равный obj. Если итерируемый объект iterable не содержит ни одного элемента, равного obj, генератор должен породить все элементы iterable.
#
# Примечание 1. Элементы итерируемого объекта в возвращаемом функцией генераторе должны располагаться в своем исходном порядке.
#
# Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

def stop_on(it,obj):
    for i in it:
        if i != obj:
            yield i
        else:
            break


# 10.7.21
# Функция with_previous()
# Реализуйте генераторную функцию, которая принимает один аргумент:
#
# iterable — итерируемый объект
# Функция должна возвращать генератор, порождающий последовательность кортежей, каждый из которых содержит очередной элемент итерируемого объекта iterable, а также предшествующий ему элемент:
#
# (<очередной элемент>, <предыдущий элемент>)
# Для первого элемента предыдущим считается значение None.
#
# Примечание 1. Элементы итерируемого объекта в возвращаемом функцией генераторе должны располагаться в своем исходном порядке.
#
# Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

def with_previous(it):
    if not it:
        return
    it = iter(it)
    prev = next(it)
    yield (prev, None)
    for i in it:
        yield (i, prev)
        prev = i


### examples
def with_previous(iterable):
    prev = None
    return ((i, prev, prev := i)[:-1] for i in iterable)


def with_previous(iterable):
    prev_elem = None
    for elem in iterable:
        yield elem, prev_elem
        prev_elem = elem

# 10.7.22
# Функция pairwise()
# Реализуйте генераторную функцию, которая принимает один аргумент:
#
# iterable — итерируемый объект
# Функция должна возвращать генератор, порождающий последовательность кортежей, каждый из которых содержит очередной элемент итерируемого объекта iterable, а также следующий за ним элемент:
#
# (<очередной элемент>, <следующий элемент>)
# Для последнего элемента следующим считается значение None.
#
# Примечание 1. Элементы итерируемого объекта в возвращаемом функцией генераторе должны располагаться в своем исходном порядке.
#
# Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.


def pairwise(it):
    if not it:
        return

    it = iter(it)
    first, second = next(it), next(it,None)
    yield (first, second)
    for i in it:
        yield (second, i)
        second = i
    yield (second, None)


### examples

def pairwise(iterable):
    it = iter(iterable)
    i = next(it, None)
    while i != None:
        i, prev = next(it, None), i
        yield prev, i

def pairwise(iterable):
    it = iter(iterable)
    try:
        a = next(it)
        for i in it:
            yield (a, i)
            a = i
        yield (a, None)
    except StopIteration:
        pass



