#     Задача 30: 
# Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: 
# an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

def progress(a, b, c):
    arr = [int(i) for i in range(a, a + b * c, b)]
    return arr


first_element = int(input('Input the first element: '))
diff = int(input('Input the diffrence: '))
num_of_elements = int(input('Input number of elements: '))
print(progress(first_element, diff, num_of_elements))

