# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.


import io



with io.open('E:\Документы\GeekBrains\Знакомство c Python\homework_4\zadacha_7.txt', 'r', encoding='utf-8') as file:
    spisok = file.read().split(' ')

for i in range(1, len(spisok)): # начинаем с одного потому что A[0] - 1 = -1 a A[0 - 1] = последний элемент в моём случае 10
    if int(spisok[i]) - 1 != int(spisok[i-1]):
        print(i)