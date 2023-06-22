# Если импортировать подпакет вне my_package, 
# то будет доступно имя foo_3, 
# даже если мы не ссылаемся на module_3

from .module_3 import foo_3

