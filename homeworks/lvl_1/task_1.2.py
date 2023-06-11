# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]


# import random
# time = 0
# i = 0
# while i < 3:
#     x = random.choice(my_favorite_songs)
#     i += 1
#     print(x)
#     time += x[1]*60
# time = int(time//60)

# print(f'Три песни звучат {time} минут')

import random
import datetime
time = datetime.timedelta()
i = 0
while i < 3:
    x = random.choice(my_favorite_songs)
    i += 1
    # print(x)
    (m, s) = str(x[1]).split('.')
    d = datetime.timedelta(minutes=int(m), seconds=int(s))
    # print(d)
    time += d
    # print(time)
(h, min, sec) = str(time).split(':')

# print(min)

print(f'Три песни звучат {min} минут')

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
# p=[]
# # #x= [i for i in my_favorite_songs_dict.values()]
# p = list(my_favorite_songs_dict.values())
# print (p)

# # #t= sum(random.choices(p,k=3))
# t= random.choices(p,k=3)
# print (t)
# t= sum(t)
# print(f'Три песни звучат {int(t//1)} минут')

import random
import datetime
p=[]
# #x= [i for i in my_favorite_songs_dict.values()]
p = list(my_favorite_songs_dict.values())
# print (p)

# #t= sum(random.choices(p,k=3))
t= random.choices(p,k=3)
# print (t)
mysum = datetime.timedelta()
for i in t:
    (m, s) = str(i).split('.')
    d = datetime.timedelta(minutes=int(m), seconds=int(s))
    mysum += d
# print(str(mysum))
(h, min, sec) = str(mysum).split(':')
print(f'Три песни звучат {min} минут')



# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 



