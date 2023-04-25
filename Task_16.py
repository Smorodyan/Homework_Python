# Задача 16: 
# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих 
# строках записаны N целых чисел Ai
# Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

arr = []
n = int(input('Input number of array elemtnts: '))
print('Input elements of array')
for i in range(n):
    arr.append(int(input()))
print(arr)
x = int(input('Input a digit for searching: '))
count = 0
for i in arr:
    if i == x:
        count += 1
print(count)
