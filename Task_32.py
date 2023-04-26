#     Задача 32: 
# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
#         0, 1, 2, 3,  4,  5, 6, 7,  8,  9, 10,11,12,13, 14,15, 16,17, 18, 19
# Вывод: [1, 9, 13, 14, 19]


import random

def get_range(arr, a1, a2):
    ind_arr = [int(i) for i in range(len(arr)) if arr[i] >= a1 and arr[i] <= a2]
    return ind_arr


arr = [random.randint(-10, 10) for i in range(20)]
print(arr)
print('Input the range: ')
a1 = int(input('a1: '))
a2 = int(input('a2: '))
print(get_range(arr, a1, a2))



