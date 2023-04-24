# Задача №17.
# Дан список чисел. Определите, сколько в нем 
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

'''
lst = [1, 1, 2, 0, -1, 3, 4, 4]
new_list = set(lst)
print(new_list)
print(len(new_list))
'''


# Задача №19. 
# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность 
# (сдвиг - циклический) на K элементов вправо, K – 
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

'''
lst = [1, 2, 3, 4, 5]
k = 3
new_list = []
for i in lst[k:]:
    new_list.append(i)
# print(new_list)
for j in lst[:k]:
    new_list.append(j)
print(new_list)
'''



# Задача №21.
# Напишите программу для печати всех уникальных 
# значений в словаре. 
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII 
# ":" S007 "}] 
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

'''
dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
        {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}] 
new_dict = []
for i in dict:
    # print(i)
    for value in i.values():
        new_dict.append(value.replace(' ',''))
print(new_dict)

get_cleaned_dict = set(new_dict)
print(get_cleaned_dict)
'''


# Задача №23. 
# Дан массив, состоящий из целых чисел. Напишите 
# программу, которая подсчитает количество 
# элементов массива, больших предыдущего (элемента 
# с предыдущим номером) 
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

arr = [0, -1, 5, 2, 3]
count = 0

for i in range(1, len(arr)):
    if arr[i] > arr[i - 1]:
        print(arr[i])
        count += 1
print(count)









