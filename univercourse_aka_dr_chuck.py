# try / except to compensate for errors
print('-----' * 5, '1')

astr = 'Hello Bob'
try:
    istr = int(astr)    # conversion!
except:
    istr = -1
print('First', istr)


print('-----' * 5, '2')  # -------------------------
astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print('Second', istr)
print()

"""
print('-----' * 5, '3')  # -------------------------

rawstr = input('Enter a number: ')
try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0:
    print('Nice work.')
else:
    print('Not a number')
"""


print('-----' * 5, 'Functions. Chapter 4')  # -------------------------

x = 5
print('Hello')


def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')


print('Yo')
x += 2
print(x)


def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')


greet('en')
greet('es')
greet('fr')

print('-----' * 3, 'Return Values:')
""" Often a function will take its arguments, do some computation, and
return a value to be used as the value of the function call in the
calling expression. The return keyword is used for this. """


def greet():
    return "Hello"


print(greet(), "Glenn")
print(greet(), "Sally")
print()


""" A "fruitful" function is one that produces a result
(or return value)

The return statement ends the function execution and
"sends back" the result of the function.
"""


def greet2(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'


print(greet2('en'), 'Glenn')
print(greet2('es'), 'Sally')
print(greet2('fr'), 'Michael')
print()


def addtwo(a, b):
    added = a + b
    return added


print(addtwo(3, 5))


print('-----' * 3, 'Breaking Out of a Loop')
"""
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')


while True:
    line = input('(to quit print "q")> ')
    if line[0] == '#':
        # if the first character is a pound sign, skip it and go to top of Loop.
        continue
    elif line == '\r':   # carriage return / enter ?????
        continue
    elif line == 'q':
        break
    print(line)
print('Done!')
print()
"""

# A Simple Definite Loop
for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff!')

print()  # 2

friends = ['Joe', 'Glenn', 'Sally']
for friend in friends:
    print('Bye,', friend)
print('Done!')
print()


print('-----' * 2, 'Just a test:')


def find_smallest_int(arr):
    # Code here
    return min(arr)


a2 = [34, -345, -1, 100]
print(find_smallest_int(a2))
print()


#
print('-----' * 2, ':')  # ---------------
