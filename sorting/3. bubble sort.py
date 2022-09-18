""" Сортировка пузырьком
    суть:
    сравнивает при каждом проходе все элементы: 1и2, 2и3...
    если пред больше след, меняет местами;
    кол-во проходов пока не отсортирует, = длина массива - 1
    можно оптимизировать чтобы не ходил зря: добавить флаг, чтобы
    поймать проход на кот не было перестановок и завершить сортировку
    сложность:
    в любом случае: квадратичная,
    тк операции выполняются даже если не было перестановок


"""

import timeit
import random


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] > lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


print(bubble_sort([9, 8, 7, 6, 5]))
"""
[9, 8, 7, 6, 5] -> [8, 9, 7, 6, 5] -> [8, 7, 9, 6, 5] -> [8, 7, 6, 9, 5] -> [8, 7, 6, 5, 9] - 1 проход
[7, 8, 6, 5, 9] -> [7, 6, 8, 5, 9] -> [7, 6, 5, 8, 9] - 2 проход
[6, 7, 5, 8, 9] -> [6, 5, 7, 8, 9] - 3 проход
[5, 6, 7, 8, 9] - 4 проход
"""

orig_list = [random.randint(-100, 100) for _ in range(10)]

# замеры 10
print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))

"""
0.009131200000000006
0.7685486
106.773521
"""
