# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

n = int(input('Введите первое число: '))
m = int(input('Введите второе число: '))

def expon_numbers(n, m):
    expon = None
    for i in range(1, n+1):
        expon = n**m
    return expon

a = expon_numbers(n, m)
print(a)