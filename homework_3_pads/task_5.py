'''
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
'''

import random
start = -100
end = 100

num_array = [random.randint(start, end) for _ in range(20)]
print(num_array)

max_neg_value = start
max_neg_index = 0

for i, num in enumerate(num_array):
    if 0 > num > max_neg_value:
        max_neg_value = num
        max_neg_index = i


print(f"Максимальный отрицательный элемент {max_neg_value}. Его индекс - {max_neg_index}")