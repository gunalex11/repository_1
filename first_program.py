#!/usr/bin/env python3 # линия Шебанга - указатель на интерпретатор, который должен использоваться
# -*- coding: utf-8 -*- # объявление используемой кодировки
 
import math # подключение модуля math из стандартной библиотеки
import numpy # подключение библиотеки numpy
import matplotlib.pyplot as mpp # подключение модуля pyplot из библиотеки matplotlib (для удобства - mpp)


if __name__=='__main__': # находящийся в этой конструкции код будет выполнен, только если программа вызвана как самостоятельная, а не в качестве модуля в другой программе
    arguments = numpy.r_[0:5:0.1] # создание средствами numpy массива arguments, содержащего числа с плавающей точкой в [0, 200) с шагом в 0.1
    mpp.plot(
        arguments,
        [(math.e)**a for a in arguments]
    ) # создание графика, содержащего по оси абсцисс значения массива arguments, а по оси ординат - значения нового массива, который состоит из значений функции в точках из массива arguments
mpp.show() # отображение окна с графиком
