# Python урок 2
# TODO - list and tuple
# TODO - условный оператор if
# TODO -  операторы цикла for и while
# TODO -  лаконичная запись цикла

# Типы данных
x = 1 # числа
word = 'Hello'  # строки 

# Изменяемый массив
shop_list = ['Картошка', 'Капуста', 'Морковь']  # список

print(type(x), type(word), type(shop_list))


# Узнаем список методов
from pprint import pprint
pprint(dir(shop_list))

# Задача 1
# Приведем список покупок в магазине

shop_list = ['Картофель', 'Горошек', 'Рис', 'Хлеб']

# Измените список согласно пунктам задания
# Выведите результат каждого пункта на консоль по очереди

#   а. Вставьте рыбу между горошком и рисом

# # Узнаем список методов
# from pprint import pprint
# pprint(dir(shop_list))

# print(shop_list.insert(shop_list.index('Рис'),  'Рыба')) -- None 
# метод insert только добавляет элемент в массив, но ничего не возвращает
# метод insert  добавляет элемент по индексу

print('пункт а')
print('Список до:', shop_list)

shop_list.insert(shop_list.index('Рис'), 'Рыба')

print('Список после:', shop_list)

#   b. Добавьте фрукты из списка fruits в конец списка shop_list

fruits = ['Яблоко', 'Апельсин', 'Клубника']
# append добавляет элементы с конца

# shop_list.append(fruits)
# print(len(shop_list))  # ['Картофель', 'Горошек', 'Рыба', 'Рис', 'Хлеб', ['Яблоко', 'Апельсин', 'Клубника']]
# элементов насчитал 6 -- добавляется массив в виде одного элемента

# extend расширяет наш список другими списками с конца
shop_list.extend(fruits)
print('пункт b', shop_list, len(shop_list)) # ['Картофель', 'Горошек', 'Рыба', 'Рис', 'Хлеб', 'Яблоко', 'Апельсин', 'Клубника']
# 8

#   c. Удалите из списка shop_list картофель

# print(shop_list.pop(0)) -- картофель -- вытаскивает элемент из массива, из массива он удаляется
# print(shop_list)

shop_list.remove('Картофель')
print('пункт c', shop_list, len(shop_list))  # ['Горошек', 'Рыба', 'Рис', 'Хлеб', 'Яблоко', 'Апельсин', 'Клубника']

#   d. Какими по счету стоят хлеб и апельсин? Выведите номера на консоль в формате
#   Номер "продукта" в списке - N 

# Формирование строк в Python
search = 'Хлеб'
# Вариант 1 - Передавать в качестве параметров списка
print('Номер', search, 'в списке -', shop_list.index(search) + 1)

print('Номер ' + search + ' в списке - ' + str(shop_list.index(search) + 1))

# Вариант 2 - форматирование строки
print('Номер {} в списке - {}'.format(search, shop_list.index(search) + 1))
# Проблема!
# url = 'https://www.ranepa.ru/my_profile/functions={}/{}/{}/{}'.format(????) --слишком легко ошибиться

# Вариант 3 - f-строки
print(f'Номер {search} в списке - {shop_list.index(search) + 1}')




