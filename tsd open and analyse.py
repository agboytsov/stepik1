with open('dataset_3380_5 (5).txt', 'r') as f:
    # Создаем словарь для хранения суммы роста и количества учеников для каждого класса
    class_data = {i: [0, 0] for i in range(1, 12)}
    # Читаем файл построчно
    for line in f:
        # Разбиваем строку на три поля
        class_num, name, height = line.strip().split('\t')
        # Добавляем рост ученика к сумме роста для его класса
        class_data[int(class_num)][0] += int(height)
        # Увеличиваем количество учеников для данного класса
        class_data[int(class_num)][1] += 1

# Создаем файл для записи результатов
with open('result.tsv', 'w') as f:
    # Проходим по всем классам от 1 до 11
    for i in range(1, 12):
        # Если для данного класса есть данные, вычисляем средний рост и записываем его в файл
        if class_data[i][1] > 0:
            avg_height = class_data[i][0] / class_data[i][1]
            f.write(f'{i}\t{float(avg_height,)}\n')
        # Если данных для данного класса нет, записываем прочерк
        else:
            f.write(f'{i}\t-\n')