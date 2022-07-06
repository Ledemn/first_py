# TUPLES() --------------------------------------------------------------------------------
ddd = (1, 2, 3, 4)                  # (1, 2, 3, 4)
type(ddd)                           # <class 'tuple'>

a = 1, 2, 3, 4, 5                   # (1, 2, 3, 4, 5)
one = (1,)                          # (1,)

s1, s2, s3, s4, s5 = a


# DICTIONARIES() --------------------------------------------------------------------------------
first_dict = {'first': 1, 'second': 2}
print(first_dict)                   # {'first': 1, 'second': 2}

first_dict.keys()                   # dict_keys(['first', 'second'])
first_dict.values()                 # dict_values([1, 2])
first_dict.items()                  # dict_items([('first', 1), ('second', 2), ('oksana_question', [1, 2, 3])])

list(first_dict.keys())             # ['first', 'second']
first_dict['first']                 # 1


first_dict['oksana_question'] = [1, 2, 3]
print(first_dict)                   # {'first': 1, 'second': 2, 'oksana_question': [1, 2, 3]}


first_dict.popitem()                # ('oksana_question', [1, 2, 3])
first_dict.clear()                  # {}


# SETS() --------------------------------------------------------------------------------
# x = set(<iter>)
a = set('asdfghjhhhhhgg')           # {'f', 'h', 's', 'a', 'g', 'j', 'd'}

# x = {<obj>, <obj>, ..., <obj>}
x = {'foo', 'bar', 'baz', 'foo', 'qux'}
print(x)                            # {'bar', 'foo', 'baz', 'qux'}

x = {'q', 'u', 'u', 'x'}            # {'u', 'q', 'x'}


x1 = {'foo', 'bar', 'buz'}
x2 = {'buz', 'qux', 'quux'}

# x1.union(x2[, x3 ...])
# x1 | x2 [| x3 ...]
x1.union(x2)                        # {'bar', 'quux', 'foo', 'buz', 'qux'}
x1 | x2                             # {'bar', 'quux', 'foo', 'buz', 'qux'}

x1.intersection(x2)                 # {'buz'}
x1 & x2                             # {'buz'}

x1.difference(x2)                   # {'bar', 'foo'}
x1 - x2                             # {'bar', 'foo'}
x2 - x1                             # {'qux', 'quux'}

x1.symmetric_difference(x2)         # {'bar', 'quux', 'foo', 'qux'}
x1 ^ x2                             # {'bar', 'quux', 'foo', 'qux'}
