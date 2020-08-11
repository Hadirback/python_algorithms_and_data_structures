'''
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться.
'''

import random
start = 0
end = 10

num_array = [random.randint(start, end) for _ in range(5)]

first_min_value = end
second_min_value = end

for num in num_array:
    if first_min_value == num:
        second_min_value = num

    if first_min_value > num:
        second_min_value = first_min_value
        first_min_value = num
    elif second_min_value > num:
        second_min_value = num


print(num_array)

print(f"Первый минимальный элемент - {first_min_value}")
print(f"Второй минимальный элемент - {second_min_value}")