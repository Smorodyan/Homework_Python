    # Задача №25.
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

'''
str = 'a a a b c a a d c d d'
str1 = str.split(sep=' ')
print(str1)
str = str.replace(' ', '')
str2 = sorted(set(str))
print(str2)

for i in str2:
    count = 0
    for j in range(len(str1)):
        if str[j] == i:
            if count == 0:
                # print(i, end=' ')
                count += 1
            else:
                # print(f'{i}_{count}', end=' ')
                str1[j] = f'{i}_{count}'
                count += 1
print(*str1)
   '''


#     Задача №27.
# Пользователь вводит текст(строка). Словом считается 
# последовательность непробельных символов идущих 
# подряд, слова разделены одним или большим числом 
# пробелов. Определите, сколько различных слов 
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

'''
quote = 'She sells sea shells on the sea shore The shells that she sells are sea shells I"m sure.So if she sells sea shells on the sea shore I"m sure that the shells are sea shore shells'
quote = quote.replace('.', ' ').split(sep=' ')
new_quote = set(quote)
print(new_quote)
print(len(new_quote))
'''


#     Задача №29. 
# “Задана последовательность неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. 

'''
arr = '1352647246063565053231'
# arr = int(list(arr))
arr = [int(x) for x in list(arr)]
print(arr)
max = arr[0]
for i in arr:
    if i == 0:
        print(max)
        break
    if i > max:
        max = i
'''











