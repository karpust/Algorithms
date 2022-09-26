"""
    сортировка кучей (пирамидальная сортировка) - heapsort
    здесь дольше чем встроенными методами (но показывает алгоритм)
    включает два приема: замена корня последним узлом и просейка.
    просейка - если узел меньше чем потомки, его нужно опустить а
    потомков поднять (для max-heap). нужна для создания кучи из
    списка и после замен - чтобы дерево продолжало оставаться кучей.
    при замене корня на его место ставится последний узел кучи, а
    максимумы идут в конец неотсортированного массива
    сложность:
    всегда O(n log n), где n — количество элементов для сортировки
"""

import timeit
import random


def heapify(lst, heap_size, root_i):
    # это просейка:
    # нужно не один раз создать кучу а поддерживать ее после каждой перестановки.
    # если узел меньше чем потомки, его нужно опустить а потомков поднять (max-heap).
    # нужна чтобы дерево всегда было сортирующим т е кучей
    # т е чтобы массив стал кучей и ею оставался всегда
    max_i = root_i  # индекс максимума
    left_i = 2 * root_i + 1  # если у родителя индекс=1 то у левого потомка=3 у правого=4
    right_i = 2 * root_i + 2

    # если верный индекс и потомок больше родителя, меняем местами
    if left_i < heap_size and lst[left_i] > lst[max_i]:
        max_i = left_i
    if right_i < heap_size and lst[right_i] > lst[max_i]:
        max_i = right_i

    # если наибольший элемент уже не корневой, они меняются местами
    if max_i != root_i:
        lst[root_i], lst[max_i] = lst[max_i], lst[root_i]
        heapify(lst, heap_size, max_i)  # просейка - поддерживаем кучу


def heap_sort(lst):
    # принимает обычный список
    n = len(lst)
    # создаём max-heap из списка:
    for i in range(n, -1, -1):  # идем с конца в начало (шаг надо)
        heapify(lst, n, i)  # просейка

    # перемещаем корень Max Heap в самый конец списка
    for i in range(n - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        heapify(lst, i, 0)  # просейка т к произошла замена


random_list_of_nums = [35, 12, 43, 8, 51]
heap_sort(random_list_of_nums)
print(random_list_of_nums)

"""
[35, 12, 43, 8, 51] [35, 51, 43, 8, 12] [51, 35, 43, 8, 12] - за первый цикл создали кучу
[43, 35, 12, 8, 51] [35, 8, 12, 43, 51] [12, 8, 35, 43, 51] [8, 12, 35, 43, 51] 
"""


orig_list = [random.randint(-100, 100) for _ in range(10)]

# замеры 10
print(
    timeit.timeit(
        "heap_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit.timeit(
        "heap_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit.timeit(
        "heap_sort(orig_list[:])",
        globals=globals(),
        number=1000))


"""
0.010328100062906742
0.1810394001659006
2.943405400030315
"""