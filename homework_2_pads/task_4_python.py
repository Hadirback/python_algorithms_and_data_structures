'''
4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,
    Количество элементов (n) вводится с клавиатуры.
'''

n = int(input('Введите n: '))
sum = 0
item = 1
coeff = -0.5

for i in range(0, n):
    sum = item + sum
    print(item)
    item = item * coeff

print(sum)