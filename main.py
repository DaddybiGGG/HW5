# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8
#
#
# def rec_pow(number, power) -> int:
#     if power == 0:
#         return 1
#     return number * rec_pow(number, power -1)
# print(rec_pow(2,3))



#-------------------------------------------------------------------------------------------------------------------




# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#
# *Пример:*
#
# 2 2
#     4

def summa(a, b) -> int:
    a += 1
    b -= 1
    if b > 0:
        return summa(a, b)
    else:
        return a

print(summa(3, 5))
