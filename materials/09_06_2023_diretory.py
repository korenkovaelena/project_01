import os

def get_path(path = '.'):
    for name in os.listdir(path):
        abs_path = os.path.abspath(os.path.join(path,name))
        yield abs_path # yield - то же самое что return,  
## но yield-ы выплнются все, а return выполняется только первый
## yield функциягенератор (возвращает не точлько опр знач-е, но и функцию, 
## может итрироваться
## запоминает значение переменной и оно может ипользоваться для повторного вызова ф-ции
        if os.path.isdir(abs_path) is True:
            yield from get_path(abs_path)

for i in get_path('homeworks'):
    print(i)

# задача 2

# def get_path(path = '.'):
#     for name in os.listdir(path):
#         abs_path = os.path.abspath(os.path.join(path,name))
#         if os.path.isfile(abs_path) is True:
#             yield abs_path
#         elif os.path.isdir(abs_path) is True:
#             yield from get_path(abs_path)

# for i in get_path('homeworks'):
#     print(i)
