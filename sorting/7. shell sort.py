"""
    сортировка Шелла (сортировка с уменьшением инкремента) - shell sort
    суть:
    то же что сортировка вставками но инкремент не 1
    (сравнивает эл в шаге др от др)
    проход - выбираем эл по шагу и срввниваем его со всеми пред в
    соотв с шагом.
    в соответствии с инкрементом выбирает элементы, сортирует их
    (если инкр 4 то сравнивает 4 и 0 5 и 1 и т д),
    инкремент уменьшается, опять выбирает, сортирует,
    как только инкремент = 1 превращается в сортировку вставками

    сложность:
    в лучшем случае O(n log n)
    сильно зависит от размера массива и от выбранной последовательности.
    а выбрать или рассчитать саму последовательность(интервал) — сложно
"""

import timeit
import random


def shell_sort(array):
    n = len(array)
    step = n // 2  # сравнивает эл в шаге др от др
    while step > 0:
        for i in range(step, n):
            temp = array[i]  # временный минимум
            j = i
            while j >= step and array[j - step] > temp:  # условие для сортировки с конца до начала
                array[j] = array[j - step]  # сохраним большее
                j -= step
            array[j] = temp  # сохранили меньшее
        step //= 2
    return array


print(shell_sort([9, 8, 7, 6, 5, 4, 12, 2]))
# проходит 4-7 и сортирует: 4,0 5,1 6,2 7,3 (step=4)
# проходит 2-7 и сортирует: 2,0 3,1 4,2 5,3 6,4 7,5 (step=2)
# проходит 1-7 и сортирует: 1,0 2,1 3,2 4,3 5,4 6,5 7,6 (step=1)
"""
step 4: [9, 8, 7, 6, 5, 4, 12, 2] -> [5, 8, 7, 6, 9, 4, 12, 2] -> [5, 4, 7, 6, 9, 8, 12, 2] -> [5, 4, 7, 2, 9, 8, 12, 6]
step 2: -> [5, 2, 7, 4, 9, 8, 12, 6]
step 1: -> [5, 2, 7, 4, 9, 6, 12, 8] -> [2, 5, 7, 4, 9, 6, 12, 8] -> [2, 4, 5, 7, 9, 6, 12, 8]
-> [2, 4, 5, 6, 7, 9, 12, 8] -> [2, 4, 5, 6, 7, 8, 9, 12]
"""


orig_list = [random.randint(-100, 100) for _ in range(10)]

# замеры 10
print(
    timeit.timeit(
        "shell_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit.timeit(
        "shell_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit.timeit(
        "shell_sort(orig_list[:])",
        globals=globals(),
        number=1000))

"""
0.007556100026704371
0.1487726999912411
2.6570034000324085
"""