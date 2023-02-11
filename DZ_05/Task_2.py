# Задача 28: Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел.

# 2 2
# 4

n = int(input('Введите первое число: '))
m = int(input('Введите второе число: '))

def sum_numbers(n, m):
    # sum = None
    for i in range(1, n+1):
        sum = n+m
    return sum

a = sum_numbers(n, m)
print(a)