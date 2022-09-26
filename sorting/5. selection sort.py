""" Сортировка выбором
    суть:
    выбрать 1-ый элемент, сравнить с остальными,
    заменить наименьшим и так по порядку
    сложность:
    квадратичная O(n^2)
"""

import timeit
import random


def selection_sort(lst_obj):
    for i in range(len(lst_obj)):
        idx_min = i  # индекс того что выбрали
        for j in range(i + 1, len(lst_obj)):  # индекс того с чем сравниваем
            if lst_obj[j] < lst_obj[idx_min]:
                idx_min = j  # находит индекс минимума
        lst_obj[idx_min], lst_obj[i] = lst_obj[i], lst_obj[idx_min]  # поменяли местами

    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10)]
print(selection_sort(orig_list))

# замеры 10
print(
    timeit.timeit(
        "selection_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit.timeit(
        "selection_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit.timeit(
        "selection_sort(orig_list[:])",
        globals=globals(),
        number=1000))

"""
0.008804099983535707
0.3658761999104172
28.72636829991825
"""
