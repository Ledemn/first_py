a = [1, 2, 3, 4]
print(a)
print(type(a))

# b = list('a', 'b', 'bbb')   # TypeError: list expected at most 1 argument, got 3
b = list(('aa', 'b', 'gagdghthth'))
print(b)

c = [4, 1, 2, 3]
print(a == c)

d = [1, 2, 3, 4]
print(a == d)
print(a is d)


func = [print, len]
print(type(func))
for i in func:
    for j in b:
        i(j)

# aa
# b
# gagdghthth
# 2
# 1
# 10


a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
#     -6     -5     -4      -3      -2      -1
#      0      1      2       3       4       5

print(a[2:5])               # ['baz', 'qux', 'quux']
print(a[-5:-2])             # ['bar', 'baz', 'qux']
print(a[1:4])               # ['bar', 'baz', 'qux']
print(a[-5:-2] == a[1:4])   # True


string = "sdfasgthgg  trzx"
print(string[0])            # 's'

b = a[::-1]
print(b)                    # ['corge', 'quux', 'qux', 'baz', 'bar', 'foo']

c = a[2:10]
print(c)                    # ['baz', 'qux', 'quux', 'corge']

string_rew = string[::-1]
print(string_rew)           # xzrt  gghtgsafds


non_uniq = [1, 1, 1, 1]     # [1, 1, 1, 1]


aa = a[:]                   # copy
print(aa)                   # ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(aa is a)              # False

string_1 = string[:]
print(string_1 is string)   # True


x = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']
print(x)
print(x[1])                 # ['bb', ['ccc', 'ddd'], 'ee', 'ff']
print(x[1][0])              # 'bb'
print(x[1][1])              # ['ccc', 'ddd']
print(x[1][2])              # 'ee'
print(x[1][3])              # 'ff'
print(x[3])                 # ['hh', 'ii']
print(x[3][0], x[3][1])     # (hh, ii)


# Lists are changeable.
aa[2] = 10                  # ['foo', 'bar', 10, 'qux', 'quux', 'corge']
aa[-1] = 20                 # ['foo', 'bar', 10, 'qux', 'quux', 20]

print(aa)                   # aa is a copy of a
print(a)

print('foo' in a)           # True


print(aa + ['ggg', 'rrr'])  # ['foo', 'bar', 10, 'qux', 'quux', 20, 'ggg', 'rrr']
print(aa)                   # ['foo', 'bar', 10, 'qux', 'quux', 20]

aa = aa * 2
print(aa)       # ['foo', 'bar', 10, 'qux', 'quux', 20, 'foo', 'bar', 10, 'qux', 'quux', 20]
print(len(aa))              # 12


print(min(a))              # 'bar'
numbers = [2, 4, 5.6, 88, 9.123]


print(min(numbers))         # 2
print(max(numbers))         # 88
print(min(c))               # 'baz'
print(max(c))               # 'qux'


del numbers[-2]             # [2, 4, 5.6, 88, 9.123]
print(numbers)              # [2, 4, 5.6, 9.123]

numbers = numbers + numbers[::-1]
print(numbers)              # [2, 4, 5.6, 9.123, 9.123, 5.6, 4, 2]


a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
a[1:4]                      # ['bar', 'baz', 'qux']

a[1:4] = [1.1, 2.2, 3.3, 4.4, 5.5]
print(a)                    # ['foo', 1.1, 2.2, 3.3, 4.4, 5.5, 'quux', 'corge']

a[1:6]                      # [1.1, 2.2, 3.3, 4.4, 5.5]

a[1:6] = ['Bark!']          # ['foo', 'Bark!', 'quux', 'corge']

a[1:1] = 'Bark!'            # ['foo', 'B', 'a', 'r', 'k', '!', 'Bark!', 'quux', 'corge']
del a[1:6]                  # ['foo', 'Bark!', 'quux', 'corge']

a += ['grault', 'garply']   # ['foo', 'Bark!', 'quux', 'corge', 'grault', 'garply']

a = [10, 20] + a            # [10, 20, 'foo', 'Bark!', 'quux', 'corge', 'grault', 'garply']


# help(list)
# a.append(<obj>)
# a.extend(<iterable>)
# a.insert(<index>, ,obj>)
# a.remove(<obj>)
# a.pop(index=-1)

numbers.append(4444)        # [2, 4, 5.6, 9.123, 9.123, 5.6, 4, 2, 4444]
numbers.pop()               # [2, 4, 5.6, 9.123, 9.123, 5.6, 4, 2]
numbers.pop(-4)             # [2, 4, 5.6, 9.123, 5.6, 4, 2]
