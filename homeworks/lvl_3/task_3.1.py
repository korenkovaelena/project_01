# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - использовать готовые классы numpy.array() и pandas.DataFrame() запрещено!
#   - проявите фантазию :)


class Matrix:
    def __init__(self, columns=4, rows=4):
        import random
        self.columns = int(columns)
        self.rows = int(rows)
        running = True
        while running == True:
            try:
                n = int(input('Введите максимальное значение чисел в таблице: '))
                self.content =[]
                for i in range(0, rows):
                    row_list = []
                    for j in range(0, columns):
                        row_list.append(random.randint(1, n))
                    self.content.append(row_list)
                    running = False
            except ValueError:
                print('Надо вводить целое число')
    
   

    def set(self, column, row, element):
        # print(self.content[row-1][column-1])
        try: 
            self.content[row-1][column-1] = int(element)
        except(ValueError, TypeError):
            self.content[row-1][column-1] = None
        print(self.content)


    def get_size(self, columns, rows):
        print(f'Число строк = {rows} и число колонок = {columns}')



m = Matrix(columns=2, rows=2)
print(m.content)
m.set(column=1, row=2, element='jkbm')
m.set(column=1, row=2, element=9)
m.set(column=1, row=2, element=None)