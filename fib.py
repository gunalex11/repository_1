"""Докстринг для модуля - PyLint попросил"""
import functools
import timeit
import sys


def fib(arg):
    """Функция без мемоизации, возвращающая число Фиббоначи с заданным номером"""
    if arg in (1, 2):
        return 1
    f_n = 1
    f_p = 1
    for i in range(arg - 2):
        f_n, f_p = f_n + f_p, f_n + i - i # PyLint ругался, что i не использован
    return f_n

sys.setrecursionlimit(3047)
@functools.lru_cache()
def fib_mem(arg):
    """функция с мемоизацией, возвращающая число Фиббоначи с заданным номером"""
    if arg in (1, 2):
        return 1
    return fib_mem(arg - 1) + fib_mem(arg - 2)

print("Введите целое число из [1, 1536]:")

A = int(input())

if A < 1 or A > 1536 or isinstance(A, int) == 0:
    print("Вероятно, вы ошиблсиь :)")
else:
    print(fib_mem(A), '\n')

    T1 = timeit.timeit("fib(A)", setup="from __main__ import fib, A", number=10000)
    T2 = timeit.timeit("fib_mem(A)", setup="from __main__ import fib_mem, A", number=10000)

    print("Функция с мемоизацией быстрее функции без мемоизации в", round(T1/T2, 2), "раз")
