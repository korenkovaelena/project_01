# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!

def minimum(arr):
    # for i in range(0, len(list_int)):
    i = 0
    j = i + 1
    while j <= len(list_int) - 1:
        if list_int[i] <= list_int[j]:
            j += 1
        else:
            i = j
            j += 1
    return(list_int[i])


def maximum(arr):
    i = 0
    j = i + 1
    while j <= len(list_int) - 1:
        if list_int[i] >= list_int[j]:
            j += 1
        else:
            i = j
            j += 1
    return(list_int[i])

import random
list_int = []
x = int(input('Введите длину списка: '))
print('Длина списка: ', x)
list_int = random.sample(range(0,500), x)
print('Наш список: ', list_int)

print('Минимальное число в списке = ', minimum(list_int))
print('Максимальное число в списке = ', maximum(list_int))