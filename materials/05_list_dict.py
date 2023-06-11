# Задача 2

# Создайте список списков населения перечисленных городов
# Количество элементов в списке "города" не меньше 3!

# Выведите на консоль население второго города в списке в формате
# Население Москвы - ХХ человек

# Выведите на консоль общий размер населения перечисленных городов как сумму населения всех городов
# Итого размер населения - ХХ человек

# population = [
#     ['Санкт-Петербург', 7e+6], 
#     ['Красноярск', 1.2e+6], 
#     ['Киров', 0.5e+6]
#     ]

# print(f"Население города {population[1][0]} - {population[1][1]} человек")

# # Вариант 1
# total_sum = population[0][1] + population[1][1] + population[2][1]

# # Вариант 2
# total_sum = 0
# for i in population:
#     total_sum += i[1]

# print(f"Итого размер населения - {total_sum} человек")

# # Вариант 3
# total_sum = 0
# for city, people in population:
#     print(f"Население города {city} - {people} человек")
#     total_sum += people

# print(f"Итого размер населения - {total_sum} человек")



# Словарь dict - пары ключ:значение
dct = {}
lst = []
tpl = ()

capitals = {}
capitals['Россия'] = 'Москва'
# print(capitals)  # {'Россия': 'Москва'}
capitals['Италия'] = 'Рим'

population = {
    'Санкт-Петербург': 7e+6, 
    'Красноярск': 1.2e+6, 
    'Киров': 0.5e+6,
    }

# print(population['Красноярск'])

# from pprint import pprint
# pprint(dir(population))

# for i in population.values():
    # print(i)

# for city, people in population.items():
#     print(city, people)

# Пример словаяр - git
# commit 215744323136234727623532
# Добавил дз

# commit 2915219759215125215215
# Добавил page 01

# {
#     '215744323136234727623532' : 'Добавил дз',
#     '2915219759215125215215' : 'Добавил page 01'
#     }


# Задача 3

# Поиск самых высокооплачиваемых работников с помощью спискового включения

# нужно найти всех сотрудников, 
# зарабатывающих по крайней мере 100 000 долларов в год

employees = {'Alice' : 100000,
    'Bob' : 99817,
    'Carol' : 122908,
    'Frank' : 88123,
    'Eve' : 93121}

# Вариант 1 - классический вариант
top_managers = []

for name in employees:
    if employees[name] >= 100000:
        top_managers.append(name)

print(top_managers)  # ['Alice', 'Carol']

# Вариант 2 - однострочники

top_managers = [n for n in employees if employees[n]>=100000]
print(top_managers)

total_sum = sum([s for s in employees.values() if s>=100000])
print(total_sum)

# # Лаконичная запись условия if
# x = 4
# if x >= 0:
#     print('Больше либо равен нулю')
# else:
#     print('Меньше нуля')

# result = 'Больше либо равен нулю' if x >= 0 else 'Меньше нуля'
# print(result)

# # Лаконичная запись цикла for
# lst = [1, 2, 3]

# for i in lst:
#     print(i**2)

# result = [i**2 for i in lst]  # списковое включение
# print(result)

