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

