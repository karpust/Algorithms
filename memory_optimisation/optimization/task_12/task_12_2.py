import memory_profiler


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_profiler.memory_usage()
        res = func(args[0])
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff
    return wrapper


@decor
def check_even_2(lst):
    new_list = map(str, lst)
    print(type(new_list))
    # print(list(new_list))
    return new_list


if __name__ == '__main__':

    res, mem_diff = check_even_2(list(range(100000)))
    print(f"Выполнение заняло {mem_diff} Mib")

# Выполнение заняло 0.01171875 Mib
