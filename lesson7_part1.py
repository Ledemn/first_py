""" Послідовність Фібоначчі
перші два члени послідовності — одиниці, а кожний наступний — сума значень двох попередніх чисел:
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

Часто, особливо в сучасному вигляді, послідовність доповнюється ще одним початковим членом:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

За визначенням, перші два числа в послідовності Фібоначчі є або 1 і 1, або 0 і 1,
залежно від обраного початку послідовностей, а кожне наступне число є сумою двох попередніх.
"""""
print()


def fibonacci_while(n):
    fib1 = 1
    fib2 = 1
    counter = 0
    while counter < n - 2:      # if n is False, while circle doesn't run and fib2 returns instead.
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        counter += 1
        print(fib_sum)  # optional line
    return fib2


""" fibonacci_while()
2 = 1 + 1   3 = 1 + 2   5 = 2 + 3   8 = 3 + 5   13 = 5 + 8  21 = 8 + 13
1 1         2 2         3 3         5 5         8 8         13 13
2 2         3 3         5 5         8 8         13 13       21 21

2           3           5           8           13          21
"""  # ---------------------------------------------------


def fibonacci_for(n):
    fib1 = fib2 = 1
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2      # hardly)
        print(f"{i}: {fib1}")               # optional line
    return f"Desired number is {fib2}."
# ---------------------------------------------------


"""
def fibonacci_recursion(n):
    if n in (1, 2):
        return 1
    return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)
"""


def fibonacci_recursion(n):
    if n in (1, 2):
        print("I'm in simply part.")    # optional line
        return 1
    else:
        print("step ")                  # optional line
    return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)


n_str = input("Enter the number of the desired number: ")
n = int(n_str)
# print(fibonacci_while(n))
# print(fibonacci_for(n))
print(fibonacci_recursion(n))
