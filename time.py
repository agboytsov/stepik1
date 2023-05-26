from math import factorial  # функция из модуля math
import time


def factorial_recurrent(n):  # рекурсивная функция
    if n == 0:
        return 1
    return n * factorial_recurrent(n - 1)


def factorial_classic(n):  # итеративная функция
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


n = 900


def get_the_fastest_func(flst, arg):
    import time
    times = []
    for i in flst:
        start = time.perf_counter_ns()
        i(arg)
        end = time.perf_counter_ns() - start
        times.append((end, i))
    res = min(times)
    return res[1]


def for_and_append():  # с использованием цикла for и метода append()
    iterations = 10_000_000
    result = []
    for i in range(iterations):
        result.append(i + 1)
    return result


def list_comprehension():  # с использованием списочного выражения
    iterations = 10_000_000
    return [i + 1 for i in range(iterations)]


def for_and_append(iterable):  # с использованием цикла for и метода append()
    result = []
    for elem in iterable:
        result.append(elem)
    return result


def list_comprehension(iterable):  # с использованием списочного выражения
    return [elem for elem in iterable]


def list_function(iterable):  # с использованием встроенной функции list()
    return list(iterable)

print(get_the_fastest_func([for_and_append, list_comprehension]))
0