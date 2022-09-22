# import os
# import sys
# os.path.dirname(sys.executable)
import string


def second_max(arr):
    """
    однопроходным алгоритмом
    возвращает второй максимум
    """
    max_1, max_2 = 0, 0
    if len(arr) < 2:
        return None
    elif arr[0] > arr[1]:
        max_1, max_2 = arr[0], arr[1]
    elif arr[1] > arr[0]:
        max_1, max_2 = arr[1], arr[0]
    else:
        max_1 = arr[0]
    for el in arr[2:]:
        if el > max_1:
            max_2, max_1 = max_1, el
        elif el > max_2:
            max_2 = el
    return max_2


def test_second_max():
    res = second_max([6, 10, -1, 7, 5, 4])
    assert res == 7, f'wrong res {res}'
    res = second_max([7, 7, 6])
    assert res == 6, f'wrong res {res}'
    res = second_max([7])
    assert res is None, f'wrong res {res}'
    res = second_max([])
    assert res is None, f'wrong res {res}'
    res = second_max([2, 4])
    assert res == 2, f'wrong res {res}'
    # res = second_max([2, 2])
    # assert res is None, f'wrong res {res}'
    # res = second_max([2, 2, 2])
    # assert res is None, f'wrong res {res}'


test_second_max()



# print(string.ascii_lowercase)
# print(type(string.ascii_lowercase))

lst1 = list(range(1, 21))
lst2 = list(string.ascii_lowercase)
# c = dict(zip(lst1, lst2))
# print(lst1)
# print(lst2)
c = {k: v for k in range(1, 21) for v in string.ascii_lowercase[k-1]}
print(c)


def cda(a, b):
    if b == 0:
        return a
    return cda(b, a % b)


print(cda(28, 6))
print(366%2)
