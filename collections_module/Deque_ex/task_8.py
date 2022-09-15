"""Класс collections.deque()"""
# простые операции с очередью
from collections import deque

simple_lst = list("bcd")
deq_obj = deque(simple_lst)
print(deq_obj)  # -> deque(['b', 'c', 'd'])

# добавим элемент в конец очереди
deq_obj.append('e')
print(deq_obj)  # -> deque(['b', 'c', 'd', 'e'])

# добавим элемент в начало очереди. а почему не insert?
deq_obj.appendleft('a')
print(deq_obj)  # -> deque(['a', 'b', 'c', 'd', 'e'])

# pop также работает с обоих концов
deq_obj.pop()
deq_obj.popleft()
print(deq_obj)  # -> deque(['b', 'c', 'd'])
