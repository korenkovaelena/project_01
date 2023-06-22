# Подробнее о времени работы
# https://translated.turbopages.org/proxy_u/en-ru.ru.50d68b5e-6347bede-cfadc34c-74722d776562/https/stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution
# https://stackoverflow.com/questions/22328183/python-line-profiler-code-example
# https://python-lab.blogspot.com/2012/07/python.html


from line_profiler import LineProfiler
from probe import *

lp = LineProfiler()
# lp_wrapper_1 = lp(foo_1)
lp_wrapper_2 = lp(foo_2)
# lp_wrapper_3 = lp(foo_3)

# lp_wrapper_1(shop_list)
lp_wrapper_2(shop_list)
# lp_wrapper_3(shop_list)

lp.print_stats()