"""
    Быстрая сортировка
    суть:
    выбираем опорный элем, по нему разбиваем массив на 3
    1 - все что меньше опорного
    2 - все что больше
    3 - все что равно
    1 и 2 также делятся рекурсивно
    пока не останется
    сложность: линейно-логарифмическая O(n log n)
    в худшем случае(если опорным будет 1-ый элем массива) - квадратичная
"""

import timeit
import random


# def my_calc(lst_obj):
def quick_sort(lst_obj):
    if len(lst_obj) <= 1:
        return lst_obj
    else:
        q = random.choice(lst_obj)
        L = []
        M = []
        R = []
        for elem in lst_obj:
            if elem < q:
                L.append(elem)
            elif elem > q:
                R.append(elem)
            else:
                M.append(elem)
        return quick_sort(L) + M + quick_sort(R)
    # return quick_sort


print(quick_sort([9, 7, 8, 6, 5]))

orig_list = [random.randint(-100, 100) for _ in range(10)]

# замеры 10
print(
    timeit.timeit(
        "quick_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit.timeit(
        "quick_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit.timeit(
        "quick_sort(orig_list[:])",
        globals=globals(),
        number=1000))

"""
0.010884799994528294
0.14124849997460842
1.1644279999891296
"""
