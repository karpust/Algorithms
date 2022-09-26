"""
    Сортировка слиянием
    суть:
    рекурсивно бьем массив пополам, базовый случай - 1 элем в массиве.
    получаем каждый массив по 1 элементу
    потом собираем их в один сортируя
    пока не получим снова один
    сложность: O(n log n)
    есть больше пямяти т к создает дополнительный массив

"""

import timeit
import random


def merge_sort(lst_obj):
    if len(lst_obj) > 1:  # базовый случай для рекурсии
        center = len(lst_obj) // 2
        left = lst_obj[:center]
        right = lst_obj[center:]

        merge_sort(left)
        merge_sort(right)

        # как только добили до 1 эл в списке
        # выполняем слияние этих массивов
        # а не бьем сразу все
        i, j, k = 0, 0, 0
        # i, j - индексы в лев и правом массивах
        # k - индекс в массиве который собираем

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst_obj[k] = left[i]
                i += 1
            else:
                lst_obj[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst_obj[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst_obj[k] = right[j]
            j += 1
            k += 1
        return lst_obj


"""
[9, 8, 7, 6, 5] -> 
[9, 8] -> [9], [8] - разбили левую - по одному значению в списке - теперь собираем левую -> [8, 9]
[7, 6, 5] -> [7], [6, 5] -> 7 ждет, разбили и собрали правую -> [5, 6]
собираем [7] и [5, 6] -> [5, 6, 7]
собираем [8, 9] и [5, 6, 7] -> [5, 6, 7, 8, 9]
"""

print(merge_sort([9, 7, 8, 6, 5]))

orig_list = [random.randint(-100, 100) for _ in range(10)]

# замеры 10
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))

"""
0.01737159991171211
0.24431610002648085
3.2807770000072196
"""
