#     Задача 26: 
# Напишите программу, которая на вход принимает 
# два числа A и B, и возводит число А в целую степень B с 
# помощью рекурсии
# A = 2; B = 3 -> 8

def degree(a,b):
    if b == 1:
        return a
    return degree(a, b-1) * a

a = int(input('Input a: '))
b = int(input('Input b: '))
print(degree(a, b))