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
count = 0
print(*arr)

for i in range(len(arr)):
    if arr[i - 1] < arr[i] > arr[(i + 1) % len(arr)]:
        count += 1
        print(i)