# Задача 2: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали 
# одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

sum = int(input('Введите общее число журавликов: '))

x = sum / 6 # Петя и Сережа сделали одинаково, поэтому x каждый. Катя сделала в два раза больше , чем Сергей и Петр вместе взятые 2 * (x+x).
sum = 6 * x
a = x
b = x
c = 2*(x+x)

print(f'Петя:',int(a),  'Серёжа:',int(b),  'Катя:',int(c))