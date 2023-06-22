# ООП - Объектно-ориентированное программирование
# ВЫПОЛНЕНО - концепции ООП
# ВЫПОЛНЕНО - создание класса Python
# ВЫПОЛНЕНО - магия Python
# ВЫПОЛНЕНО - наследование

# Императивный стиль - четкий набор инструкций для обработки интерпритатором

# ######################################################################
# Создание объекта
# Создать ячейку из Excel в Python

# Создание класса
# Имена классов записыватся в CamelCase
# если функции - get_value()
# если переменные - shop_list, table, text
# то классы - HouseWhereItAllHappens, BigCar, CargoPlane, BeautifulSoup, Flask, LineProfiler

class Cell:
    # атрибуты - это переменные внутри класса
    content = 1
    content_type = type(content)

    # методы - это функции внутри класса
    def set_value(self, val):
        self.content = val
        self.content_type = type(val)
    

# создание экземпляра (instanse) класса
#   x = 1
#   text = 'Hello' 
A1 = Cell()
B2 = Cell()

# Вызвать атрибуты экземпляра
print(A1.content)
A1.set_value('Hello!')
print(A1.content)
print(A1.content_type)


# ######################################################################
# Магия Python
# Как создавать атрибуты для экземпляра при его объявлении?
# У каждого класса есть набор встроенных специальных методов. Это и есть магия!


# Пример
# Создадим иммитацию объектного хранилища - Бакет
# в которой будем хранить странички нашего сайта

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

# пустой бакет
empt_bucket = Bucket()
print(bool(website))  # True, так как он полон!
print(bool(empt_bucket))  # False, так как он пуст!


# ######################################################################
# Первый код на Python - print('Hello World!')
# Что такое программа - 'Goodbye World!'?

class String:

    # метод __init__ создает экзепляры
    def __init__(self, text) -> None:
        self.text = text

    # метод __del__ унижтожает объекты
    def __del__(self):
        print('Goodbye World!')

greeting = String('Hello World!')
print(greeting.text)



# Пример ДЗ

class Matrix:
    pass

m = Matrix(columns=10, rows=20)
m.set(2, 3, 'Hello')
# 1 1 1
# 1 1 1
# 1 1 1
# 1 1 1

# None None
# None None

# 1 2 3
# 2 4 6
# 3 6 9

# a b
# 1 2