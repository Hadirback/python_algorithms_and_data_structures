'''
9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
'''
top_num = 0
max_sum = 0
for i in range(0, 6):
    num = int(input('Введите число: '))
    tmp_num = num
    sum = 0

    while True:
        tmp_value = num % 10
        sum = sum + tmp_value
        num = num // 10
        if num <= 0:
            break

    if sum > max_sum:
        max_sum = sum
        top_num = tmp_num

print(f'Наибольная сумма цифр - {max_sum} у числа {top_num}')
