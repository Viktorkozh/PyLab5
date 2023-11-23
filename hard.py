#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Функция Бесселя первого рода In(x) = ((x/2)^n)*sum(k = 0 to infinity)(((x ^ 2 / 4) ^ k) / (k! * (k + n)!)), значение n = 0, 1, 2, - также должно вводиться с клавиатуры

import sys
import math

ans = 0
k = 0


if __name__ == '__main__':
    x = float(input("Введите значение x: "))
    n = int(input("Введите значение n: "))
    
    if n < 0:
        print("Illegal value of n", file=sys.stderr)
        exit(1)

    ans = 1/math.factorial(n)
    term = ans

    while math.fabs(term) > 10**(-10):
        term *= (x**2/4)/((k+1)*(k+n+1))
        ans += term
        k += 1

    result = ((x / 2) ** n) * ans

    print("Результат вычисления выражения:", result)
