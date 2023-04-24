# Задача 18: 
# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

import sys

arr = []
n = int(input('Input number of array elemtnts: '))
print('Input elements of array')
for i in range(n):
    arr.append(int(input()))
print(arr)
# arr = [1,2,4,5]
x = int(input('Input a digit for comparing: '))
max_arr = []
min_arr = []
k = None
m = None

for i in arr:
    if i == x:
        print(i)
        sys.exit()
    if i > x:
        max_arr.append(i)
        k = min(max_arr)
    if i < x:
        min_arr.append(i)
        m = max(min_arr)
if m == None:
    print(k)
elif k == None:
    print(m)
else:
    print(m,k)
