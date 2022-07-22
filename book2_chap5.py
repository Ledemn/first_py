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





print('------------------------------9')
# ------------------------------------------------------------


print('------------------------------10')
# ------------------------------------------------------------


print('------------------------------11')
# ------------------------------------------------------------
