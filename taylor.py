import math
import numpy as np
import matplotlib.pyplot as plt

iterations = 20

def my_exp(x: float) -> float:
    """Вычисление экспоненты при помощи частичного суммирования ряда Тейлора"""
    x_pow: float = x
    multiplier: float = 1
    partial_sum: float = 1+x
    for n in range(1, iterations):
        x_pow *= x
        multiplier *= 1 / (n+1)
        partial_sum += x_pow * multiplier
    
    return partial_sum

def div_array(args: np.ndarray, n: float) -> np.ndarray:
    return [a/100 for a in args]

print("Библиотечная экспонента:      ", math.e**2.5)
print("Экспонента через ряд тейлора: ", my_exp(2.5))

plt.figure(1) # графики библиотечной и моей экспоненты приблизительно совпадают на промежутке от 0 до 5
arguments_1: np.ndarray = div_array(np.r_[0:500:1], 100) # MyPy попросил записать шаг с помощью int, поэтому берём все элементы в 100 раз больше, затем делим их на 100 и получаем массив, который хотели. MyPy доволен :)
plt.plot(arguments_1, [math.e**a for a in arguments_1])
plt.plot(arguments_1, [my_exp(a) for a in arguments_1])

plt.figure(2) #  на промежутке от 0 до 20 уже видно, что графики библиотечной и моей экспоненты расходятся
arguments_2: np.ndarray = div_array(np.r_[0:2000:1], 100) # аналогично со строчкой 26
plt.plot(arguments_2, [math.e**a for a in arguments_2])
plt.plot(arguments_2, [my_exp(a) for a in arguments_2])

plt.show()
