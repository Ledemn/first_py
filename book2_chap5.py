# Book2: Chapter 5. Wrangling Bigger Chunks of Code
#
""" IN THIS CHAPTER
Creating your own function
Including a comment in a function
Seeing how to pass information to a function
Returning values from a function
Understanding anonymous functions
"""
print('------------------------------1')
# ------------------------------------------------------------


def hello():
    print('Hello')


hello()

print('------------------------------2')
# ------------------------------------------------------------


def hello():    # Practice function
    """ A docstring describing the function. """
    print('Hello')


hello()

print('------------------------------3')
# ------------------------------------------------------------


def hello(x):   # Practice function.
    """ A docstring describing the function. """
    print('Hello ' + x)


""" Generic names don't exactly help make your code easy to understand. It
would be better to use a more descriptive name, such as name or even
user_name, as in the following: """


def hello(user_name):   # Practice function
    """ A docstring describing the function """
    print('Hello ' + user_name)


"""
hello()     # TypeError: hello() missing 1 required positional argument: 'user_name'

For this particular function, a string needs to be passed. We know this
because we concatenate (add) whatever is passed into the variable to
another string (the word hello followed by a space). If you tried to
concatenate a number to a string, you'd get an error.


user_name = 1
type(user_name)     # <class 'int'>
hello(user_name)    # TypeError: can only concatenate str (not "int") to str
"""
hello('Alan')


print('------------------------------4')
# Defining optional parameters with defaults ---------------------------------
# The syntax follows: def functioname(parametername=defaultvalue):


def hello(user_name='nobody'):    # An optional parameter with a default value added to the hello() function.
    """ A docstring describing the function """
    print('Hello, ' + user_name)


hello('Silly')
hello()


print('------------------------------5')
# Passing multiple values to a function -----------------------------------


def hello(fname, lname, datestring):    # Practice function
    """ A docstring describing the function. """
    print('Hello ' + fname + ' ' + lname)
    print('The date is ' + datestring)


print('Alan', 'Wake', '21-07-2022')


def hello(fname, lname, datestring):    # Practice function
    """ A docstring describing the function. """
    msg = "Hello " + fname + " " + lname
    msg += " you mentioned " + datestring
    print(msg)


hello('Alan', 'Simpson', '12-01-2002')
print()


def hello(fname, lname, datestring=''):
    msg = 'Hello ' + fname + ' ' + lname
    if len(datestring) > 0:
        msg += ' you mentioned ' + datestring
        # print(msg)
    print(msg)


hello('Lana', 'Del', '00/00/00')    # 3
hello('Lana', 'Del')                # 2
""" Two examples of calling this version of the function.
The first call passes three values, and the second call passes only two.
Both work because the third parameter is optional.
"""


print('------------------------------6')
# Using keyword arguments (kwargs) ---------------------------------


def hello(fname='Alan', lname='Simpson', datestring='14/30/2001'):
    print(fname, lname, datestring)


hello()
hello(datestring='19/02/2000', lname='Simpson', fname='Aaron')

# The same concept applies if you pass variables:
apt_date = '12/30/2019'
last_name = 'Janda'
first_name = 'Kylie'
hello(datestring=apt_date, lname=last_name, fname=first_name)


print('------------------------------7')
# Passing multiple values in a list -------------------------------------
""" An iterable is anything that Python can loop through to get values.
A list is a simple and perhaps the most commonly used iterable.

The main trick to working with lists is this: If you want to alter the list
contents (for example, by sorting the contents), make a copy of the list in
the function and then make changes to the copy. You have to work with
a copy of the list that was passed because the function doesn’t receive
the original list in a mutable (changeable) format; it receives only a
pointer to the list, which indicates the list's location. Then the function
can get the list's contents. The function can do anything it likes with its
own copy of the list, but the original list remains unchanged.

After you have a copy of the list inside the function, you can sort that
copy using the simple sort() method. Or, if you want to sort in
descending order, use sort(reverse=True). """


