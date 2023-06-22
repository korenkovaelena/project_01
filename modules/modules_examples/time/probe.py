
# Задача 1
# Приведем список покупок в магазине

shop_list =["Рис", "Морковь", "Горошек", "Картофель", "Горошек", "Рис", "Горошек", "Морковь"]

# Измените список согласно пунктам задания
# Выведите результат каждого пункта на консоль по очереди

#   а. Вставьте рыбу между горошком и рисом

# Вариант 1
def foo_1(arr):
    arr.insert(arr.index('Рис'), 'Рыба')

# Вариант 2
def foo_2(arr):
    copy_list = arr.copy()
    name = copy_list.pop(0)
    m_list = list(map(lambda x,y: x + y, arr, copy_list)) 
    n = m_list.index('ГорошекРис')
    arr.insert(n+1, "Рыба")
 


# Вариант 3
def foo_3(arr):
    arr.insert(tuple(i+j for i,j in zip(arr[1:], arr)).index('ГорошекРис'), 'Рыба')







