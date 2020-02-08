"Модуль, содержащий инструменты для работы с простыми числами"

def is_prime(arg: int) -> bool:
    """Тест простоты числа. Реализован с помощью алгоритма перебора делителей"""

    if arg in (2, 3): # обрабатываем исключения
        return True
    if arg % 2 == 0: # проверим делимость на два, чтобы исключить из перебора чётные числа
        return False
    if arg % 3 == 0: # проверим делимость на три, чтобы исключить из перебора числа, кратные трём
        return False

    i = 5 # начнём с 5, так как кратные двум и трём уже проверили
    switch: bool = True # переключатель, чтобы функция знала, когда прибавлять 2, а когда 4
    while i**2 < arg + 1: # смотрим на числа, меньшие sqrt(arg + 1)
        if arg % i == 0:
            return False

def euler_func(arg: int) -> bool:
    "Функция Эйлера. Работает корректно только для простых чисел"

    return arg - 1