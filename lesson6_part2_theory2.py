a = 123
b = str(a)
print(f"type of a: {type(a)}")      # type of a: <class 'int'>
print(f"type of b: {type(b)}")      # type of b: <class 'str'>

c = "qwertyui"
d = list(c)
print(d)        # ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i']

sss = iter(c)
print(sss)
step_1 = next(sss)
print(step_1)
step_2 = next(sss)
print(step_2)
# ...

list_1 = []
list_2 = [None]
print(f"list_1: {bool(list_1)}")    # False
print(f"list_2: {bool(list_2)}")    # True

sum([1, 2, 3])      # 6

f = "qweqetrqaarty mncxz"
print(f"max: {max(f)}, min: {ord(min(f))}")
""" ----------------------------------------------------------
chr(i, /)
    Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.

ord(c, /)
    Return the Unicode code point for a one-character string.
"""
print()  # ----------------------------------------------------------


# lambda_1
g = lambda x, y, z: x + y * z
print(g(1, 2, 3), '\n')               # 7

# lambda_2
gl = [
    lambda x: pow(x, 0),
    lambda x: pow(x, 1),
    lambda x: pow(x, 2),
    lambda x: pow(x, 3),
    lambda x: pow(x, 4),
]

for i in gl:
    print(i(2))

print()


# -------
def h0(x): return pow(x, 0)
def h1(x): return pow(x, 1)
def h2(x): return pow(x, 2)
def h3(x): return pow(x, 3)
def h4(x): return pow(x, 4)


hh = [h0, h1, h2, h3, h4]
for i in hh:
    print(i(4))
