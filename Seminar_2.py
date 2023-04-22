
# Задача №9.
# По данному целому неотрицательному n вычислите 
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех 
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл 
# while
# Input: 5
# Output: 120

'''
n = int(input('Input a number for Factorial: '))
sum = 1

while n > 1:
    sum *= n
    n -= 1
print(sum)
'''



# Задача №11. 
# Дано натуральное число A > 1. Определите, каким по 
# счету числом Фибоначчи оно является, то есть 
# выведите такое число n, что φ(n)=A. Если А не 
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

n = int(input('Input Fibonachi number: '))
num1 = 0
num2 = 1
fibonachi = 0
count = 1
for i in range(n):
    fibonachi = num1 + num2
    num1 = num2
    num2 = fibonachi
    count += 1
    print(fibonachi, end=' ')
print()
print('Output:', count)




# Задача №13. 
# Уставшие от необычно теплой зимы, жители решили узнать, 
# действительно ли это самая длинная оттепель за всю историю 
# наблюдений за погодой. Они обратились к синоптикам, а те, в 
# свою очередь, занялись исследованиями статистики за 
# прошлые годы. Их интересует, сколько дней длилась самая 
# длинная оттепель. Оттепелью они называют период, в 
# который среднесуточная температура ежедневно превышала 
# 0 градусов Цельсия. Напишите программу, помогающую 
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

'''
n = int(input('Input a number of days: '))
num = []
for i in range(n):
    degree = int(input('degree: '))
    num.append(degree)
print(num)
count = 0
degree_count = 0
for j in num:
    if j > 0:
        count += 1
        if degree_count < count:
            degree_count = count
    else:
        count = 0
    
print(degree_count)
'''


# Задача №15. 
# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. 
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача: 
# арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

'''
n = int(input('Input numver of watermelons: '))
watermelon =[]
for i in range(n):
    num = int(input('kg: '))
    watermelon.append(num)
print(watermelon)

min = watermelon[0]
max = watermelon[0]
for i in watermelon:
    if i < min:
        min = i
    if i > max:
        max = i

print('min: ', min)
print('max: ', max)
'''