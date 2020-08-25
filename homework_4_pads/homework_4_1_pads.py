
'''
1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать,
b. написать 3 варианта кода (один у вас уже есть),
c. проанализировать 3 варианта и выбрать оптимальный,
d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
e. написать общий вывод: какой из трёх вариантов лучше и почему.
'''

'''
Определить, какое число в массиве встречается чаще всего.
'''

import random
import cProfile as cp



def alg_num_1():
    random.seed(44)
    num_array = [random.randint(0, 1000) for _ in range(100)]
    num_dict = {x: 0 for x in set(num_array)}
    max_count = 0
    max_value = 0
    for elem in num_array:
        num_dict[elem] = num_dict[elem] + 1

        if max_count < num_dict[elem]:
            max_value = elem
            max_count = num_dict[elem]

    return max_count, max_value


def alg_num_2():
    random.seed(44)
    num_array = [random.randint(0, 1000) for _ in range(100)]
    dict_count = {}
    for elem in num_array:
        if elem in dict_count:
            dict_count[elem] = dict_count[elem] + 1
        else:
            dict_count[elem] = 1

    max_value = 0
    max_count = 0

    for key, elem in dict_count.items():
        if max_count < elem:
            max_count = elem
            max_value = key
    return max_count, max_value


def alg_num_3():
    random.seed(44)
    num_array = [random.randint(0, 1000) for _ in range(100)]
    dict_count = {}
    max_value = 0
    max_count = 0

    for elem in num_array:
        if elem in dict_count:
            dict_count[elem] = dict_count[elem] + 1
        else:
            dict_count[elem] = 1

        for key, item in dict_count.items():
            if max_count < item:
                max_count = item
                max_value = key

    return max_count, max_value


'''
timeit:

alg_num_1()
1000 loops, best of 5: 148 usec per loop
Первый вариант выполняется дольше так как создается новый вспомогательный 
словарь и в основном цикле происходит перебор.


1000 loops, best of 5: 125 usec per loop
Второй вариант самый быстрый так как не создается дополнительных словерей.
В данном случае сложнесть алгоритма линейная O(N + c)

1000 loops, best of 5: 314 usec per loop
Трейтий вариант долговыполняющийся, за счет внутреннего вложенного цикла. 
Сложность такого алгоритма O(N^2)
'''

'''
В итоге получаем что 2 вариант самый быстрый, так как идет линейный перебор 
всех значений и с последующим нахождением самого частого числа в последовательности.
'''

