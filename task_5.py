# Реализуйте алгоритм перемешивания списка.

from random import randint


num = int(input('Введите размерность списка, n: '))
list = []
for i in range(num):
    list.append(i)
print(list)

def mixing_list(list):
    for i in range(len(list)):
        temp = list[i]
        k = randint(0, len(list)-1)
        list[i] = list[k]
        list[k] = temp
    return list

print(mixing_list(list))