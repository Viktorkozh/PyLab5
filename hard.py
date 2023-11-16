#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# Функция Бесселя первого рода In(x) = ((x/2)^n)*sum(k = 0 to infinity)(((x ^ 2 / 4) ^ k) / (k! * (k + n)!)), значение n = 0, 1, 2, - также должно вводиться с клавиатуры 

import sys
import math

ans = 0

if __name__ == '__main__':
    x = float(input("Введите значение x: "))
    n = int(input("Введите значение n: "))
    if n < 0:
        print("Illegal value of x", file=sys.stderr)
        exit(1)

    ans = x
    term = ans

    while math.fabs(term) > 10*math.exp(-10):
        term *= -x**2*(2*n+1)/((2*n+3)**2*(2*n+2))
        ans += term
        n += 1

    result = ((x / 2) ** n) * ans

    print("Результат вычисления выражения:", result)