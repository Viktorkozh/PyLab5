#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Дано число (1<=m<=7). Вывести на экран название дня недели, который соответствует этому номеру.

import sys


if __name__ == '__main__':
    n = int(input("Введите номер дня недели: "))

    if n == 1:
        print("Понедельник")
    elif n == 2:
        print("Вторник")
    elif n == 3:
        print("Среда")
    elif n == 4:
        print("Четверг")
    elif n == 5:
        print("Пятница")
    elif n == 6:
        print("Суббота")
    elif n == 7:
        print("Воскресенье")
    else:
        print("Ошибка!", file=sys.stderr)
        exit(1)
