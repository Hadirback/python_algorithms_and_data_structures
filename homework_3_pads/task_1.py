'''
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
 Примечание: 8 разных ответов.
'''
nums_array = {x: 0 for x in range(2, 10)}

for num in range(2, 100):
    for i in nums_array:
        if num % i == 0:
            nums_array[i] = nums_array[i] + 1

print(nums_array)


