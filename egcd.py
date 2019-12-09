"""Ищем коэффициенты Безу для двух чисел и их НОД"""

from typing import Tuple, Any

def gcd_eucl(arg_1: int, arg_2: int) -> int: # из предыдущего задания про НОД
    """Возвращает НОД двух чисел, используя алгоритм Евклида"""
    if arg_2 == 0:
        return arg_1
    return gcd_eucl(arg_2, arg_1%arg_2)

def egcd(a_1: int, a_2: int) -> Tuple[Any, Any, Any]:
    """Возвращает НОД и соотношение Безу для двух чисел в виде списка"""
    gcd = gcd_eucl(a_1, a_2)
    for i in range(10 ** 3):
        for j in range(10 ** 3):
            if i * a_1 + j * a_2 == gcd:
                return i, j, gcd
            if -i * a_1 - j * a_2 == gcd:
                return -i, -j, gcd
            if -i * a_1 + j * a_2 == gcd:
                return -i, j, gcd
            if i * a_1 - j * a_2 == gcd:
                return i, -j, gcd
    return '❌', '❌', '❌' # На случай, если алгоритм окажется бессилным

A = int(input())
B = int(input())

R = egcd(A, B)

print("Bezout's coefficients are:", R[0], R[1])
print("gcd is:", R[2])
