"""Ищем НОД двух чисел с помощью алгоритма Евклида"""

def gcd_eucl(arg_1: int, arg_2: int) -> int:
    """Возвращает НОД двух чисел, используя алгоритм Евклида"""
    if arg_2 == 0:
        return arg_1
    return gcd_eucl(arg_2, arg_1%arg_2)

A = int(input())
B = int(input())

print(gcd_eucl(A, B))
