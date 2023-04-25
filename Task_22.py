#     Задача 22: 
# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# Input: 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# Output: 6 12

n = int(input('Input a number of elements the array_1: '))
print('Fill the first array out')
array1 = [int(input()) for i in range(n)]
m = int(input('Input a number of elements the array_2: '))
print('Fill the second array out')
array2 = [int(input()) for i in range(m)]

# array1 = '2 4 6 8 10 12 10 8 6 4 2'
# array2 = '3 6 9 12 15 18'
# array1 = set(array1.split(sep=' '))
# array2 = set(array2.split(sep=' '))
array1 = set(array1)
array2 = set(array2)
print(array1)
print(array2)
print(*sorted(array1.intersection(array2), reverse=True))
