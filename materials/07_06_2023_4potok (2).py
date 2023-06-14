# -*- coding: utf-8 -*-
"""07_06_2023_4potok.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qLvdS4ZnFmRVHQ_dtGHubJH9taSIDrC7
"""

print ('Буква q закроет калькулятор')
while True:
  s = input("Знак (+,-,*,/,%):")
  if s == 'q':
    break
  if s in ('+','-','*','/','%'):
    if s == '%':
      print ('x - число, от которого берем %')
      print ('y - % который берем')
    x = float(input('x = '))
    y = float(input('y = '))
    if s == '+':
      print ("%.2f" % (x + y))
    elif s == '-':
      print ("%.2f" % (x - y))
    elif s == '*':
      print ("%.2f" % (x * y))
    elif s == '%':
      print ("%.2f" % (x / 100 * y))
    elif s == '/':
      if y != 0:
        print ("%.2f" % (x / y))
      else:
        print ('Деление на 0')
  else:
    print ("Неверный знак операции")

a = 44
b = 12

while a != 0 and b != 0:
  if a > b:
    a = a % b
    print (a)
  else:
    b = b % a
    print (b)

print (a + b)

a = 35
b = 14

while a != b:
  if a > b:
    a = a - b
    print (a)
  else:
    b = b - a
    print(b)

#print (b)

from datetime import datetime
arr = [[4,6,2,1,9,63,-134,566],[-52, 56, 30, 29, -54, 0, -110],[42, 54, 65, 87, 0], [5]]

def choice(data):
  i = 0
  length = len(data)
  while i < length - 1:
    m = i
    j = i + 1
    while j < length:
      if data[j] < data[m]:
        m = j
      j += 1
    data[i], data[m] = data[m], data[i]
    i += 1
  return data

def bubble_for(data):
  for i in range(len(data)- 1):
    for j in range (len(data)-i-1):
      if data[j] > data[j+1]:
        data[j], data[j+1] = data[j+1], data[j]
  return data

def bubble_while(data):
  i = 0
  while i < len(data) - 1:
    j = 0
    while j < len(data) - 1 - i:
      if data[j] > data[j+1]:
        data[j], data[j+1] = data[j+1], data[j]
      j += 1
    i += 1
  return data

def default(data):
  data.sort()
  return data

def insertion(data):
  for i in range(len(data)):
    j = i - 1
    val = data[i]
    while data[j] > val and j >= 0:
      data[j + 1] = data[j]
      j -= 1
    data[j + 1] = val
  return data

def minimum(arr):
    print ('МИНИМАЛЬНЫЕ ЗНАЧЕНИЯ')
    print ('Метод choice')
    start_time = datetime.now()
    for data in arr:
      print ("Минимальное значение из массива: ", data, choice(data)[0])
    end_time = datetime.now()
    print ("Продолжительность: {}".format(end_time - start_time))
    print ('Метод  bubble for')
    start_time = datetime.now()
    for data in arr:
      print ("Минимальное значение из массива: ", data, bubble_for(data)[0])
    end_time = datetime.now()
    print ("Продолжительность: {}".format(end_time - start_time))
    print ('Метод  bubble while')
    start_time = datetime.now()
    for data in arr:
      print ("Минимальное значение из массива: ", data, bubble_while(data)[0])
    end_time = datetime.now()
    print ("Продолжительность: {}".format(end_time - start_time))
    print ('Метод  default')
    start_time = datetime.now()
    for data in arr:
      print ("Минимальное значение из массива: ", data, default(data)[0])
    end_time = datetime.now()
    print ("Продолжительность: {}".format(end_time - start_time))
    print ('Метод  insertion')
    start_time = datetime.now()
    for data in arr:
      print ("Минимальное значение из массива: ", data, insertion(data)[0])
    end_time = datetime.now()
    print ("Продолжительность: {}".format(end_time - start_time))

