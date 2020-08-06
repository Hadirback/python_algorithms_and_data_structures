'''
2. Посчитать четные и нечетные цифры введенного натурального числа.
    Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
'''

num = int(input('Введите число: '))

start_num = num
even_numbers = 0
odd_numbers = 0

while True:
    tmp = num % 10
    if tmp % 2 == 0:
        even_numbers = even_numbers + 1
    elif tmp % 2 != 0:
        odd_numbers = odd_numbers + 1

    num = num // 10

    if num <= 0:
        break

print(f'Введенное число {start_num} содержит {even_numbers} четное(ых) чисел(о) и {odd_numbers} нечетное(ых)')




print()