# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

numbers = int(input('Введите число элементов: '))
first_number = int(input('Введите первое число: '))
difference = int(input('Введите разность: '))

print(*range(first_number, first_number + difference * numbers, difference))