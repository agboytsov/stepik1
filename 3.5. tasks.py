###3.5.1
# Во время решения очередной задачи программист фиксирует время начала и окончания ее решения и добавляет полученные
# результаты в список data. Каждый результат представляет собой кортеж, первым элементом которого является время начала
# решения в виде строки в формате HH:MM, вторым элементом — время окончания решения в виде строки в том же формате.
# Дополните приведенный ниже код, чтобы он вывел общее целое количество минут, которое программист затратил на решение всех задач.
# from datetime import date, time, datetime, timedelta
#
# data = [('07:14', '08:46'),
#         ('09:01', '09:37'),
#         ('10:00', '11:43'),
#         ('12:13', '13:49'),
#         ('15:00', '15:19'),
#         ('15:58', '17:24'),
#         ('17:57', '19:21'),
#         ('19:30', '19:59')]
# #data = [(datetime.strptime(i[0],'%H:%M'),datetime.strptime(i[1],'%H:%M'),)for i in data]
# secs = [(i[1]-i[0]).total_seconds() for i in [(datetime.strptime(i[0],'%H:%M'),datetime.strptime(i[1],'%H:%M'),)for i in data]]
# print(int(sum(secs)/60))

###examples
# seconds = 0
#
# for tup in data:
#     start, end = [datetime.strptime(x, '%H:%M') for x in tup]
#     seconds += (end - start).total_seconds()
#
# print(int(seconds // 60))
#####
# print(sum(map(lambda tms: (datetime.strptime(tms[1], '%H:%M') - datetime.strptime(tms[0], '%H:%M')).seconds // 60, data)))

####
# def num_sec(data):
#     return (datetime.strptime(data[1], '%H:%M') - datetime.strptime(data[0], '%H:%M')).seconds
#
# data = [('07:14', '08:46'),
#         ('09:01', '09:37'),
#         ('10:00', '11:43'),
#         ('12:13', '13:49'),
#         ('15:00', '15:19'),
#         ('15:58', '17:24'),
#         ('17:57', '19:21'),
#         ('19:30', '19:59')]
#
# print(sum([num_sec(info) for info in data]) // 60)


##3.5.2
# Пятница, 13-е
# Число 13 считалось дьявольским издавна. Это имеет свое объяснение, и не одно: тут есть трактовки, связанные с Тайной вечерей — где были Христос и
# 12 апостолов, один из которых стал предателем. Есть поверье, что для шабаша нужны  12 ведьм и сатана. В истории число  13 в связке с пятницей стало «несчастливым» в
# 1307 году, когда король Франции Филипп Красивый отдал приказ схватить всех тамплиеров — членов рыцарского ордена крестоносцев.
# Все они были сожжены на кострах инквизиции, и произошло это в пятницу, 13 апреля.
# Докажите, что
# 13-е число месяца чаще всего приходится на пятницу. Напишите программу, которая вычисляет,
# сколько тринадцатых чисел приходится на каждый день недели в период с 01.01.0001 по 31.12.9999.
#
# Формат входных данных
# На вход программе ничего не подается.
#
# Формат выходных данных
# Программа должна вывести
# 7
# 7 чисел — количество тринадцатых чисел, которые приходятся на понедельник, вторник, среду, четверг, пятницу,
# субботу и воскресенье в период с 01.01.0001 по 31.12.9999. Числа должны быть расположены каждое на отдельной строке.
#
# from datetime import datetime
# d = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
#
# start,end = datetime.strptime('01.01.0001','%d.%m.%Y'),datetime.strptime('31.12.9999','%d.%m.%Y')
# for i in range(start.toordinal(), end.toordinal()+1):
#     if datetime.fromordinal(i).day == 13:
#         d[datetime.fromordinal(i).weekday()] += 1
#
# for i in d.keys():
#     print(d[i])
#
# #examples:
# t = time()
# d = datetime(1, 1, 1)  # минимум
# weekdays = {}  # словарь дней недели
# while d < datetime(9999, 12, 31):
#     if d.day == 13:  # если 13 число
#         weekdays[d.weekday()] = weekdays.get(d.weekday(), 0) + 1
#         if d < datetime(9999, 12, 31) - timedelta(28):  # проверка, чтобы не вылететь за максимум
#             d += timedelta(27)
#     d += timedelta(1)  # +1 день
# print(weekdays)