def alphabetize(original_list=[]):  # ...
    """ Pass any list in square brackets, displays a string with items sorted. """
    # Inside the function make a working copy of the list passed in.
    """
    Because the function can't alter the list directly, it first makes a copy of
    the original list (the one that was passed) in a new list called
    sorted_list, with this line of code: """
    sorted_list = original_list.copy()

    # Sort the working copy.
    """ At this point, sorted_list isn't really sorted; it’s still just a copy of the
    original. """
    print(sorted_list, type(sorted_list))          # before .sort()

    """ The next line of code does the sorting: """
    sorted_list.sort()
    print(sorted_list, type(sorted_list))          # after .sort()

    # Make a new empty string for output.
    """ So the next line creates a new variable name, final_list and,
    after the = sign, starts the variable off as an empty string (two single
    quotation marks with no space between): """
    final_list = ''

    # Loop through sorted list and append name and comma and space.
    """ This loop loops through the sorted list and adds each item in the list,
    separated by a comma and a space, to the final_list string:
    """
    for name in sorted_list:
        final_list += name + ', '
        print(final_list, type(final_list))         # $: -v 8)

    # Knock off last comma and space if the string is not blank.
    """ When that’s done, if anything was added to final_list, it will have an
    extra comma and a space at the end. The following statement removes
    those last two characters, assuming the list is at least two characters in length:
    """
    final_list = final_list[:-2]
    # Print the alphabetized list.
    print(final_list, type(final_list))


al = list('qwertyuiop')
print(al, type(al), '\n')

alphabetize(al)
print()
alphabetize(['Schrepfer', 'Maier', 'Santiago', 'Adams'])
"""
As always, you can also pass in the name of a variable that contains the
list, as in this example:

names = ['Schrepfer', 'Maier', 'Santiago', 'Adams']
alphabetize(names)
"""
print()


print('------------------------------8')
# Passing in an arbitrary number of arguments -----------------------------


def sorter(*args):  # A function accepting any number of arguments with *args.
    """ Pass in any number of arguments separated by commas
    Inside the function, they treated as a tuple named args. """

    print(args, type(args))         # (1, 0.001, 100000, -900, 2) <class 'tuple'>

    # Create a list from the passed-in tuple.
    """ Whatever you pass in becomes a tuple named args inside the function.
    Remember, a tuple is an immutable list (a list you can't change). So
    again, if you want to change things, you need to copy the tuple to a list
    and then work on that copy. Here is an example where the code uses the
    simple statement: """
    new_list = list(args)

    """ You can read that as the variable named newlist
    is a list of all the things that are in the args tuple. """

    # Sort and show the list.
    """ The next line, newlist.sort() sorts the list, and print displays
    the contents of the list: """
    new_list.sort()
    print(new_list)


sorter(1, 0.001, 100_000, -900, 2)      # [-900, 0.001, 1, 2, 100000]


print('\n', '------------------------------9')
# Returning Values from Functions ------------------------------
""" So far, all our functions have displayed output on the screen so you can
make sure the function works. In real life, it's more common for a
function to return some value and put it in a variable specified in the
calling code. The line that does the returning is typically the last line of
the function followed by a space and the name of the variable (or some
expression) that contains the value to be returned.

Here is a variation of the alphabetize function. It contains no print
statement. Instead, at the end, it simply returns the alphabetized list
(final_list) that the function created: """


def alphabetize(original_list=[]):  # Printing a string returned by the alphabetize() function.
    """ Pass any list in square brackets,
    displays a string with items sorted. """

    # Inside the function make a working copy of the list passed in.
    sorted_list = original_list.copy()
    # Sort the working copy.
    sorted_list.sort()
    # Make a new empty string for output.
    final_list = ''
    # Loop through sorted list and append name and comma and space.
    for name in sorted_list:
        final_list += name + ', '
    # Knock off last comma space.
    final_list = final_list[:-2]
    # Return the alphabetized list.
    return final_list


""" The first line defines a variable called random_list,
which is just a list containing names in no particular order,
enclosed in square brackets (which tells Python it's a list). """
random_list = ['McMullen', 'Keaser', 'Maier', 'Wilson', 'Yudt', 'Gallagher', 'Jacobs']

