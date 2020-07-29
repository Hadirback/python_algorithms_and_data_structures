'''
8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
'''

a = int(input('Введите 1 число: '))
b = int(input('Введите 2 число: '))
c = int(input('Введите 3 число: '))

mid_value = None

if b < a < c or c < a < b:
    mid_value = a
elif a < b < c or c < b < a:
    mid_value = b
else:
    mid_value = c

print(mid_value)