#Задачи на циклы и оператор условия------
#----------------------------------------

'''
Задача 1

Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
for i in range(1,6):
    print (str(i) + '.', '00000')
'''
Задача 2

Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
col_5 = 0
for i in range (10):
    if int(input('Введите цифру:')) == 5: col_5 += 1
print('Количество цифр 5 =', col_5)

'''
Задача 3

Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
# sum = 0
#
# for i in range(1,101):
#     sum+=i
# print(sum)

'''
Задача 4

Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''

'''
Задача 5

Вывести цифры числа на каждой строчке.
'''

# integer_number = 2129
#
# #print(integer_number%10,integer_number//10)
#
# while integer_number>0:
#     print(integer_number%10)
#     integer_number = integer_number//10

'''
Задача 6

Найти сумму цифр числа.
'''


'''
Задача 7

Найти произведение цифр числа.
'''

'''
Задача 8

Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
integer_number = 213413
while integer_number>0:
    if integer_number%10 == 5:
        print('Yes')
        break
    integer_number = integer_number//10
else: print('No')

'''
Задача 9

Найти максимальную цифру в числе
'''


'''
Задача 10

Найти количество цифр 5 в числе
'''