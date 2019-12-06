"""Алгоритм, проверяющий простоту числа"""

def is_simple(arg: int) -> int:
    """Тест простоты числа. Реализован с помощью алгоритма перебора делителей"""

    if arg in (2, 3):
        return True
    if arg % 2 == 0: # проверим делимость на два, чтобы исключить из перебора чётные числа
        return False

    i = 3 # начнём с 3, так как 2 уже проверили
    j = 0 # здесь будет индикатор простоты введённого числа
    while i**2 < arg + 1 and j != 1: # смотрим на числа до sqrt(arg + 1) и проверяем наш индикатор
        if arg % i == 0: # если поделилось, нарисуем единичку в индикатор
            j = 1
        i += 2

    if j == 1: # проверка индикатора и окончательный приговор суда
        return False
    return True


A = int(input())
print(is_simple(A))
