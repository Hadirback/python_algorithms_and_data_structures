'''
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
'''

num = int(input('Введите число: '))

start_num = num
result_value = 0

while True:
    tmp = num % 10
    result_value = tmp + result_value * 10
    num = num // 10

    if num <= 0:
        break

print(result_value)