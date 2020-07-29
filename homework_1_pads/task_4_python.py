'''
4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
'''


start = input('Введите первую букву: ')
end = input('Введите вторую букву: ')

if len(start) == 1 and len(end) == 1 and start.isalpha() and end.isalpha():

    if start > end:
        tmp = end
        end = start
        start = tmp

    start = start.lower()
    end = end.lower()

    place_start = ord(start) - 96
    place_end = ord(end) - 96

    count_letters = place_end - place_start - 1

    print(f'Место занимаемое буквой {start} - {place_start}')
    print(f'Место занимаемое буквой {end} - {place_end}')
    print(f'Между ними {count_letters} буква(ы).')

