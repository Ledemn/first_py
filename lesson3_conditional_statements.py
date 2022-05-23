####
# if -оператор <expr -вираз в булієвському контексті>: не забуваємо за двокропек!
# відступ <statement -оператор>
####
####
# >>> x = 5
# >>> y = 0
# >>> if y > 5:
# ...     print('yes')
# ...
# ------------------------------------------------------
# >>> if y < x:
# ...     print('yes')
# ...
# yes
# ------------------------------------------------------
# >>> if x:
# ...     print("yes")
# ...
# yes
# ------------------------------------------------------
# >>> if 'fff' in 'dfagsfg gsg fff':
# ...     print("yes")
# ...
# yes
# ------------------------------------------------------
# >>> if 'fff' in 'aaa bbb fff sss':
# ...     z = 3 + 2
# ...     print(z)
# ...     print("fff")
# ...
# 5
# fff
# ------------------------------------------------------
name = "John"
if name == "Fred":
    print("Hello, Fred")
elif name == "Sara":
    print("Hello, Sara")
elif name == "John":
    print("Hello, John")
else:
    print("Hello, friend!")

# Hello, John
# ------------------------------------------------------

# ------------------------------------------------------
# не рекомендується використовувати однорядкові оператори IF, як показано нижче:
# if "f" in "foo": print("1"); print("2"); print("3")
# elif "d" in "ddd": print("4"); print("5")
# else: print("in else")

# не рекомендується використовувати однорядкові оператори IF, як показано нижче:
# if "f" in "foo":
#     print("1"); print("2"); print("3")
# elif "d" in "ddd":
#     print("4"); print("5")
# else:
#     print("in else")

# правильний запис показано нижче:
if "f" in "foo":
    print("1")
    print("2")
    print("3")
elif "d" in "ddd":
    print("4")
    print("5")
else:
    print("in else")
# 1
# 2
# 3
# ------------------------------------------------------
if "m" in "foo":
    print("1")
    print("2")
    print("3")
elif "d" in "ddd":
    print("4")
    print("5")
else:
    print("in else")
# 4
# 5
# ------------------------------------------------------
if "k" in "foo":
    print("1")
    print("2")
    print("3")
elif "l" in "ddd":
    print("4")
    print("5")
else:
    print("in else")
# in else
# ------------------------------------------------------
# інколи використання однорядкових операторів IF виправдане:
debugging = True
if debugging: print("We are testing a code.")
# We are testing a code.


# ------------------------------------------------------
# тренарний оператор    <expr1> if <conditional_expr> else <expr2>
#
x = y = 40
z = 1 + x if x > y else y + 2
print(z)
# 42
# ------------------------------------------------------
# () - для зрозумілості пріоритету виконання: (1дія) 3дія (2дія)
x = y = 40
z = (1 + x) if x > y else (y + 2)
print(z)
# 42
