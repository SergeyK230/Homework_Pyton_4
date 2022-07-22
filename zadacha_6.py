# Создать текстовый файл (не программно). 
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк). 
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. 
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# 
# Иванов 23543.12
# Петров 13749.32

import io
slovar = {}
with io.open('E:\Документы\GeekBrains\Знакомство c Python\homework_4\zadacha_6.txt', 'r', encoding='utf-8') as file:
    for line in file:
        vrem = line.strip().split(' ')
        slovar[vrem[0]] =  vrem[1]

sred = 0
col = 0
for key in slovar:
    sred = float(slovar[key]) + sred
    col+=1
    if float(slovar[key]) < 20000.0:
        print(key)

print(f'Средняя зарплата = {round(sred/col,2)}')