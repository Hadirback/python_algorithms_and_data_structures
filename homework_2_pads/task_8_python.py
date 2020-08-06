'''
8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
    Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
'''

seq_of_numbers = int(input('Введите последовательность чисел: '))
find_value = int(input('Введите цифру, которую нужно посчитать в последовательности: '))

start_seq = seq_of_numbers
count = 0

while True:
    tmp = seq_of_numbers % 10
    if tmp == find_value:
        count = count + 1
    seq_of_numbers = seq_of_numbers // 10
    if seq_of_numbers <= 0:
        break

print(f'В последовательности {start_seq} обнаруженно {count} цифр {find_value}')