###
# def main2():
#     d = datetime(1, 1, 1)
#     weekdays = {}
#     dt = datetime(9999, 12, 31)
#     td_28 = timedelta(28)
#     td_27 = timedelta(27)
#     td_1 = timedelta(1)
#
#     while d < dt:
#         if d.day == 13:
#             weekdays[d.weekday()] = weekdays.get(d.weekday(), 0) + 1
#             if d < dt - td_28:
#                 d += td_27
#         d += td_1

####3.5.3
# Снова не успел
# Дан режим работы магазина:
#
# Понедельник	9:00 - 21:00
# Вторник	9:00 - 21:00
# Среда	9:00 - 21:00
# Четверг	9:00 - 21:00
# Пятница	9:00 - 21:00
# Суббота	10:00 - 18:00
# Воскресенье	10:00 - 18:00
# Напишите программу, которая принимает на вход текущие дату и время и определяет количество минут, оставшееся до закрытия магазина.
#
# Формат входных данных
# На вход программе подаются текущие дата и время в формате DD.MM.YYYY HH:MM.
#
# Формат выходных данных
# Программа должна вывести количество минут, которое осталось до закрытия магазина, или текст Магазин не работает, если он закрыт.


# from datetime import datetime, time,timedelta
#
# #понедельник = 0,  воскресенье = 6
# d = {
#         0: (time(9,0),time(21,0)),
#         1: (time(9,0),time(21,0)),
#         2: (time(9,0),time(21,0)),
#         3: (time(9,0),time(21,0)),
#         4: (time(9,0),time(21,0)),
#         5: (time(10,0),time(18,0)),
#         6: (time(10,0),time(18,0))
#     }
# #a = datetime.strptime(input(),'%d.%m.%Y %H:%M')
# a = datetime.strptime('07.11.2021 10:00','%d.%m.%Y %H:%M')
# if a.time()<d[a.weekday()][0] or a.time()>d[a.weekday()][1]:
#     print('Магазин не работает')
# else:
#     close = datetime(a.year,a.month,a.day,d[a.weekday()][1].hour,d[a.weekday()][1].minute)
#     if a == close:
#         print('Магазин не работает')
#     else:
#         print(int((close-a).total_seconds()/60))
#
#
# #### examples
# from datetime import datetime, timedelta
#
# dt = datetime.strptime(input(), '%d.%m.%Y %H:%M')
# td = timedelta(hours=dt.hour, minutes=dt.minute)
#
# if dt.weekday() < 5 and timedelta(hours=9) <= td < timedelta(hours=21):
#     print(int((timedelta(hours=21) - td).total_seconds() // 60))
# elif dt.weekday() > 4 and timedelta(hours=10) <= td < timedelta(hours=18):
#     print(int((timedelta(hours=18) - td).total_seconds() // 60))
# else:
#     print('Магазин не работает')

###
# from datetime import datetime
# date = datetime.strptime(input(), '%d.%m.%Y %H:%M')
#
# start, end = (date.replace(hour=i, minute=0) for i in ((9, 21), (10, 18))[date.weekday() > 4])
#
# if start <= date < end:
#     print((end - date).seconds // 60)
# else:
#     print('Магазин не работает')


###3.5.4
# Самое понятное условие
# Даны две даты — левая и правая границы диапазона соответственно. Напишите программу, которая из этого диапазона,
# включая границы, выводит, начиная с даты, у которой сумма дня и месяца нечетная, каждую третью дату, только если она не понедельник и не четверг.
#
# Формат входных данных
# На вход программе подаются две даты в формате DD.MM.YYYY — левая и правая границы диапазона соответственно,
# каждая на отдельной строке. Гарантируется, что первая дата не больше второй.
#
# Формат выходных данных
# Программа должна из указанного диапазона, включая концы, вывести, начиная с даты, у которой сумма дня и месяца нечетная,
# каждую третью дату, только если она не понедельник и не четверг. Даты должны быть расположены каждая на отдельной строке, в формате DD.MM.YYYY.
#
# Примечание 1. Если дат, удовлетворяющих условию, нет, программа ничего не должна выводить.
#
# Примечание 2. Рассмотрим второй тест. Левая граница диапазона 07.03.2021 не является начальной датой,
# так как имеет четную сумму дня и месяца, поэтому в качестве начальной берем следующую дату 08.03.2021.
# Дата 08.03.2021 не выводится, так как является понедельником, поэтому двигаемся к следующей дате с шагом три: 11.03.2021.
# Дата 11.03.2021 не выводится, так как является четвергом.
# from datetime import datetime
# pattern = '%d.%m.%Y'
# a, b = datetime.strptime(input(),pattern),datetime.strptime(input(),pattern)
#
# lst = [datetime.fromordinal(i) for i in range(a.toordinal(), b.toordinal()+1)]
# res =[]
# counter = 0
# for i in range(len(lst)):
#     if (lst[i].day+lst[i].month) % 2 != 0:
#         counter = i
#         break
# for i in range(counter,len(lst),3):
#     if lst[i].weekday() == 0 or lst[i].weekday() == 3:
#         continue
#     else:
#         print(lst[i].strftime(pattern))

