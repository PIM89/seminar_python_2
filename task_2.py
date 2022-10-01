#   15. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#   Пример:
#   пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

while True:
    num = input('Введите целое положительное число: ')
    try:
        num = int(num)
        if num > 0:
            break
    except ValueError:
        print('Ошибка. Ожидалось целое положительное число.')

numbers = []
i = 1
k = 1
while k <= num:
    i = i*k
    k += 1
    numbers.append(i)
print(numbers)
