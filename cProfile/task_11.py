"""Профилировка времени выполнения функций"""

from cProfile import run
from time import sleep


def fast():
    print("Я быстрая функция")


def slow():
    sleep(3)
    print("Я очень медленная функция")


def medium():
    sleep(0.5)
    print("Я средняя функция...")


def main():
    fast()
    slow()
    medium()


run('main()')
