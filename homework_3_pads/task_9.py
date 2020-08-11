'''
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
'''

import random

col_size = 4
row_size = 5

start = 0
end = 100

matrix = [[random.randint(start, end) for _ in range(col_size)] for _ in range(row_size)]

print(matrix)

min_col_values_array = []
for i in range(col_size):
    min_value_col = end

    for j in range(row_size):
        if min_value_col > matrix[j][i]:
            min_value_col = matrix[j][i]

    min_col_values_array.append(min_value_col)

max_item = start
for num in min_col_values_array:
    if max_item < num:
        max_item = num

print(f"Максимальный элемент {max_item} из {min_col_values_array}")