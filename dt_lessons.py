from datetime import datetime, timedelta
##
dt = datetime(2021, 11, 4, 13, 6) + timedelta(weeks=1,hours =12)

print(dt.strftime('%d.%m.%Y %H:%M:%S'))

from datetime import date, timedelta

today = date(2021, 11, 4)
birthday = date(2022, 10, 6)

days = (today - birthday).days

print(type(days))


### ПОЛЕЗНО
# Предыдущая и следующая даты
# Напишите программу, которая принимает на вход дату и выводит предыдущую и следующую даты.
#
# Формат входных данных
# На вход программе подается дата в формате DD.MM.YYYY.
#
# Формат выходных данных
# Программа должна вывести предыдущую и следующую даты относительно введенной даты, каждую на отдельной строке, в формате DD.MM.YYYY.
#
# Примечание 1. Гарантируется, что у подаваемой даты есть предыдущая и следующая даты.

# from datetime import datetime, timedelta
# dt = datetime.strptime(input(), '%d.%m.%Y')
# print((dt-timedelta(days=1)).date().strftime('%d.%m.%Y'))
# print((dt+timedelta(days=1)).date().strftime('%d.%m.%Y'))



# ########
# Количество секунд
# Напишите программу, которая принимает на вход время и выводит целое количество секунд, прошедшее с начала суток.


from datetime import datetime, timedelta
h,m,s = input().split(':')
total =  int(h)*3600 + int(m)*60 + int(s)
print(total)


#examples

# from datetime import datetime, timedelta
#
# h, m, s = map(int, input().split(':'))
#
# td = timedelta(hours=h, minutes=m, seconds=s)
#
# print(int(td.total_seconds()))


####
# from datetime import time
#
# t = time.fromisoformat(input())
# seconds = t.hour * 3600 + t.minute * 60 + t.second
# print(seconds)

####
# from datetime import date, time, timedelta, datetime
# a = datetime.strptime(input(),'%H:%M:%S')
# b = timedelta(hours = a.hour,minutes = a.minute, seconds = a.second)
# print(b.seconds)


####
# Таймер
# Часы показывают время в формате HH:MM:SS. На этих часах запустили таймер, который прозвенит через
# n секунд. Напишите программу, которое определит, какое время будет на часах, когда прозвенит таймер.

from datetime import timedelta, datetime
a = datetime.strptime(input(),'%H:%M:%S')
n = int(input())
res = a+timedelta(seconds=n)
print(res.strftime('%H:%M:%S'))
###examples
# from datetime import datetime, timedelta
#
# pattern = '%H:%M:%S'
# dt = datetime.strptime(input(), pattern) + timedelta(seconds=int(input()))
#
# print(dt.strftime(pattern))



####
# from datetime import timedelta, datetime
# print((datetime.strptime(input(), '%H:%M:%S') + timedelta(seconds=int(input()))).time())




####
# Функция num_of_sundays()
# Реализуйте функцию num_of_sundays(), которая принимает на вход один аргумент:
#
# year — натуральное число, год
# Функция должна возвращать количество воскресений в году year.
#
# Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию num_of_sundays(), но не код, вызывающий ее.
#
# Примечание 2. Тестовые данные доступны по ссылкам:

def num_of_sundays(year):
    from datetime import date, timedelta
    dt = date(year=year,month=12,day=31)

    return dt.strftime('%U')
year = 2000
print(num_of_sundays(year))

#examples
#
# def num_of_sundays(year):
#     counter, td = 0, timedelta(days=7)
#     d = date(year, 1, 1)
#     d += timedelta(days=6 - d.weekday())
#     while d.year == year:
#         d += td
#         counter += 1
#     return counter


###

