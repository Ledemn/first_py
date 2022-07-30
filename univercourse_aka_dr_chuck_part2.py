# Chapter 6. Strings
print('\n', '-----', 'String Data Type')  # ---------------
str1 = "Hello"
str2 = 'there'
bob = str1 + str2
print(bob)


str3 = '123'
# str3 += 1       # TypeError: can only concatenate str (not "int") to str
""" We can convert numbers in a string into a number using int() """
x = int(str3) + 1
print(x)


#
print('\n', '-----', 'Reading and Converting')  # ---------------
"""
We prefer to read data in using strings and then parse
(робити граматичний аналіз) and convert the data as we need.

This gives us more control over error situations and/or
bad user input.

Raw input numbers must be converted from strings.
"""
# name = input('Enter: ')
# print(name)
# apple = input('Enter: ')
# x = apple - 10  # TypeError: unsupported operand type(s) for -: 'str' and 'int'
# x = int(apple) - 10
print(x)


#
print('\n', '-----', 'Looking Inside Strings')  # ---------------
fruit = 'banana'
letter = fruit[1]   # means "fruit sub-one"
print(letter)       # a

x = 3
w = fruit[x - 1]    # 3-1=2 == fruit[2] == 'ba[n]ana'
print(w)            # n



#
print('\n', '-----', 'A Character Too Far')  # ---------------
"""
! Tou will get a python error if you attempt to index
beyond the end of a string:

zot = 'abc'
print(zot[5])       # IndexError: string index out of range

!! So be careful when constructing index values and slices.
"""



#
print('\n', '-----', 'Strings Have Length')  # ---------------
# The built-in function len gives us the length of a string.
fruit = 'banana'
print(len(fruit))




#
print('\n', '-----', 'Len Function')  # ---------------
fruit = 'banana'
x = len(fruit)
print(x)
"""
A function is a some stored code that we use. A function
takes some input and produces an output.

'banana'(a string) ---> len() function ---> 6 (a number)
"""



#
print('\n', '-----', 'Looping Through Strings: While')  # ---------------
"""
Using a while statement and an iteration variable, and the len
function, we can construct a loop to look at each of the letters
in a string individually.
"""
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index += 1



#
print('\n', '-----', 'Looping Through Strings: For')  # ---------------
"""
A define loop using a FOR statement is much more elegant.
The iteration variable is completely taken care of by the FOR loop.
"""
fruit = 'banana'
for letter in fruit:
    print(letter)
print()



#
print('\n', '-----', 'Looping And Counting: For')  # ---------------
"""
This is a simple loop that loops through each letter in a string
and counts the number of times the loop encounters the 'a' character.
"""
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count += 1
print(count)



#
print('\n', '-----', 'Looking Deeper Into IN')  # ---------------
"""
The iteration variable "iterates" through the sequence (ordered set).

| iteration variable - letter               |
| sequence/six-character string - 'banana'  |

The block(body) of code is executed once for each value in the sequence.

The iteration variable moves through all of values in the sequence.
"""
print('...')



#
print('\n', '-----', 'String Comparison')  # ---------------
if word == 'banana':
    print('All right, bananas.')


if word < 'banana':
    print('Your word,' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word,' + word + ', comes after banana.')
else:
    print('All right, bananas.')



#
print('\n', '-----', 'String Library')  # ---------------
greet = 'Hello Bob'
zap = greet.lower()
print(zap)
print(greet)
print('Hi There'.lower())

fruit = 'banana'
pos = fruit.find('na')      # ba[na]na
print(pos)                  # [2]

aa = fruit.find('z')
print(aa)                   # -1

greet = 'Hello Bob'
nnn = greet.upper()         # HELLO BOB
print(nnn)
print()

greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Jane')
print(nstr)
nstr = greet.replace('o', 'X')
print(nstr)

"""
lstrip() and rstrip() remove whitespace
at the left or right.

strip() removes both beginning and ending whitespace.
"""
greet = '     Hello Bob     '
print(greet.lstrip())       # 'Hello Bob     '
print(greet.rstrip())       # '     Hello Bob'
print(greet.strip())        # 'Hello Bob'

# Prefixes
line = 'Please have a nice day'
print(line.startswith('Please'))    # True
print(line.startswith('P'))         # True
print(line.startswith('p'))         # False
print()


# Parsing and Extracting
data = 'We found 10 new job offers matching your criteria. <no-reply@justjoin.it>'
jobpos = data.find('job')
print(jobpos)               # 16
atpos = data.find('@')
print(atpos)                # 60
dotpos = data.find('.')
print(dotpos)               # 49
host = data[dotpos+2:]      # <no-reply@justjoin.it>
print(host)
