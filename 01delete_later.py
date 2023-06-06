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


rainbow = ['red', 'green', 'blue', 'violet']
for i in enumerate(rainbow):
    print(i)
