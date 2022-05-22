print(10)
print(0b01001111001101)  # 0b...

# >>> type(10)
# <class 'int'>

# >>> 1_000
# 1000

# >>> 3.5
# 3.5
# >>> type(3.5)
# <class 'float'>

# >>> 0.1 + 0.2
# 0.30000000000000004

# >>> type(3+6j)
# <class 'complex'>

# >>> a = True
# type(a)
# <class 'bool'>

# >>> empty = ''
# >>> full = 'fafggggsge'
# >>> bool(empty)
# False
# >>> bool(full)
# True

# >>> bool(0)
# False
# >>> bool(-25)
# True

# None - спец.тип данних. Визначає нічого!
# >>> type(None)
# <class 'NoneType'>
# >>> None == 0
# False

lines = """
LPIC-1 is the first certification
in the multi-level Linux professional certification program
of the Linux Professional Institute (LPI).
The LPIC-1 will validate the candidate's ability
to perform maintenance tasks on the command line,
install and configure a computer running Linux and configure basic networking.
"""  # """ - дозволяють переносити довгі тексти на кілька рядків.
a = lines.splitlines()
print(a)

line_2 = "LPIC-1 is the first certification"
print(line_2.upper())

result = "LPIC" in line_2.upper()
print(result)