# Продуктивность
# Артуру нужно подготовить
# 10 задач для нового курса "ООП на Python". Чтобы занятие не оказалось утомительным, он придумал правило:
#
# если сегодня он подготовил первую задачу, то вторую он должен подготовить через один день
# если сегодня он подготовил вторую задачу, то третью он должен подготовить через два дня
# если сегодня он подготовил третью задачу, то четвертую он должен подготовить через три дня
# и так далее
# Напишите программу, которая определяет даты, в которые Артуру нужно подготовить задачи.
#
# Формат входных данных
# На вход программе подается дата подготовки первой задачи в формате DD.MM.YYYY.
#
# Формат выходных данных
# Программа должна вывести
# 10 дат, удовлетворяющих условию задачи, каждую на отдельной строке, в формате DD.MM.YYYY.

from datetime import datetime, timedelta
pattern = '%d.%m.%Y'
dt = datetime.strptime(input(), pattern )
print(dt.strftime(pattern))
for i in range(1,10):
    dt = dt + timedelta(days=i+1)
    print(dt.strftime(pattern))


#examples
#
# from datetime import datetime, timedelta
#
# pattern = '%d.%m.%Y'
# dt = datetime.strptime(input(), pattern) - timedelta(days=1)
#
# for i in range(1, 11):
#     dt += timedelta(days=i)
#     print(dt.strftime(pattern))


# ###
# Соседние даты
# Дана последовательность дат. Напишите программу, которая создает и выводит список, элементами которого являются неотрицательные целые числа — количество дней между двумя соседними датами последовательности.
#
# Формат входных данных
# На вход программе подается последовательность дат, разделенных пробелом, в формате DD.MM.YYYY.
#
# Формат выходных данных
# Программа должна вывести список, содержащий неотрицательные целые числа, каждое из которых — количество дней между двумя соседними датами последовательности.
#
# Примечание 1. Даты в последовательности могут располагаться в произвольном порядке, то есть не гарантируется, что следующая дата больше предыдущей.
#
# Примечание 2. Если последовательность состоит из одной даты, то программа должна вывести пустой список.
#
# Примечание 3. Рассмотрим второй тест, в котором подается последовательность из пяти дат. Определим элементы результирующего списка:
#
# первый элемент —
# 1
# 1, количество дней между датами 06.10.2021 и 05.10.2021
# второй элемент —
# 3
# 3, количество дней между датами 05.10.2021 и 08.10.2021
# третий элемент —
# 1
# 1, количество дней между датами 08.10.2021 и 09.10.2021
# четвертый элемент —
# 2
# 2, количество дней между датами 09.10.2021 и 07.10.2021
from datetime import datetime,timedelta
dates = [datetime.strptime(i, '%d.%m.%Y') for i in input().split()]
res_lst = [abs(dates[i]-dates[i-1]).days for i in range(1,len(dates))]

print(res_lst)



########
#
# Функция fill_up_missing_dates()
# Реализуйте функцию fill_up_missing_dates(), которая принимает на вход один аргумент:
#
# dates — список строковых дат в формате DD.MM.YYYY
# Функция должна возвращать список, в котором содержатся все даты из списка dates, расположенные в порядке возрастания, а также все недостающие промежуточные даты.
#
# Примечание 1. Рассмотрим первый тест. Список dates содержит период с 01.11.2021 по 07.11.2021:
#
# dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']
# в котором отсутствуют даты 02.11.2021, 05.11.2021, 06.11.2021. Тогда вызов функции:
#
# fill_up_missing_dates(dates)
# должен вернуть список:
#
# ['01.11.2021', '02.11.2021', '03.11.2021', '04.11.2021', '05.11.2021', '06.11.2021', '07.11.2021']
# Примечание 2. Функция должна создавать и возвращать новый список, а не изменять переданный.
#
# Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию fill_up_missing_dates(), но не код, вызывающий ее.


def fill_up_missing_dates(dates):
    from datetime import datetime
    dates = sorted([datetime.strptime(i, '%d.%m.%Y') for i in dates])
    lst = [datetime.fromordinal(i).strftime('%d.%m.%Y') for i in range(min(dates).toordinal(), max(dates).toordinal()+1)]
    return lst

dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']

print(fill_up_missing_dates(dates))


