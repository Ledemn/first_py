any([False, False, False])          # False
any([False, True, False])           # True
any((False, 1, 0))                  # True


def f():
    print("I'm in f-function")


print(f(), '\n')


def summa(a, b):
    print(a + b)


summa(5, 10)
summa('ssss', 'dddd')
print('\n')  # ------------------------------------------------


def pretty_print(qty, item, price):
    print(f"{qty} {item} cost ${price:.2f}")


pretty_print(6, 'bananas', 1.8888)
pretty_print(price=2.111, qty=7, item='bananas')
pretty_print(8, price=2.444, item='bananas')
print('\n')  # ------------------------------------------------


def pretty_print_1(qty=6, item='bananas', price=1.888):
    print(f"{qty} {item} cost ${price:.2f}")


pretty_print_1(item='lemons')
print('\n')  # -----------------------------------1------------


def add_some(my_list=[]):
    my_list.append('###')
    return my_list


print(add_some())
print(add_some())
print(add_some())
print('\n')  # ------------------------------------2-----------


def add_some(my_list=['---']):
    my_list.append('###')
    return my_list


print(add_some())
print(add_some())
print(add_some())
print('\n')  # ---------------------------------solution----------


def add_some(my_list=None):
    if my_list is None:
        my_list = []
    my_list.append('###')
    return my_list


print(add_some())
print(add_some())
print(add_some())


print('\n')  # ------------------------------------------------


def avg0(a, b, c):
    return (a + b + c)/3


print('avg0:', avg0(34, 67, 154))
# ------------------------------------------------


def avg1(a):
    total = 0
    for v in a:
        total += v
    return total / len(a)


print('avg1:', avg1([34, 67, 154]))
print('avg1 as list:', avg1([34, 67, 154, 55, 6788, -123]))
print('avg1 as tuple:', avg1((34, 67, 154, 55, 6788, -123)))


# ------------------------------------------------*args


def avg2(*args):
    total = 0
    for v in args:
        total += v
    return total / len(args)


print('avg2:', avg2(34, 67, 154))
print('avg2:', avg2(34, 67, 154, 299, ))

t = (11, 22, 33, 55, 89)
print('avg2 (*t):', avg2(*t))


print('\n')  # ------------------------------------------------**kwargs


def avg3(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, '-->', value)


avg3(one=1, two=2, name='Dmz')

fff = {'first': 8, 'second': 16, 'third': 32}
print(avg3(**fff), '\n')


def abc(a, b, *args, **kwargs):  # -----------------a--b--*args--**kwargs
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'args = {args}')
    print(f'kwargs = {kwargs}')


abc('aa', 10.10, 20, 30, 40, 50, 60, hd=720, fhd=1080)
print('\n')


def ggg(x, y, z):               # ----------------------------__doc__
    """It is a function."""
    pass


print(ggg.__doc__)
