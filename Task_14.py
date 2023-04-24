# Задача 14: 
# Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

import sys

n = int(input('Input n: '))
for i in range(0, n):
    num = 2 **i
    if num >= n:
        sys.exit()
    print(num, end=' ')

