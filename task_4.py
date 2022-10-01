# Задайте число N, создайте список: [-N, N]. Найдите произведение элементов на
# указанных позициях. Позиции (случайные) хранятся в файле file.txt (создаётся во
# время выполнения кода и зависит от количества элементов в списке) в одной
# строке одно число.

from random import randint

while True:
    num = input('Введите целое положительное число: ')
    try:
        num = int(num)
        if num > 0:
            break
    except ValueError:
        print('Ожидалось целое положительное число.')
        
list = []
for i in range(-num, num + 1):
    list.append(i)
print(list)

with open('text.txt', 'w') as file:
    i = 0
    while i < num:
        file.write(f'{randint(-num, num)}\n')
        i += 1

with open('text.txt', 'r') as file:
    lines = file.read().splitlines()
    multiply = 1
    for i in range(num):
        multiply *= list[int(lines[i])]
        print(list[int(lines[i])], end= ' ')

print(f'\nПроизведение равно: {multiply}')
