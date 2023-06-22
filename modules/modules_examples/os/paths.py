# os для управления файлами и каталогами
import os
#### Получить абсолютные пути только файлов. 
def get_paths(path = '.'):

    for name in os.listdir(path):
        abs_path = os.path.abspath(os.path.join(path, name))
        if os.path.isfile(abs_path) is True:
            yield abs_path
        
        elif os.path.isdir(abs_path) is True:
            yield from get_paths(abs_path)


for i in get_paths('Хранилище'):
    print(i)