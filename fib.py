import functools
import timeit
from math import *
import sys

def fib(a): # функция без мемоизации, возвращающая число Фиббоначи с заданным номером
    if a==1 or a==2:
        return 1
    f = 1
    fp = 1
    for i in range(a - 2):
        f, fp = f + fp, f
    return f

sys.setrecursionlimit(3047)
@functools.lru_cache()
def fib_mem(a): # функция с мемоизацией, возвращающая число Фиббоначи с заданным номером
    if a==1 or a==2:
        return 1
    fib_mem.cache_clear() # после подсчёта отдельно взятого числа чистим кэш, чтобы всё было честно, иначе для следующего раза значение просто будет взято из словаря
    return fib_mem(a - 1) + fib_mem(a - 2)

print("Введите целое число из [1, 1536]:")

a = int(input())

if a < 1 or a > 1536 or type(a) != int:
    print("Вероятно, вы ошиблсиь :)")
else:
    print(fib_mem(a), '\n')

    t1 = timeit.timeit("fib(a)", setup = "from __main__ import fib, a", number = 10000)
    t2 = timeit.timeit("fib_mem(a)", setup = "from __main__ import fib_mem, a", number = 10000)

    print("Функция с мемоизацией быстрее функции без мемоизации в", round(t1/t2, 2), "раз")
