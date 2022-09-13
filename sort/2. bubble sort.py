"""
Сортировка пузырьком или сортировка простыми обменами.
Эффективен только для небольших массивов.
На практике почти не применяется, простой но очень медленный.
Сложность: O(n2)
Суть:
Максимумы всплывают в конец списка.
При каждом проходе больший элемент всплывает к концу списка.
Обходим весь список сравнивая соседние элементы.
Если они не отсортированы меняем местами.
Повторяем проходы пока все не отсортируем и даже больше.
"""

from random import randint
from decos import execution_time

l_lst = [randint(1, 10000) for i in range(10000)]
# l_lst = [5, 4, 3, 2, 1]


@execution_time
def bubble_sort(lst):
    """
    обычная сортировка пузырьком
    """
    ll = len(lst)-1  # здесь ll это кол-во максимумов, которое должно всплыть к конецу списка
    for k in range(ll):
        for i in range(ll):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst


@execution_time
def bubble_sort_1(lst):
    """
    оптимизированная сортировка пузырьком:
    не совершает нового прохода по списку,
    если в предыдущем не было ни одной замены.
    """
    ll = len(lst)-1
    swap = True
    while swap:
        swap = False
        for i in range(ll):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                swap = True  # если будет хотябы одна замена,
                # swap переключится на True и будет следующий проход
    return lst


@execution_time
def bubble_sort_2(lst):
    """
    оптимизированная сортировка пузырьком:
    проходя на один элемент меньше при каждом проходе.
    (один проход = один элемент встал на свое место)
    не совершает нового прохода по списку,
    если в предыдущем не было ни одной замены.
    """
    ll = len(lst)-1
    swap = True
    while swap:
        swap = False
        for i in range(ll):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swap = True
        ll -= 1
    return lst


bubble_sort(l_lst)
bubble_sort_1(l_lst)
bubble_sort_2(l_lst)