##########Examples
#
# def fill_up_missing_dates(dates):
#     pattern = '%d.%m.%Y'
#     dates = [datetime.strptime(d, pattern) for d in dates]
#     start, end = min(dates), max(dates)
#     days = (end - start).days
#     return [(start + timedelta(days=i)).strftime(pattern) for i in range(days + 1)]
######
# from datetime import datetime, timedelta
#
# def fill_up_missing_dates(l, pat='%d.%m.%Y'):
#     l = list(map(lambda x: datetime.strptime(x, pat), l))
#     return [datetime.strftime(min(l) + timedelta(days=i), pat) for i in range((max(l) - min(l)).days + 1)]

#####
# from datetime import datetime, timedelta
# def fill_up_missing_dates(dates):
#     f = '%d.%m.%Y'
#     data = [datetime.strptime(i, f).toordinal() for i in dates]
#     return [datetime.fromordinal(d).strftime(f) for d in range(min(data), max(data)+1)]


###########################
# Реп по матеше
# Репетитор по математике проводит занятия по
# 45 минут с перерывами по
# 10 минут. Репетитор обозначает время начала рабочего дня и время окончания рабочего дня. Напишите программу, которая генерирует и выводит расписание занятий.
#
# Формат входных данных
# На вход программе в первой строке подается время начала рабочего дня в формате HH:MM. В следующей строке вводится время окончания рабочего дня в том же формате.
#
# Формат выходных данных
# Программа должна сгенерировать и вывести расписание занятий. На первой строке выводится время начала и окончания первого занятия в формате HH:MM - HH:MM, на второй строке — время начала и окончания второго занятия в том же формате, и так далее.
#
# Примечание 1. Если занятие обрывается временем окончания работы, то добавлять его в расписание не нужно.
#
# Примечание 2. Если разница между временем начала и окончания рабочего дня меньше
# 45 минут, программа ничего не должна выводить.
from datetime import datetime,timedelta
a, b = datetime.strptime(input(),'%H:%M'),datetime.strptime(input(),'%H:%M')

lesson = 45*60
rest = 10*60
lessons = []
cur_time = a

while True:
    lesson_start = cur_time
    lesson_end = lesson_start + timedelta(seconds=lesson)
    if lesson_start >= b or lesson_end > b:
        break
    else:

        lessons.append([lesson_start,lesson_end])
        cur_time = lesson_end+timedelta(seconds=rest)
for i in lessons:
    print(f"{i[0].strftime('%H:%M')} - {i[1].strftime('%H:%M')}")



###examples
#
#
# from datetime import datetime, timedelta
# f = '%H:%M'
# start, stop = (datetime.strptime(input(), f) for i in '__')
# while start <= (stop - timedelta(minutes=45)):
#     print(start.strftime(f), '-', (start + timedelta(minutes=45)).strftime(f))
#     start += timedelta(minutes=55)


####
# from datetime import *
#
# hour_begin = datetime.strptime(input(),'%H:%M') # Начало работы
# hour_end = datetime.strptime(input(),'%H:%M')   # Конец работы
# time_lesson = timedelta(minutes=45)             # Время урока
# time_recess = timedelta(minutes=10)             # Время перемены
# current = hour_begin                            # Текущее время
# while current + time_lesson <= hour_end:        # Пока не конец работы
#     print(f"{current.strftime('%H:%M')} - {(current + time_lesson).strftime('%H:%M')}") # текущее время - текущее время + время урока
#     current = current + time_lesson + time_recess   # текущее время = текущее время + время урока + время перемены


####
# from datetime import datetime, timedelta
# pattern = '%H:%M'
# start, end = [datetime.strptime(input(), pattern) for _ in range(2)]
# while start + timedelta(seconds=2700) <= end:
#     print(f'{start.strftime(pattern)} - {(start + timedelta(seconds=2700)).strftime(pattern)}')
#     start += timedelta(seconds=3300)


# from datetime import datetime, timedelta
#
# pattern = '%H:%M'
# start, end = [datetime.strptime(input(), pattern) for i in '12']
# lesson = timedelta(minutes=45)
# break_time = timedelta(minutes=10)
#
# while (start + lesson) <= end:
#     print(f'{start.strftime(pattern)} - {(start + lesson).strftime(pattern)}')
#     start = start + lesson + break_time