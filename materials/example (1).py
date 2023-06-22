# Примеры
# Автомобили

# создание класса автомобиль
# который имеет: колеса, двигатель, цвет
# который может: сигналить, заводиться

# класс - лекало или шаблон для создания экземпляров
# на базе класса интерпритатор как на заводе клепает новые объекты

# Наследование
# Родительский класс
class Car:
    """Модель машины"""
    # Секретка в родительском классе?!?!
    __secret_key = 'Секретка'

    # методы класса
    # связыанные методы (bound methods)
    def __init__(self, *, color='Black'):
        # атрибуты при создании экземпляра
        self.wheels = 4
        self.engine_status = False
        self.color = color


    def sound(self):
        print('Beeebeb')
    

    def start(self, key):
        if key == 'Ключ от машины':
            self.engine_status = True
            return self.engine_status
        else:
            return 'Ключ не подходит!'
        

# Дочерний класс
class Sedan(Car):

    class ClimatConrol:
        global temperature
        temperature = 22
        
    pass


# Дочерний класс
class Truck(Car):
    """Самосвал загружает объект в ковш и выгружает в другом месте."""

    def __init__(self, *args):
        super().__init__(color='Yellow')
        print('Загружено в ковш:')
        [print(i) for i in args]

    # def __del__(self):
    #     print('Содержимое выгружено из ковша!')

        
# создание экземпляра класса
# это те машины которые сошли с конвеера
# каждый экземпляр-машина живет своей жизнью
toyota1 = Sedan()
toyota2 = Sedan()
toyota3 = Sedan(color='Yellow')
toyota4 = Sedan(color='Green')


# экземпляр самосвала
belaz = Truck("песок", "щебень", "блоки", "и тд.")

# т.е. мы создавали экземпляры всегда
# shop_list = list()
# rainbow = list()

# изменение атрибута
toyota1.color = 'Red'
print(
    f'toyota1 {toyota1.color}',
    f'toyota2 {toyota2.color}',
    f'toyota3 {toyota3.color}',
    f'toyota4 {toyota4.color}',
    sep='\n'
    )

# атрибута самосвала которые наследуются от родителя Car
print(
    f'Колеса белаза {belaz.wheels}',
    f'Цвет белаза {belaz.color}',
    sep='\n'
)

# вызов метода
# shop_list.append('Картофель')

# для кого вызывается метод?
toyota1.sound()
print(toyota1.start('Ключ от машины'))
print(toyota1.engine_status)


# Вызов атрибута родителя
print(toyota4.__secret_key)






# Абстрактный пример наследования - про самолеты
class Plane:
    def __init__(self) -> None:
        self.wing_length = 100
        self.engine = True

    def fly(self):
        pass

class AirBus(Plane):
    def __init__(self) -> None:
        super().__init__()
        self.cargo = 2
        self.staff = 'Стюардесса'

class WarPlane(Plane):
    def shoot(self):
        return 'Babah!!!'
    
class WarCargoPlane(WarPlane, AirBus):
    def __init__(self) -> None:
        super().__init__()
        self.cargo = 10
        self.staff = 'Военные'
    
TU154 = AirBus()
SU27 = WarPlane()


