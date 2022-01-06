#Задачи на циклы и оператор условия------
#----------------------------------------

'''
Задача 1

Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
print('\nЗадача 1')
for i in range(1,6):
    print (str(i) + '.', '0000000000')
'''
Задача 2

Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
print('\nЗадача 2')
col_5 = 0
for i in range (10):
    if input('Введите цифру:') == '5':
       col_5 += 1
print('Количество цифр 5 =', col_5)

'''
Задача 3

Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
print('\nЗадача 3')
sum_100 = 0
for i in range(1,101):
     sum_100 += i
print('Сумма ряда чисел от 1 до 100 =', sum_100)

'''
Задача 4

Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
print('\nЗадача 4')
mul_10 = 1
for i in range(1, 11):
    mul_10 *= i
print('Произведение ряда чисел от 1 до 10 =', mul_10)
'''
Задача 5

Вывести цифры числа на каждой строчке.
'''
print('\nЗадача 5')
number = 25664129
print('Число -', number, '\nЦифры числа на каждой строчке:')
str_num = str(number)
for i in range(len(str_num)):
    print(str_num[i])

'''
Задача 6

Найти сумму цифр числа.
'''
print('\nЗадача 6')
number = 12345
sum_num = 0
print('Число -', number)
str_num = str(number)
for i in range(len(str_num)):
    sum_num += int(str_num[i])
print('Сумма цифр числа =', sum_num)
'''
Задача 7

Найти произведение цифр числа.
'''
print('\nЗадача 7')
number = 12345
mul_num = 1
print('Число -', number)
str_num = str(number)
for i in range(len(str_num)):
    mul_num *= int(str_num[i])
print('Произведение цифр числа =', mul_num)
'''
Задача 8

Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
print('\nЗадача 8')
number = 325344
print('Число -', number)
str_num = str(number)
i = 0
while i < len(str_num):
    if str_num[i] == '5':
        print('Пятёрка есть')
        break
    i += 1
else:
    print('Пятёрки нет')

'''
Задача 9

Найти максимальную цифру в числе
'''
print('\nЗадача 9')
number = 1245384
max_num = 0
print('Число -', number)
str_num = str(number)
for i in range(len(str_num)):
    if int(str_num[i]) > max_num:
        max_num = int(str_num[i])
print('Максимальная цифра числа =', max_num)
'''
Задача 10

Найти количество цифр 5 в числе
'''
print('\nЗадача 10')
number = 525354
print('Число -', number)
str_num = str(number)
col_5 = 0
for i in range (len(str_num)):
    if str_num[i] == '5':
        col_5 += 1
print('Количество цифр 5 в числе = ', col_5)