"""Стандартная сортировка"""

import timeit
import random


def reverse_sort(lst_obj):
    lst_obj.sort()
    return orig_list


orig_list = [random.randint(-100, 100) for _ in range(10)]

# замеры 10
print(
    timeit.timeit(
        "reverse_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit.timeit(
        "reverse_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit.timeit(
        "reverse_sort(orig_list[:])",
        globals=globals(),
        number=1000))

"""
0.00039260000000000683
0.004685000000000009
0.0959738
"""
