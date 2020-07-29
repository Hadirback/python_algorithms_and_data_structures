'''
5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
'''

num_value = input('Введите номер буквы в латинском алфавите: ')

try:
    num_value = int(num_value)

    if num_value > 0 and num_value < 27:
        letter = chr(num_value + 96)

        print(f'{num_value} номер у буквы {letter}')
except Exception as ex:
    print(f'Exception {ex}')