# Даны два массива:
# [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
# Надо вернуть их пересечение
# [1, 2, 2, 3]
# (порядок не важен)


list_1 = [5, 1, 2, 7, 3, 2]
list_2 = [1, 2, 3, 2, 0]
list_3 = []

for i in list_1:
    if i in list_3:
        continue
    for j in list_2:
        if i == j:
            list_3.append(i)

print(f'Пересечение двух списков: {list_3}')