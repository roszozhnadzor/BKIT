
# Здесь должна быть реализация декоратора
def print_result(func):
    def dec(*arg):
        print(func.__name__)
        if arg:
            rez = func(arg)
        else:
            rez = func()
        if isinstance(rez, list):
            for i in rez:
                print(i)
        elif isinstance(rez, dict):
            for key, value in rez.items():
                print('{} = {}'.format(key, value))
        return rez

    return dec


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()