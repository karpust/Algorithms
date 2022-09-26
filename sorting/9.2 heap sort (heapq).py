"""
    с использованием встроенных методов из модуля heapq:
    heappush(list, item) : добавляет элемент в кучу (куча остается кучей) - для min-heap.
    heappop(list) : удаляет самый маленький элемент и возвращает его
                    (куча остается кучей) - для min-heap.
    _heappop_max, _heappush_max для max-heap

    создание min-heap из массива:
    arr[0] - корень
    если arr[1] > arr[0] - дочерний узел
    если меньше то он меняется местами с родительским
    и т д до конца массива.

    сортировка созданного min-heap:
    корень запомнили а на его место последний элем кучи
    его сравниваем с левым значением
    и т д до конца
"""

import timeit
import random
from heapq import heappop, heappush


def heapq_sort(arr):
    # min-heap:
    heap = []
    for element in arr:
        heappush(heap, element)  # добавляет эл в кучу

    ordered = []

    # while we have elements left in the heap
    while heap:
        ordered.append(heappop(heap))  # heappop удаляет min и возвращает его

    return ordered


array = [13, 21, 15, 5, 26, 4, 17, 18, 24, 2]
print(heapq_sort(array))


orig_list = [random.randint(-100, 100) for _ in range(10)]

# замеры 10
print(
    timeit.timeit(
        "heapq_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit.timeit(
        "heapq_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit.timeit(
        "heapq_sort(orig_list[:])",
        globals=globals(),
        number=1000))

"""
0.0018193998839706182
0.020447699818760157
0.23946100007742643 
"""
# встроенные методы быстрее!!
