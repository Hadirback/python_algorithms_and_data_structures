'''
7. Написать программу, доказывающую или проверяющую, что для множества натуральных
    чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.
'''
correct = True
for num in range(1, 1000):

    sum_value = 0
    for i in range(1, num+1):
        sum_value = i + sum_value

    print(f'Рассчитанная сумма для n = {num} элементов равна {sum_value}')

    formula_value = num * (num + 1) / 2
    print(f'Значение рассчитанное по формуле равно {formula_value}')

    if sum_value != formula_value:
        correct = False

if correct:
    print('Значения верны для 1000 проверенных значений.')
else:
    print('Значения не верны, следовательно формула не верна')