
#     Задача №31.
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21


#     Задача №33. 
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1
'''
# n = int(input('Input number of marks: '))
# marks = [int(input()) for i in range(n)]
marks = '1 3 3 4 4'
marks = list([int(x) for x in marks.replace(' ', '')])
print(marks)
max_mark = marks[0]
min_mark = marks[0]
for i in marks:
    if i > max_mark:
        max_mark = i
    if i < min_mark:
        min_mark = i
for j in range(len(marks)):
    if marks[j] == max_mark:
        marks[j] = min_mark
print(marks)
'''

#     Задача №35.
# Напишите функцию, которая принимает одно число и 
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое 
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes
'''
import sys
num = int(input('Input a number for checking: '))
if num == 2 or num == 3:
    print('yes')
    sys.exit()
if num % 2 == 0 or num % 3 == 0:
    print('no')
else:
    print('yes')
'''

#     Задача №37.
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

def reverse(n):
    return 

n = int(input('Input a number: '))
arr = [int(input()) for i in range(n)]
print(reverse(arr))