""" The second line creates a new variable named alpha_list
by passing random_list to the alphabetize() function and
storing whatever that function returns. """
alpha_list = alphabetize(random_list)

""" The final print statement displays whatever is in the alpha_list variable: """
print(alpha_list)


print('\n', '------------------------------10')
# Unmasking Anonymous Functions --------------------------------
""" Python supports the concept of anonymous functions, also called lambda
functions. The anonymous part of the name is based on the fact that the
function doesn't need to have a name (but can have one if you want it
to). The lambda part is based on the use of the keyword lambda to
define anonymous functions in Python. In other words, when you see the
word lambda in Python code, that line of code is defining an anonymous
function.

lambda arguments : expression
"""

names = ['Adams', 'Ma', 'diMeola', 'Zandusky']
names.sort()
print(names)        # ['Adams', 'Ma', 'Zandusky', 'diMeola']
""" The reason diMeola comes after Zandusky is because
the sort is based on ASCII, which is a system in which each character is
represented by a number. All lowercase letters have numbers that are
higher than uppercase numbers.

the sort() method lets you include a key= expression inside the parentheses,
where you can tell it how to sort. The syntax is as follows:

.sort(key = transform)
"""
names.sort(key=len)
print(names)        # ['Ma', 'Adams', 'diMeola', 'Zandusky']


def lowercaseof(anystring):     # Putting a custom function named lowercaseof() to the test.
    """ Converts string to all lowercase """
    return anystring.lower(),\
           print(anystring.lower())  # print() is added for test


""" So now we have a custom function to convert any string to all
lowercase letters. How do we use that as a sort key? Easy. Use
key=transform the same as before, but replace transform with your
custom function name. Our function is named lowercaseof, so we'd use
.sort(key=lowercaseof), as shown in the following: """

names = ['Adams', 'Ma', 'diMeola', 'Zandusky']
# names.sort(key=lowercaseof())         # TypeError: lowercaseof() missing 1 required positional argument: 'anystring'
# names.sort(key=lowercaseof(names))    # AttributeError: 'list' object has no attribute 'lower'
names.sort(key=lowercaseof)

print(names)        # ['Adams', 'diMeola', 'Ma', 'Zandusky']
""" The displayed names are the same as before because only the sorting,
which took place behind the scenes, used lowercase letters.
The original data is still in its original uppercase and lowercase letters. """


"""
When your function can do its thing with a simple one-line expression
like that, you can skip the def and the function name and just use this
syntax:
lambda parameters : expression

Replace parameters with one or more parameter names that you make
up yourself (the names inside the parentheses after def and the function
name in a regular function). Replace expression with what you want
the function to return without the word return. So in this example, the
key, using a lambda expression, would be

lambda anystring: anystring.lower()

So the advantage of using the lambda expression is that you don’t even need
the external custom function. You just need the parameter followed by a colon and an
expression that tells it what to return.
"""
names = ['Adams', 'Ma', 'diMeola', 'Zandusky']
names.sort(key=lambda anystring: anystring.lower())     # Using a lambda expression as a sort key.
print('\n', names)


print('\n', '------------------------------11')
# lambda with names -----------------------------------------------
""" For example, here is a lambda function named currency that takes any
number and returns a string in currency format (that is, with a leading
dollar sign, commas between thousands, and two digits for pennies):
"""
currency = lambda c: f"${c:,.2f}"
print(currency(99))
print(currency(12345.456799))
print()


# Using a regular function.
def currency(c, w=15):
    """Show number in currency format with width."""
    c = f"${c:,.2f}"
    # Pad left of output with spaces to width of w.
    return c.rjust(w)


print(currency(123))


print('\n', '------------------------------12')
# lambda with names -----------------------------------------------
""" Here is one named percent that multiplies any number you send to it by
100 and displays it with two digits after the decimal point and a percent
sign at the end:
"""
percent = lambda p: f"{p:.2%}"
print(percent(0.065))
print(percent(.5))


# Using a regular function.
def percent(p):
    """Show number in percent format."""
    return f"{p:.1%}"
