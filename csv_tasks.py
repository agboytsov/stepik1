
def csv_columns(filename):
    import csv
    with open(filename, 'r', encoding='UTF-8') as file:
        rows = list(csv.reader(file, delimiter=',', quotechar='"'))
    cols = tuple(i for i in rows[0])
    res = {k:[] for k in rows[0]}
    for col in cols:
        res[col] += [i[rows[0].index(col)] for i in rows[1:]]
    return res




#print(csv_columns('deniro.csv'))

#####4.2.16

# import csv
# #считываем пользователей
# with open('data.csv', 'r', encoding='UTF-8') as file:
#     rows = list(csv.DictReader(file, delimiter=',', quotechar='"'))
# res = {}
# for row in rows:
#     domain = row['email'].split('@')[1]
#     if domain in res.keys():
#         res[domain] += 1
#     else:
#         res[domain] = 1
# # сортируем пользователйе
# res = {k: v for k, v in sorted(res.items(), key = lambda x: (x[1],x[0]))}
#
# # готовим список словарей для диктрайтера
# columns = ['domain','count']
# new_lst = []
# for k,v in res.items():
#     new_lst.append({'domain':k, 'count':str(v)})
#
# # выводим csv в файл
# with open('domain_usage.csv','w',encoding='UTF-8', newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=columns)
#     writer.writeheader()
#     for row in new_lst:
#         writer.writerow(row)


#4.2.17

# import csv
#
# wifi = dict()
#
# with open('wifi.csv', encoding='utf-8') as f:
#     rows = csv.reader(f,  delimiter=';')
#     next(rows)
#     for adm_area, district, location, APnumber in rows:
#         #key = district
#         wifi[district] = wifi.get(district, 0) + int(APnumber)
#     res = {k: v for k, v in sorted(wifi.items(), key = lambda x: (-x[1],x[0]))}
# for k,v in res.items():
#     print(f'{k}: {v}')


# 4.2.18

# import csv
#
# with open('titanic.csv', encoding='utf-8') as f:
#     rows = csv.reader(f,  delimiter=';')
#     # survived;name;sex;age
#     next(rows)
#     male = {}
#     female = {}
#     for survived, name, sex, age in rows:
#         if int(survived) == 1 and float(age) < 18:
#             if sex == 'male':
#                 male[name] = age
#             else:
#                 female[name] = age
#     survived = male | female
#     print(*survived, sep='\n')


# 4.2.19
# import csv
# #format = '%d/%m/%Y %H:%M'
#
# #datetime.strptime(row[2], format)]
# with open('name_log.csv', encoding='utf-8') as f:
#     head = list(f.readline().strip('\n').split(','))
#     rows = csv.reader(f,  delimiter=',')
#     rows = sorted(list(rows),key = lambda x: (x[2]), reverse=True )
#     emails = {}
#     for username, email, dtime in rows:
#         if emails.get(email):
#             continue
#         else:
#             emails[email] = [username, email, dtime]
#
# emails = [head] + [i for i in sorted(emails.values(), key=lambda x:  (x[1]))]
# with open('new_name_log.csv', 'w',encoding='UTF-8', newline='') as out_f:
#     writer = csv.writer(out_f)
#     for row in emails:  # запись строк
#         writer.writerow(row)
#
#
# ####
# import csv
# from datetime import datetime
#
# with open('name_log.csv', encoding='UTF-8') as f:
# 	header, *rows = csv.reader(f)
#
# d = {i[1]:i for i in sorted(rows, key=lambda x: datetime.strptime(x[2], '%d/%m/%Y %H:%M'))}
#
# with open('new_name_log.csv', 'w', encoding='UTF-8', newline='') as f:
# 	w = csv.writer(f)
# 	w.writerow(header)
# 	w.writerows(sorted(d.values(), key=lambda x: x[1]))


# 4.2.20

def condense_csv(filename,id_name):
    import csv
    headers = [id_name]
    res = {}


    with open(filename, 'r',encoding='UTF-8') as f:
        rows = list(csv.reader(f))

        for i in range(len(rows)):
            id, cat, value = rows[i]

            if not res.get(id):
                res[id] = {cat:value}
            else:
                res[id] = res[id] | {cat:value}
            if cat not in headers:
                headers.append(cat)
    res = list({k:{id_name:k}|v for k, v in res.items()}.values())

    with open('condensed.csv','w',encoding='UTF-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers, delimiter=',')
        writer.writeheader()  # запись заголовков
        for row in res:  # запись строк
           writer.writerow(row)


#
#
# condense_csv('data4220.csv',id_name='ID')


#4.2.21
#
# import csv
#
# with open('student_counts.csv', encoding='utf-8') as f:
#     reader = csv.DictReader(f)
#     headers = [reader.fieldnames[0]]+ sorted(list(reader.fieldnames)[1:],key=lambda x: (int(x.split('-')[0]), x.split('-')[1]))
#     lst = list(reader)
#     res = []
#     for i in lst:
#         new_dct = {}
#         for j in headers:
#             new_dct[j] = i[j]
#         res.append(new_dct)
# with open('sorted_student_counts.csv','w',encoding='UTF-8', newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=headers, delimiter=',')
#     writer.writeheader()
#     for row in res:
#        writer.writerow(row)


#4.2.22

import csv

with open('prices.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f,delimiter =';')
    headers = list(reader.fieldnames)
    rows = list(reader)
    lowest = 9999999999999999999
    res = []

    for field in headers[1:]:
        for row in rows:
            if int(row[field]) <= lowest:
                lowest = int(row[field])
                res.append((field,row['Магазин'],lowest))
    prod, shop, *els = sorted(res,key=lambda x: (x[2],x[0]))[0]
    print(f'{prod}: {shop}')

