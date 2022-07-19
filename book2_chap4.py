# Book2: Chapter4. Cruising Massive Data with Dictionaries
# Producing a data dictionary
# Seeing how to loop through a dictionary
# Copying dictionaries
# Deleting items in a dictionary
# Using multi-key dictionaries

# Understanding Data Dictionaries  ---------------------------
"""
"htanaka"   = ["Haru Tanaka", 2000, 0, True]
"ppatel"    = ["Priya Patel", 2015, 1, False]

"ppatel"=   "full_name"         = "Priya Patel"
            "year_hired"        = 2000
            "dependents"        = 0
            "has_company_cell"  = True

Each dictionary entry having multiple keys is common in Python,
because the language makes it easy to isolate the specific item of data
you want using object.key syntax, like this:
ppatel.full_name = "Priya Patel"
ppatel.year_hired = 2015
ppatel.dependents = 1
ppatel.has_company_cell = True


The key name is more descriptive than using an index based on position,
as you can see in the following example.
ppatel[0] = 'Priya Patel'
ppatel[1] = 2015
ppatel[2] = 1
ppatel[3]=True
"""


#
# Creating a Data Dictionary  ---------------------------
# name = {key:value, key:value, key:value, key:value, …}
""" To make the code more readable, developers often place each key:value
pair on a separate line. But the syntax is still the same. The only
difference is that a line break follows each comma, as in the following:

name = {
    key:value,
    key:value,
    key:value,
    key:value,
    …
}

The ellipsis (…) just means that you can have as many key-value pairs as you want.
"""

people = {
    'htanaka': 'Haru Tanaka',
    'ppatel': 'Priya Patel',
    'bagarcia': 'Benjamin Alberto Garcia',
    'zmin': 'Zhang Min',
    'afarooqi': 'Ayesha Farooqi',
    'hajackson': 'Hanna Jackson',
    'papatel': 'Pratyush Aarav Patel',
    'hrjackson': 'Henry Jackson'
}


#
# Accessing dictionary data  ---------------------------
print(people, '\n')
"""
people.clear(       people.fromkeys(    people.items(       people.pop(         people.setdefault(  people.values(
people.copy(        people.get(         people.keys(        people.popitem()    people.update(
"""
# dictionaryname[key]
print(people['zmin'])   # “print people sub zmin”, where sub just means the specific key.
print()



#
# Getting the length of a dictionary  ---------------------------
# len(dictionaryname)
# Count the number of key:value pairs and put in a variable.
howmany = len(people)
print(howmany, '\n')



#
# Seeing whether a key exists in a dictionary  ---------------------------
print('hajackson' in people)
print('schmeedledorp' in people, '\n')



#
# Getting dictionary data with get()  ---------------------------
# dictionaryname.get(key)
# Python's nicer way of saying there is no schmeedledorp.
print(people.get('schmeedledorp', 'Unbeknownst to this dictionary'), '\n')



#
# Changing the value of a key  ---------------------------
# dictionaryname[key] = newvalue

# Print hajackson' current value.
print(people['hajackson'])
# Change the value of the hajackson key.
people['hajackson'] = "Hanna Jackson-Smith"
# Print the hajackson key to verify that the value has changed.
print(people['hajackson'])
print()



#
# Adding or changing dictionary data  ---------------------------
""" dictionaryname.update(key, value)

If the key you specify doesn't exist in the dictionary, it will be added as a new item with the value you specify.
If the key you specify does exist, nothing will be added.
The value of the key will be changed to whatever you specify as the value.
"""

# Make a data dictionary named people.
people = {
    'papatel': 'Pratyush Aarav Patel',
    'hrjackson': 'Henry Jackson',
    'zmin': 'Zhang Min'
}

# Change the value of the hrjackson key.
people.update({'hrjackson': 'Henrietta Jackson'})
print(people)

# Update the dictionary with a new key:value pair.
people.update({'wwigins': 'Wanda Wiggins'})
print(people)
print()

# Show what's in the data dictionary now.
for person in people.keys():
    print(person + " = " + people[person])
print()



#
# Looping through a Dictionary  ---------------------------
"""
If you just specify the dictionary name in the for loop, you get all the
keys, as follows:
"""
for person in people:
    print(person)
print()


"""
If you want to see the value of each item, keep the for loop the same,
but print dictionaryname[key] where dictionaryname is the name of
the dictionary (people in our example) and key is whatever name you
use right after the for in the loop (person, in the following example).
"""
for person in people:
    print(people[person])
print()


"""
You can also get all the names by using a slightly different syntax in the
for loop: Add .values() to the dictionary name, as in the following.
Then you can just print the variable name (person) inside the loop. The
output would be the full name of each person, as in the previous loop
example.
"""
for person in people.values():
    print(person)
print()


"""
Lastly, you can loop through the keys and values at the same time by
using .items() after the dictionary name in the for loop. But you will
need two variables after the for as well, one to reference the key and the
other to reference the value. If you want the code to display both
variables as it's looping through the dictionary, you’ll need to use those
names inside the parentheses of the print.
"""
# Looping through a dictionary with items() and two variable names.
for key, value in people.items():
    print(key, " = ", value)
# using two variable names, key and value (although they could be x and y or anything else)
print()



#
# Data Dictionary Methods  ---------------------------
"""
clear()         Empties the dictionary by remove all keys and values.
copy()          Returns a copy of the dictionary.
fromkeys()      Returns a new copy of the dictionary but with only specified keys and
                values.
get()           Returns the value of the specified key, or None if it doesn't exist.
items()         Returns a list of items as a tuple for each key-value pair.
keys()          Returns a list of all the keys in a dictionary.
pop()           Removes the item specified by the key from the dictionary, and returns
                its value.
popitem()       Removes the last key-value pair.
setdefault()    Returns the value of the specified key. If the key doesn't exist, inserts the
                key with the specified value.
update()        Updates the value of an existing key, or adds a new key-value pair if the
                specified key isn't already in the dictionary.
values()        Returns a list of all the values in the dictionary.
"""



#
# Copying a Dictionary  ---------------------------
"""
If you need to make a copy of a data dictionary to work with, use this
syntax:
newdictionaryname = dictionaryname.copy()
"""
