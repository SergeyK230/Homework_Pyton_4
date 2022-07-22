# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

with open('E:\Документы\GeekBrains\Знакомство c Python\homework_4\zadacha_5,1.txt', 'r') as file:
   mnog1 = file.read()
   mnog1 = mnog1[0:-4]

with open('E:\Документы\GeekBrains\Знакомство c Python\homework_4\zadacha_5,2.txt', 'r') as file:
   mnog2 = file.read()

with open('E:\Документы\GeekBrains\Знакомство c Python\homework_4\zadacha_5.txt', 'w', encoding='utf-8') as file:
   file.write(f'{mnog1} + {mnog2}')
