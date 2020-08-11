'''
2. Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5
(помните, что индексация начинается с нуля), т. к. именно в этих позициях первого массива стоят четные числа.
'''
import random

index_even_nums = []

num_array = [random.randint(0, 100) for _ in range(10)]
for i, num in enumerate(num_array):
    if num % 2 == 0:
        index_even_nums.append(i)

print(num_array)
print(index_even_nums)

