# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите число -> '))
spisok = [n]

def prosto(spisok):
    fl = 0
    for n in range(len(spisok)):
#        fl = 0
        for i in range(spisok[n] // 2, 2, -1):
            if spisok[n] % i == 0:
#                spisok.append(spisok[n] // i)
                spisok.append(i)
                spisok[n] = spisok[n] // i              
                fl += 1
#        spisok.remove(n)
    if fl != 0:
        prosto(spisok)


#spisok.append(n)
prosto(spisok)
    
print(spisok)

