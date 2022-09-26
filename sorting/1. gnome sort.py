"""
    гномья сортировка
    суть:
    синтез пузырьком + вставками

    проход(всего один) -
    идет с начала в конец
    сравнивает со 2-го, эл с предыдущим
    если эл больше пред идет дальше
    если эл меньше пред - меняет местами(пузырьком)
    и идет сортируя в сторону начала(вставками)

    сложность:
    квадратичная
"""


import timeit
import random


def gnome_sort(data):
    i, size = 1, len(data)
    while i < size:
        if data[i - 1] <= data[i]:  # если пред меньше текущего,
            i += 1  # то идем дальше
        else:
            data[i - 1], data[i] = data[i], data[i - 1]  # если нет то меняем местами (пузырьком)
            if i > 1:  # с i-1 уже сравнили, есть ли другие предыдущие
                i -= 1  # и сравниваем эл со всеми предыдущими (вставками)
    return data


print(gnome_sort([9, 8, 7, 6, 5, 4, 12, 2]))

orig_list = [random.randint(-100, 100) for _ in range(10)]

# замеры 10
print(
    timeit.timeit(
        "gnome_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit.timeit(
        "gnome_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit.timeit(
        "gnome_sort(orig_list[:])",
        globals=globals(),
        number=1000))

"""
0.01197719993069768
0.968878599931486
80.09761109994724
"""