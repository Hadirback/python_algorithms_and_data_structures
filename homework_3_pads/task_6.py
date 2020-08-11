'''
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
 Сами минимальный и максимальный элементы в сумму не включать.
'''

import random
start = 0
end = 100

num_array = [random.randint(start, end) for _ in range(20)]
print(num_array)

min_value_index = 0
min_value = end

max_value_index = 0
max_value = start

for i, num in enumerate(num_array):
    if min_value > num:
        min_value = num
        min_value_index = i

    if max_value < num:
        max_value = num
        max_value_index = i


sum_between_min_max = 0


if min_value_index > max_value_index:
    tmp = min_value_index
    min_value_index = max_value_index
    max_value_index = tmp

if max_value_index - min_value_index > 1:
    for num in num_array[min_value_index + 1 : max_value_index]:
        sum_between_min_max = sum_between_min_max + num

print(f'Сумма между числами {min_value} и {max_value} = {sum_between_min_max}')