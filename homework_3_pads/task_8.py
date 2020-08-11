'''
8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
 Программа должна вычислять сумму введенных элементов каждой строки и записывать ее
 в последнюю ячейку строки. В конце следует вывести полученную матрицу.
'''

matrix = []

for i in range(4):
    row = []
    row_sum = 0
    for j in range(5):
        if j != 4:
            elem = int(input())
            row.append(elem)
            row_sum = row_sum + elem
        else:
            row.append(row_sum)
    matrix.append(row)

print(matrix)
