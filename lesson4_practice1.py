# 1. WHILE
# 1.1 --------------------------------------------------------- :
print('---' * 5, '4.1.1:')

n = 5               # init n
while n > 0:        # then we entered into WHILE (true/false)
    n -= 1          # -1...
    print(n)        # print: 4(true), 3(true) ,2(true) ,1(true) ,0(false).




#
# 1.2 --------------------------------------------------------- :
print('\n\n', '---' * 5, '4.1.2:')

n = 5
while n > 0:
    n -= 1
    if n == 2:
        print("Loop ended")
        break
    print(n)




#
# 1.3 --------------------------------------------------------- :
print('\n\n', '---' * 5, '4.1.3:')


n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue    # 2 skipped
    print(n)




#
# 1.4 --------------------------------------------------------- :
print('\n\n', '---' * 5, '4.1.4:')      # WHILE + ELSE

n = 5
while n > 0:
    n -= 1
    print(n)
else:
    print("Loop done")




#
# 1.5 --------------------------------------------------------- :
print('\n\n', '---' * 5, '4.1.5:')

n = 5
while n > 0:
    n -= 1
    if n == 2:
        break               # вихід за межі циклу.
    print(n)
else:                       # процедура закінчення циклу. Але в циклі.
    print("Loop done")




#
# 1.6 --------------------------------------------------------- :
print('\n\n', '---' * 5, '4.1.6:')

a = ["foo", "bar", "baz", "qux"]
s = "corge"
i = 0
while i < len(a):   # len() func returns a count of elements in the list = 4.
    if a[i] == s:
        break
    i += 1
else:
    print(s, 'not found in list')



#
# 1.7 --------------------------------------------------------- :
print('\n\n', '---' * 5, '4.1.7:')

# while True:                       # незкінченний цикл (для службових прог)
#    print("+" * 30)

n = 5
while n > 0: n -= 1; print(n)     # однорядкова форма запису




#
# 2. FOR
# 2.1 --------------------------------------------------------- :
# for <var> in <iterable>:
#   <statement(s)>

print('\n\n', '---' * 5, '4.2.1:')

a = "Hello, World!"
for i in a:
    print(i)



#
# 2.2 --------------------------------------------------------- :
print('\n\n', '---' * 5, '4.2.2:')

print(iter(a))
iterator_a = iter(a)
print(type(iterator_a))

print(next(iterator_a))
print(next(iterator_a))
print(next(iterator_a))
print(next(iterator_a))
print(next(iterator_a))
print(next(iterator_a))
print(next(iterator_a))
print(next(iterator_a))
print(next(iterator_a))
print(next(iterator_a))
print(next(iterator_a))
print(next(iterator_a))
print(next(iterator_a))
# print(next(iterator_a))   # StopIteration




#
# 2.3 --------------------------------------------------------- :
print('\n\n', '---' * 5, '4.2.3:')

a = ['foo', 'bar', 'baz']

for i in a:                     # 1. iter() for a
    print(i)                    # 2. next()...,   3. StopIteration


# ------- FOR:
# a = ['foo', 'bar', 'baz']
# iter()
# itr = iter(a)
# next(itr)     -> 'foo'
# next(itr)     -> 'bar'
# next(itr)     -> 'baz'
# next(itr)     -> StopIteration
# -------



#
# 2.4 --------------------------------------------------------- :
print('\n\n', '---' * 10, '4.2.4: range()')

x = range(5)
for i in x:
    print(i)


print('\n', '-------range(10)')

for i in range(10):
    print(i)


print('\n', '-------range(2, 10)')

for i in range(2, 10):
    print(i)


print('\n', '-------range(32, 50, 5)')

for i in range(32, 50, 5):
    print(i)


print('\n', '-------range(100, 90, 2)')

for i in range(100, 90, -2):
    print(i)



#
# 2.5 --------------------------------------------------------- :
print('\n\n', '---' * 10, '4.2.5: break, continue, else')
print('-------break')
for i in ["foo", "bar", "baz", "qux"]:
    if 'b' in i:
        break
    print(i)


print('\n', '-------continue')
for i in ["foo", "bar", "baz", "qux"]:
    if 'b' in i:
        continue
    print(i)


print('\n', '-------else')
for i in ["foo", "bar", "baz", "qux"]:
    print(i)
else:
    print('Done.')  # Will execute
