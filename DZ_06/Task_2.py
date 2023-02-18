# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint
# n = []
# a = int(input('Введите колличество элементов массива: '))
# for i in range(a):
#     a = random.randint(1, 10)
#     n.append(a)
# print(*n)

arr = [randint(1, 10) for i in range(int(input('Введите N: ')))]
print(*arr)

min_num = int(input('Введите минимум: '))
max_num = int(input('Введите максимум: '))
for i in range(len(arr)):
    if min_num < arr[i] < max_num:
        print(f'Индекс числа из заданного диапазона: ', i)