def maximum(arr):
    print ('МАКСИМАЛЬНЫЕ ЗНАЧЕНИЯ')
    print ('Метод choice')
    start_time = datetime.now()
    for data in arr:
      print ("Максимальное значение из массива: ", data, choice(data)[len(data) - 1])
    end_time = datetime.now()
    print ("Продолжительность: {}".format(end_time - start_time))
    print ('Метод  bubble for')
    start_time = datetime.now()
    for data in arr:
      print ("Максимальное значение из массива: ", data, bubble_for(data)[len(data) - 1])
    end_time = datetime.now()
    print ("Продолжительность: {}".format(end_time - start_time))
    print ('Метод  bubble while')
    start_time = datetime.now()
    for data in arr:
      print ("Максимальное значение из массива: ", data, bubble_while(data)[len(data) - 1])
    end_time = datetime.now()
    print ("Продолжительность: {}".format(end_time - start_time))
    print ('Метод  default')
    start_time = datetime.now()
    for data in arr:
      print ("Максимальное значение из массива: ", data, default(data)[len(data) - 1])
    end_time = datetime.now()
    print ("Продолжительность: {}".format(end_time - start_time))
    print ('Метод  insertion')
    start_time = datetime.now()
    for data in arr:
      print ("Максимальное значение из массива: ", data, insertion(data)[len(data) - 1])
    end_time = datetime.now()
    print ("Продолжительность: {}".format(end_time - start_time))


def main():
  print (minimum(arr))
  print (maximum(arr))

print (main())

data = [12, 4, 54, 29, 46, 36, 72, 99, 85]

def choice(data):
  i = 0
  length = len(data)
  while i < length - 1:
    m = i
    j = i + 1
    while j < length:
      if data[j] < data[m]:
        m = j
      j += 1
    data[i], data[m] = data[m], data[i]
    i += 1
  return data

choice(data)

# Бинарный поиск
from random import randint

def binary_search(arr,x):
  low = 0
  high = len(arr)-1
  index = -1
  while (low <= high) and (index == -1):
    mid = (low+high)//2
    if arr[mid] == x:
      index = mid
    else:
      if x < arr[mid]:
        high = mid - 1
      else:
        low = mid + 1
  return index


# Тестовый маасив
n = 10
arr = []
for i in range (n):
  arr.append(randint(1,99))
arr.sort()
print (arr)
x = int(input("Введи значение элемента: "))

# Вызов и интерпритация функции

if binary_search(arr,x) != -1:
  print ("Элемент найден. Индекс элемента: ",binary_search(arr,x))
else:
  print ("Элемент не найден.")

# Бинарный поиск с рексурсией
from random import randint

def binary_search_rec(arr, low, high, x):
  #Вычисляем середину
  if high >= low:
    mid = (high + low) // 2
    # Если элемент в середине
    if arr[mid] == x:
      return mid
    # Если элемент не в середине, то в левой части
    elif arr[mid] > x: 
      return binary_search_rec(arr, low, mid - 1, x)
    # Если элемент в правой части
    else:
      return binary_search_rec(arr, mid + 1, high, x)
  else:
    # В случае, если элемент вообще не в массиве
    return -1

# Тестовый маасив
n = 10
arr = []
for i in range (n):
  arr.append(randint(1,99))
arr.sort()
print (arr)
x = int(input("Введи значение элемента: "))


# Вызов и интерпритация функции

result = binary_search_rec(arr,0,len(arr)-1,x)

if result != -1:
  print ('Элемент найден под индексом', str(result))
else:
  print ('Элемент не найден')

"""Зарплата сотрудника составляет salary руб., 
Расходы на проживание превышают зарплату и составляют expenses руб. в месяц. 
Расходы растут каждый месяц, кроме 1 на 10% в месяц.
Напишите скрипт расчета суммы денег, которую сотрудник должен брать в кредит, (12 месяцев).
Формат вывода:
Сотрудник будет должен: ХХХ.ХХ рублей

"""

salary = float(input('Введите сумму ЗП в месяц: '))
expenses = float(input('Введите расходы в месяц: '))
month = [1,2,3,4,5,6,7,8,9,10,11,12]
exptemp = expenses


if salary >= expenses:
  print ('Условия задачи нарушены')
else:
  for i in month:
    print ("Сейчас месяц ", i)
    if i != 1:
      all_sallary = salary * i
      print ("Зарплата: ", all_sallary)
      expenses = expenses * 1.1
      exptemp = exptemp + expenses
      print ('Расходы: ', exptemp)
    else:
      print ("1 месяц без %")
      print ("Зарплата: ", salary)
      print ("Расходы: ", expenses)

live = abs(all_sallary - exptemp) # модуль (результат получится со знаком минус)
print ("Сотрудник будет должен:", round(live,2), " рублей") #round(live,2) - округление да 2 символов после запятой