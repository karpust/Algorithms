import time


def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        exec_time = end_time - start_time
        print(f'Функция {func.__name__}: {func.__doc__}'
              f'Время выполнения: {exec_time}\n')
    return wrapper
