"""Класс collections.defaultdict()"""
from collections import defaultdict
from timeit import timeit


def check_1():
    dict_of_lst = defaultdict(list)
    res = dict_of_lst["model"]


def check_2():
    dict_of_lst = dict()
    res = dict_of_lst.setdefault("model", [])


print(
    'defaultdict: ',
    timeit(
        f'check_1()',
        globals=globals()))
print(
    'setdefault: ',
    timeit(
        f'check_2()',
        globals=globals()))


"""
defaultdict:  0.430548269
setdefault:  0.262938792
"""


def revers_3():
    s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    d = defaultdict(list)
    for k, v in s:
        d[k].append(v)


def revers_4():
    s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    d = {}
    for k, v in s:
        d.setdefault(k, []).append(v)


print(
    'defaultdict: ',
    timeit(
        f'revers_3()',
        globals=globals()))
print(
    'setdefault: ',
    timeit(
        f'revers_4()',
        globals=globals()))

"""
defaultdict:  1.2769025500000002
setdefault:  1.138680689
"""