#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Даны три действительных числа. Составить программу, выбирающую из них те, которые принадлежат интервалу (0, 1).


if __name__ == '__main__':
    print("Введите три действительных числа:")
    a = float(input())
    b = float(input())
    c = float(input())

    if 0 < a < 1:
        print(f"{a} принадлежит интервалу (0, 1)")
    if 0 < b < 1:
        print(f"{b} принадлежит интервалу (0, 1)")
    if 0 < c < 1:
        print(f"{c} принадлежит интервалу (0, 1)")
