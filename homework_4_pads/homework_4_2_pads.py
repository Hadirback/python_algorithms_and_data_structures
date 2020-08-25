'''
2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и
попробуйте его улучшить/оптимизировать под задачу.
Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
'''


def get_simple_num(index):
    if index >= 1 and index <= 3:
        return index

    simple_list = [2, 3]
    max_simple_value = 3
    tmp_index = 3

    while tmp_index != index:
        max_simple_value = max_simple_value + 1
        is_simple = True

        for num in simple_list:
            if max_simple_value % num == 0:
                is_simple = False
                break

        if is_simple:
            simple_list.append(max_simple_value)
            tmp_index = tmp_index + 1

    return max_simple_value


def get_simple_num_sieve_of_eratosthenes(index):
    n = index

    a = []
    for i in range(n + 1):
        a.append(i)
    a[1] = 0

    i = 2
    while i <= n:
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j = j + i
        i += 1

    a = set(a)
    a.remove(0)
    return a

print(get_simple_num(10))
print(get_simple_num_sieve_of_eratosthenes(10)0