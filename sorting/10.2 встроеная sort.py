"""
    Стандартная сортировка Timsort:
    Внутри Python использует Timsort – гибридный алгоритм сортировки,
    сочетающий сортировку вставками и сортировку слиянием.
    Смысл в том, что в реальном мире часто встречаются частично
    отсортированные данные, на которых Timsort работает ощутимо
    быстрее прочих алгоритмов сортировки. Сложность по времени:
    O(n log n) в худшем случае и O(n) – в лучшем.

    list.sort() - Сортирует лист, но возвращает None
    sorted(list) - Сортирует лист и возвращает его
"""

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
0.0004811999388039112
0.003860600059852004
0.09319529996719211
"""

"""
https://www.w3schools.com/python/ref_list_sort.asp
"""


# A function that returns the length of the value:
def my_func(word):
    return len(word)


cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=my_func)  # ['VW', 'BMW', 'Ford', 'Mitsubishi']
cars.sort(reverse=True, key=my_func)  # ['Mitsubishi', 'Ford', 'BMW', 'VW']
# сортирует результ ф-ции


lst = [2, 4, 1, 2, 5]
dic = {i: lst[i] for i in range(len(lst))}
dic = sorted(dic.items(), key=lambda x: x[1])  # 1 т к сортируем по values
lst = [dic[i][0] for i in range(4)]
print(lst)
