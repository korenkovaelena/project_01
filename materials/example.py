# Примеры
# Автомобили

# создание класса автомобиль
# который имеет: колеса, двигатель, цвет
# который может: сигналить, заводиться

# класс - лекало или шаблон для создания экземпляров
# на базе класса интерпритатор как на заводе клепает новые объекты
class Car:
    # атрибуты класса
    wheels = 4
    engine_status = False
    color = 'Black'

    # методы класса
    # связыанные методы (bound methods)
    def sound(self):
        print('Beeebeb')
    
    def start(self, key):
        if key == 'Ключ от машины':
            self.engine_status = True
            return self.engine_status
        else:
            return 'Ключ не подходит!'
        
# создание экземпляра класса
# это те машины которые сошли с конвеера
# каждый экземпляр-машина живет своей жизнью


toyota1 = Car()
toyota2 = Car()
toyota3 = Car()
toyota4 = Car()

# т.е. мы создавали экземплры всегда
# shop_list = list()
# rainbow = list()

# изменение атрибута
toyota1.color = 'Red'
print('toyota1', toyota1.color, 'toyota2', toyota2.color)

# вызов метода
# shop_list.append('Картофель')

# для кого вызывается метод?
toyota1.sound()
print(toyota1.start('Ключ от машины'))
print(toyota1.engine_status)
