'''
4. Определить, какое число в массиве встречается чаще всего.
'''

import random

num_array = [random.randint(0, 10) for _ in range(100)]
num_dict = {x: 0 for x in set(num_array)}
max_count = 0
max_value = 0
for elem in num_array:
    num_dict[elem] = num_dict[elem] + 1

    if max_count < num_dict[elem]:
        max_value = elem
        max_count = num_dict[elem]


print(num_array)
print(num_dict)

print(f"Число {max_value} встречается чаще всего в массиве - ({max_count}) раз")

