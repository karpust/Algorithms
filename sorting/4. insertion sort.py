"""
    Сортировка вставками
    суть:
    поиск места для вставки меньшего элемента.
    идем от начала массива.
    проход -
    выбираем эл, сравниваем его со всеми пред
    пока не упремся в пред меньше или начало,
    если пред больше - меняем местами.
    новый проход - выбираем след эл и т д

    сложность:
    зависит от упорядоченности изначального массива
    лучший случай: линейная
    худший: квадратичная
    средний: квадратичная
"""


import timeit
import random


def insertion_sort(lst_obj):
    for i in range(len(lst_obj)):
        min_val = lst_obj[i]  # предполагаемый мин
        j = i  # индекс минимума
        while lst_obj[j-1] > min_val and j > 0:  # если пред > след и есть ли пред
            lst_obj[j] = lst_obj[j-1]  # отодвинули большее назад
            j -= 1  # меньшее вперед, ищем куда вставлять
        lst_obj[j] = min_val  # вставка меньшего
    return lst_obj


print(insertion_sort([9, 8, 7, 6, 5]))
"""
[9, 8, 7, 6, 5] -> [9, 9, 7, 6, 5] -> [8, 9, 7, 6, 5] - проход
[8, 9, 9, 6, 5] -> [8, 8, 9, 6, 5] -> [7, 8, 9, 6, 5] - проход
[7, 8, 9, 9, 5] -> [7, 8, 8, 9, 5] -> [7, 7, 8, 9, 5] -> [6, 7, 8, 9, 5] - проход
[6, 7, 8, 9, 9] -> [6, 7, 8, 8, 9] -> [6, 7, 7, 8, 9] -> [6, 6, 7, 8, 9] -> [5, 6, 7, 8, 9] - проход
... etc
"""

orig_list = [random.randint(-100, 100) for _ in range(10)]


# замеры 10
print(
    timeit.timeit(
        "insertion_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit.timeit(
        "insertion_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit.timeit(
        "insertion_sort(orig_list[:])",
        globals=globals(),
        number=1000))

"""
0.004877600003965199
0.3794262999435887
36.00719819997903
"""