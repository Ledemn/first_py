# global and local
# LEGB
# ----------------------------------------------------------
# x = value
# import module
# from module import name
# def func(): ...
# def func(arg1, arg2, ... argN): ...
# class MyClass: ...
print()  # -------------------------------------------------


def square(base):   # base and result are local vars.
    """ This func prints a square of any number."""
    result = base ** 2
    print(f"The square of {base} is {result}.")


square(2)
square(4)
print()


def cube(base):   # base and result are local vars.
    """ This func prints a cube of any number."""
    result = base ** 3
    print(f"The cube of {base} is {result}.")


cube(2)
cube(4)
print()

print("-" * 30)  # --------------

var = 200


def outer_func():
    var = 100
    another_var = 300

    def inner_func():
        print(f"from inner_func: {var}")
        another_var = 500
        print(f"from inner_func: {another_var}")

    inner_func()
    print(f"printing var from outer_func: {var}")
    print(f"printing another_var from outer_func: {another_var}")


outer_func()
print()

# __main__
print(dir())
