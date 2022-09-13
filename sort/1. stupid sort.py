"""
Глупая сортировка
Сложность: O(n3)
Суть:
как только натыкается на пару неотсортированных элементов,
сортирует их и возвращается на новый проход, не завершая первого.
Если доработать - превратится в сортировку пузырьком.
"""

from random import randint
from decos import execution_time

l_lst = [randint(1, 10000) for i in range(10000)]
# l_lst = [5, 4, 3, 2, 1]


@execution_time
def stupid_sort(lst):
    """
    Глупая сортировка
    """
    i = 0
    n = len(lst) - 1
    # m = 0
    while i < n:  # если i = n значит все отсортировано
        # m += 1
        if lst[i] > lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
            i = 0  # если замена была, то делаем новый проход
        else:
            i += 1  # если замены не было - продолжаем
    return lst


stupid_sort(l_lst)
