import sys

from recordclass import recordclass
from collections import namedtuple

# pip install recordclass


def rc_demo():
    var_1 = recordclass('var_1', ('x', 'y', 'z'))
    var_2 = namedtuple('var_2', ('x', 'y', 'z'))
    c = {'x': 1, 'y': 2, 'z': 3}
    a = var_1(x=1, y=2, z=3)
    b = var_2(x=1, y=2, z=3)
    a.x = 4
    '''
    нельзя сделать следующее:
    b.x = 4
    результат: >>> AttributeError: can't set attribute
    '''
    print(f'Объём занимаемой объектом recordclass памяти: {sys.getsizeof(a)} байт(а)')
    print(f'Объём занимаемой объектом namedtuple памяти: {sys.getsizeof(b)} байт(а)')
    print(f'Объём занимаемой объектом dict памяти: {sys.getsizeof(c)} байт(а)')


rc_demo()

"""
Объём занимаемой объектом recordclass памяти: 48 байт(а)
Объём занимаемой объектом namedtuple памяти: 72 байт(а)
Объём занимаемой объектом dict памяти: 240 байт(а)
"""
