# shop_list = ['Картофель', 'Горошек', 'Рис', 'Хлеб']
# shop_list.insert(shop_list.index('Рис'),  'Рыба')


# print('Список после:', shop_list)

# fruits = ['Яблоко', 'Апельсин', 'Клубника']
# # shop_list.append(fruits)
# print( shop_list)
# print(len(shop_list))

# shop_list.extend(fruits)
# print( shop_list)
# print(len(shop_list)),

# # print(shop_list.pop(0))
# print( shop_list)

# shop_list.remove('Картофель')
# print( shop_list)


# search = 'Хлеб'
# # print('Номер {} в списке - {}'.format(search,shop_list.index(search)+1))
# print(f'Номер {search} в списке - {shop_list.index(search)+1}')


# population = [  
#     ['hрл', 5],
#     ['kgk', 4555]
#     ]


# print(population[0][0], population[0][1])

# archive = (1, 2, 3)
# archive
# print(population[0][0][0], population[0][1]) 

# rainbow = ['red', 'green', 'blue']
# colors = rainbow


# colors.append('violet')
# print(colors)
# print(rainbow)


# print(id(rainbow))
# print(id(rainbow) == id(colors))

# new_archive = archive

# new_archive = new_archive + (4, 5)

# print(archive, new_archive)
# print(id(archive) == id(new_archive))

# x = 5
# print(x > 0 or x == 4)


# print('Здравствуйте!')
# room_prices = [41, 94, 100, 7, 21, 92, 62, 49, 37, 17, ]
# i = 0

# while i < len(room_prices):
#     price = room_prices[i]
#     print('Проверяем ', price)
#     i += 1
#     if price == min(room_prices):
#         print('Найдена минимальная цена')


# rainbow = ['red', 'green', 'blue', 'violet']
# for i in enumerate(rainbow):
#     print(i)


# list = []
# list.append(1)
# print('djgk',list)

# population = [
#     ['Санкт-Петербург', 7e+6], 
#     ['Красноярск', 1.2e+6],
#     ['Киров', 0.5e+6]
#     ]
# print(f"Население города {population[1][0]} - {population[1][1]} человек")

# total_sum = population[0][1] + population[1][1] + population[2][1]
# print(total_sum)
# population = [
#     ['Санкт-Петербург', 7e+6], 
#     ['Красноярск', 1.2e+6], 
#     ['Киров', 0.5e+6]
#     ]


# total_sum = 0
# for i in population:
#     total_sum += i[1]
# print(total_sum)


# population = {
#     'Санкт-Петербург': 7e+6, 
#     'Красноярск': 1.2e+6, 
#     'Киров': 0.5e+6,
#     }

# print(population['Красноярск'])

# from pprint import pprint
# pprint(dir(population))


# for i in population.values():
#     print(i)

# employees = {'Alice' : 100000,
#     'Bob' : 99817,
#     'Carol' : 122908,
#     'Frank' : 88123,
#     'Eve' : 93121}
# top_managers = sum([employees[n] for n in employees if employees[n]>=100000])
# print(top_managers)
# # total_sum = sum([s for s in employees.values() if s>=100000])
# # print(total_sum)

# my_favorite_songs = [
#     ['Waste a Moment', 3.03],
#     ['New Salvation', 4.02],
#     ['Staying\' Alive', 3.40],
#     ['Out of Touch', 3.03],
#     ['A Sorta Fairytale', 5.28],
#     ['Easy', 4.15],
#     ['Beautiful Day', 4.04],
#     ['Nowhere to Run', 2.58],
#     ['In This World', 4.02],
# ]

# import random
# import datetime
# time = 0
# i = 0
# while i < 3:
#     x = random.choice(my_favorite_songs)
#     i += 1
#     print(x)
#     time += x[1]*60
# time = int(time//60)

# print(f'Три песни звучат {time} минут')

# import random
# import datetime
# from datetime import timedelta
# # from datetime import datetime
# time = 0
# i = 0
# # h = timedelta(hours=0)
# # h = []
# # while i < 3:
# #     x = random.choice(my_favorite_songs)
# #     i += 1
# #     print(x)
# #     # time += x[1]*60
# #     date_string = str(x[1])
# #     print(date_string)
# #     date_obj = datetime.datetime.strptime(date_string, '%M.%S')
# #     print(date_obj)
# #     # d = datetime.time.strftime(20:00:00 '%M.%S')
# #     # print(d)
# #     # h.append(date_obj ) 
# #     # s = timedelta(date_obj)
# #     # print(s)
# #     # print(h)
# #     from datetime import timedelta
# # from datetime import datetime

# # import random
# # data =[]
# # data.append(randint(1,99))
# # print(data)

# def remove_exclamation_marks(s):
#     print(s.find('!'))
#     while s.find('!') != -1:
#         ns = ''
#         for j in range(0, len(s)):
#             # string = ''
#             print(j)
#             if j != s.find('!'):  
#                 ns = ns+ s[j]
#                 # print(ns)
#         s=ns
#     # print(s)    
#     return s 
        
# string = 'hhh!!!'
# print('Исправленный текст: ', remove_exclamation_marks(string))

class Bucket:
    """Хранилище объектов для статического сайта."""

    # конструктор __init__ - создает экземпляр класса
    def __init__(self, tutorial=None):
        self.content = []
        if tutorial != None:
            self.content.append(tutorial)


    def __str__(self) -> str:
        """Возвращает содержимое бакета"""
        return "Содержимое: " + ", ".join(self.content)
    

    def __bool__(self) -> bool:
        return self.content != []


    def add(self, obj):
        """Поместить объект в хранилище"""
        print('Добавлен,', obj)
        self.content.append(obj)

    
# создадим экземпляр - вебсайт
website = Bucket()
# website = Bucket('README.md')
website.add('index.html')
print(website) 