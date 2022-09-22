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


d = deque([i for i in range(5)], maxlen=7)
d.append(5)
d.appendleft(6)  # 6012345
d.extend([7, 8, 9])  # 601 2345789 если сзади запихнули, спереди вывалилось(601)
d.extendleft([10, 11])  # 111023457 если спереди зпихнули, сзади вывалилось - maxlen
print(d)

