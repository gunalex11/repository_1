"""Вывод числа в произвольной системе счисления( <= 36)"""

def to_str(arg: int) -> str:
    """Переводит целое число из [0, 35] в строку, содержащую символ от 0 до 9 или от A до Z"""
    if arg < 10:
        return chr(arg + 48)
    return chr(arg + 55)

def str_base(value: 'int', base: 'int') -> 'str':
    """Shows value using number base, e.g. str_base(44027, 36)=='XYZ'"""

    output: str = ""
    while value != 0:
        output += to_str(value % base)
        value //= base
    return ''.join(reversed(output))

V = int(input("Value? (integer)" + '\n'))
B = int(input("Base? (integer in [1, 36])" + '\n'))

if B not in range(1, 37):
    print("Mi scusi, you're mistaken :c")
else:
    print(str_base(V, B))
