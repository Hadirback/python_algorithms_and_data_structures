'''
5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и
    заканчивая 127-м включительно. Вывод выполнить в табличной форме: по десять пар
    «код-символ» в каждой строке.
'''

start_code = 32
end_code = 127
count = 0
string_output = ''

for i in range(start_code, end_code + 1):
    string_output = string_output + f'code: {i} symbol: "{chr(i)}" '
    count = count + 1

    if count == 10:
        count = 0
        print(string_output)
        string_output = ''

    if end_code == i:
        print(string_output)