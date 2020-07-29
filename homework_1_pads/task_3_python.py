import random

'''
3. Написать программу, которая генерирует в указанных пользователем границах:
    a. случайное целое число,
    b. случайное вещественное число,
    c. случайный символ.
    Для каждого из трех случаев пользователь задает свои границы диапазона. 
    Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
    Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
'''

init_type = input("Введите I Если будет введено число целое, \n F если число вещественное, \n S если символ.").lower()

start = input('Введите начальное значение: ')
end = input('Введите конечное значение: ')

is_correct_type = True

try:
    if init_type == 'i':
        start = int(start)
        end = int(end)
    elif init_type == 'f':
        start = float(start)
        end = float(end)
    elif init_type != 's':
        is_correct_type = False
except:
    is_correct_type = False


if is_correct_type and start != end:

    if start > end:
        tmp = end
        end = start
        start = tmp

    result = None

    if type(start) == int:
        result = random.randint(start, end)
    elif type(start) == float:
        result = random.uniform(start, end)
    elif type(start) == str:
        start = ord(start.lower())
        end = ord(end.lower())
        result = random.randint(start, end)
        result = chr(result)

    print(f'Случайный элемент {result}')

