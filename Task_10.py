# Задача 10: 
# На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть
# Input: 5 -> 1 0 1 1 0
# Output: 2


num = int(input('Input a number of coins: '))
eagle = 0
tails = 0
for i in range(num):
    side = int(input('Input coins side: '))
    if side == 1:
        eagle += 1
    else:
        tails += 1
       
if eagle > tails:
    print('tails:', tails)
if eagle < tails:
    print('eagle', eagle)
else:
    print('You can turn either eagle or tails')