####examples

# from datetime import datetime, timedelta
#
# pattern = '%d.%m.%Y'
# start = datetime.strptime(input(), pattern)
# end = datetime.strptime(input(), pattern)
#
# while not (start.month + start.day) % 2:
#     start += timedelta(days=1)
#
# while start <= end:
#     week = start.isoweekday()
#     if week in (2,3,5,6,7):
#         print(start.strftime(pattern))
#     start += timedelta(days=3)

###
# from datetime import datetime, date, timedelta
# pattern = '%d.%m.%Y'
# start, end = [datetime.strptime(input(), pattern) for _ in range(2)]
# while (start.day + start.month) % 2 == 0:
#     start += timedelta(days=1)
#
# while start <= end:
#     if start.weekday() not in [0, 3]:
#         print(start.strftime(pattern))
#     start += timedelta(days=3)


###3.5.5
#
# Сотрудники организации 😄
# Дан список сотрудников организации, в котором указаны их фамилии, имена и даты рождения.
# Напишите программу, которая определяет самого старшего сотрудника из данного списка.
#
# Формат входных данных
# На вход программе в первой строке подается натуральное число
# �
# n — количество сотрудников, работающих в организации. В последующих
# �
# n строках вводятся данные о каждом сотруднике: имя, фамилия и дата рождения, разделённые пробелом. Дата рождения указывается в формате DD.MM.YYYY.
#
# Формат выходных данных
# Программа должна определить самого старшего сотрудника и вывести его дату рождения, имя и фамилию, разделив пробелом. Если таких сотрудников несколько, программа должна вывести их дату рождения, а также их количество, разделив пробелом.
#
# Примечание 1. Гарантируется, что у всех сотрудников имена и фамилии различны.
#
# Примечание 2. Тестовые данные доступны по ссылкам:
# from datetime import datetime
# pattern = '%d.%m.%Y'
# n = int(input())
# employees = []
# for i in range(n):
#     name, surname, birthday = input().split()
#     birthday = datetime.strptime(birthday, pattern)
#     employees.append((name + ' ' + surname, birthday))
#
# employees= sorted(employees, key = lambda x:x[1])
# morethanone =[employees[0]]
# for i in range(1,len(employees)):
#     if employees[i][1] == employees[0][1]:\
#         morethanone.append(employees[i])
# if len(morethanone) > 1:
#     print(morethanone[0][1].strftime(pattern), len(morethanone))
# else:
#     print(morethanone[0][1].strftime(pattern),morethanone[0][0])
#
# ####examples
# from datetime import datetime, timedelta
#
# data = {}
# youngest = datetime.max
# pattern = '%d.%m.%Y'
#
# for _ in range(int(input())):
#     *name, birthday = input().split()
#     name, birthday = ' '.join(name), datetime.strptime(birthday, pattern)
#     if birthday < youngest:
#         youngest = birthday
#     data[name] = birthday
#
# oldest = [name for name, bd in data.items() if bd == youngest]
#
# if len(oldest) > 1:
#     print(youngest.strftime(pattern), len(oldest))
# else:
#     print(youngest.strftime(pattern), oldest[0])

# from datetime import datetime
#
# data = [tuple(input().rsplit(' ', 1)) for _ in range(int(input()))]
#
# oldest = min(data, key=lambda x: datetime.strptime(x[1], '%d.%m.%Y'))
#
# result = list(filter(lambda x: x[1] == oldest[1], data))
#
# if len(result) > 1:
#     print(oldest[1], len(result))
# else:
#     print(*oldest[::-1])