"""Фибо через цикл"""

# Числа Фибоначчи — бескочечная числовая последовательность,
# в которой каждое число есть сумма двух предыдущих

#  0,1,1,2,3,5,8,13,21...

from timeit import timeit


def func(n_val):
    if n_val < 2:
        return n_val
    pp = 0
    p = 1
    for i in range(n_val-1):
        pp, p = p, pp + p
    return p


n = 8

print(timeit("func(n)", "from __main__ import func, n"))
print(timeit("func(n)", globals=globals()))  # то же
# optional globals argument specifies a namespace in which to execute the code
# globals() return the dictionary containing the current scope's global variables
# те чтобы аргументы замеряемых ф-ций брались из глобальной обл видимости
# так же благодаря globals ушли от импорта ф-ций

# print(timeit.timeit("f(n)", "from __main__ import f")) -> вот так не сработает

"""
0.6502667
0.653676
"""
