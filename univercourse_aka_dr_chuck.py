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
print('\n', '-----', 'Looking at In...')  # ---------------
for i in [5, 4, 3, 2, 1]:
    print(i)


#
print('\n', '-----', 'Loop Idioms: ')  # through a Set -------
print('Before')
for thing in [9, 41, 12, 3, 74, 15]:
    print(thing)
print('After')



#
print('\n', '-----', 'Finding the largest value.')  # ---------------

largest_so_far = -1
print('Before:', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('After:', largest_so_far)

""" We make a variable that contains the largest value we have seen so far.
If the current number we are looking at is larger, it is the new largest
value we have seen so far.
"""



#
print('\n', '-----', 'Counting in a loop.')  # ---------------

zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork += 1
    print(zork, thing)
print('After', zork)



#
print('\n', '-----', 'Summing in a loop.')  # ---------------

zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + thing
    print(zork, thing)
print('After', zork)

""" To add up a value we encounter in a loop, we introduce a sum variable that
starts at 0 and we add the value to the sum each time through the loop.

Щоб додати значення, яке ми зустрічаємо в циклі, ми вводимо змінну суми,
яка починається з 0, і ми додаємо значення до суми кожного разу в циклі.
"""



#
print('\n', '-----', 'Finding the Average in a loop.')  # ---------------

count = 0
sum = 0
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count += 1
    sum = sum + value
    print(count, sum, value)
print(f"'After' {count} {sum} {sum / count:,.3f}")

""" An average just combines the counting and sum patterns and
divides when the loop is done. """



#
print('\n', '-----', 'Filtering in a Loop.')  # ---------------

print('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if value > 20:
        print('Large number', value)
print('After')

""" We use an if statement in the loop to catch/filter the values
we are looking for. """



#
print('\n', '-----', 'Search Using a Boolean Variable.')  # ---------------

found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
        print(found, value)
        break
    print(found, value)
print('After', found)

""" If we just want to search and know if a value was found, we use
a variable that starts at False and is set to True as soon as we find
what we are looking for. """



#
print('\n', '-----', 'Finding the smallest value.')  # ---------------

smallest = None     # It's like a marker. It's not empty, but it's a nothing!
print('Before', smallest)
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:    # is - stronger than equal(==)!
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)

print('After', smallest)

""" We still have a variable that is the smallest so far. The first time
through the loop smallest is None, so we take the first value to be the smallest. """



#
print('\n', '-----', 'The "is" and "is not" Operators.')  # ---------------
"""
a) Python has an IS operator that can be used in logical expressions.
b) Implies "is the same as"
c) Similar to, but stronger than "==":
    0 == 0.0 True
    0 is 0.0 False

d) IS NOT also is a logical operator.

We use them with Boolean and None (!)
"""
