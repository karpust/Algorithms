"""Профилировка памяти"""

from memory_profiler import profile


class Point:
    def __init__(self, x=0, y=0, lst=[]):
        self.x = x
        self.y = y
        self.lst = list(range(100000))

    def __del__(self):
        # garbage collector его вызывает, когда удаляет объект
        # cам не удаляет, это не деструктор это finalizer
        # явно его вызывать нельзя
        class_name = self.__class__.__name__
        print(f'{class_name} уничтожен')


@profile
def func():
    pt1 = Point()
    pt2 = pt1
    pt3 = pt1
    print(id(pt1), id(pt2), id(pt3))

    del pt1
    print('ярлык pt1 удален')
    del pt2
    print('ярлык pt2 удален')
    del pt3  # сразу после удаления последней ссылки будет удален объект и вызван __del__
    print('ярлык pt3 удален')


func()
