# 16 Задайте список из n чисел последовательности (1+ 1/n)**n и выведите на экран их сумму.

while True:
    num = input('Введите целое положительное число: ')
    try:
        num = int(num)
        if num > 0:
            break
        else: print('Число отрицательное!')
    except ValueError:
        print('Ошибка. Ожидалось целое положительное число.')

my_list = []
for i in range(1, num + 1):
    elem = round(((1 + 1/i)**i), 2)
    my_list.append(elem)
myDict = {i+1: my_list[i] for i in range(0, len(my_list))}
print(myDict)
print(f'Сумма последовательности равна: {sum(my_list)}')