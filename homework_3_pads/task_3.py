'''
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''

import random
start = 0
end = 100

num_array = [random.randint(start, end) for _ in range(10)]
print(num_array)
min_value = max_value = num_array[0]

min_index = end
max_index = start

for i, num in enumerate(num_array):
    if num > max_value:
        max_value = num
        max_index = i

    if num < min_value:
        min_value = num
        min_index = i

num_array[min_index] = max_value
num_array[max_index] = min_value

print(num_array)

