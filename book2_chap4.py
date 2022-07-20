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
# Define a dictionary named people.
people = {
    'htanaka': 'Haru Tanaka',
    'zmin': 'Zhang Min',
    'afarooqi': 'Ayesha Farooqi',
}
# Make a copy of the people dictionary and put it in peeps2.
peeps2 = people.copy()

print(people)
print(peeps2)
print()



#
# Deleting Dictionary Items  ---------------------------
"""
You can remove data from data dictionaries in several ways. The del
keyword (short for delete) can remove any item based on its key. The
syntax is as follows:

del dictionaryname[key]
"""
# Define a dictionary named people.
people = {
    'htanaka': 'Haru Tanaka',
    'zmin': 'Zhang Min',
    'afarooqi': 'Ayesha Farooqi',
}

# Show original people dictionary.
print(people)

# Remove zmin from the dictionary.
del people["zmin"]

# Show what's in people now.
print(people)
print()

"""
If you forget to include a specific key with the del keyword and specify
only the dictionary name, the entire dictionary is deleted, even its name.
"""
del people
# print(people)   # NameError: name 'people' is not defined


"""
To remove all key-value pairs from a dictionary without deleting the
entire dictionary, use the clear method with this syntax:

dictionaryname.clear()

The following code creates a dictionary named people, puts some key-
value pairs in it, and then prints the dictionary so you can see its content.
Then, people.clear() empties all the data:
"""
# Define a dictionary named people.
people = {
    'htanaka': 'Haru Tanaka',
    'zmin': 'Zhang Min',
    'afarooqi': 'Ayesha Farooqi',
}
# Show original people dictionary.
print(people)
# Remove all data from the dictionary.
people.clear()
# Show what's in people now.
print(people)
print()


"""
The pop() method offers another way to remove data from a data
dictionary. The pop() method actually does two things:

1>> If you store the results of the pop() method in a variable, that
variable gets the value of the popped key.
2>> Regardless of whether you store the result of the pop() method in a
variable, the specified key is removed from the dictionary.
"""
people = {
    'htanaka': 'Haru Tanaka',
    'zmin': 'Zhang Min',
    'afarooqi': 'Ayesha Farooqi',
}
# Show original people dictionary.
print(people)


# Popping an item from a dictionary.
adios = people.pop("zmin")
""" adios = people.pop("zmin") is executed, putting
the value of the zmin key in a variable named adios. We then print the
adios variable so we can see that it contains Zhang Min, the value of the
zmin key.
"""
# Print the contents of adios and people.
print(adios)
""" Printing the entire people dictionary again proves that "zmin"
has been removed from the dictionary:
"""
print(people)
print()


"""
Data dictionaries offer a variation on pop() that uses this syntax:
dictionaryname = popitem()
"""
# Define a dictionary named people.
people = {
    'htanaka': 'Haru Tanaka',
    'zmin': 'Zhang Min',
    'afarooqi': 'Ayesha Farooqi',
    'bagarcia': 'Benjamin Alberto Garcia',
}
print(people)
people.popitem()    # popitem() always removes the last key-value pair.
print(people)
print()



#
# Having Fun with Multi-Key Dictionaries  ---------------------------
"""
For example, suppose that just knowing the person’s full name isn’t
enough. You want to also know the year the person was hired, his or her
date of birth, and whether or not that employee has been issued a
company laptop. The dictionary for any one person might look like this:
"""
employee = {
    'name': 'Haru Tanaka',
    'year_hired': 2005,
    'dob': '11/23/1987',
    'has_laptop': False
}
"""
Or suppose you need a dictionary of products that you sell. For each
product, you want to know its name, its unit price, whether or not it’s
taxable, and how many you currently have in stock. The dictionary
might look something like this (for one product):
"""
product = {
    'name': 'Ray-Ban Wayfarer Sunglasses',
    'unit_price': 112.99,
    'taxable': True,
    'in_stock': 10,
    # The value for a property can be a list, tuple, or set;
    # it doesn't have to be a single value.
    'models': ['Black', 'Tortoise']
}

"""
You can use the simple dictionaryname[key] syntax to print just the value of each
key. For example, using that last product example, the output of this code:
"""
print(product['name'])
print(product['unit_price'])
print(product['taxable'])
print(product['in_stock'])
print(product['models'])
print('\n')


print('Name:    ', product['name'])
print('Price:   ', f"${product['unit_price']:.2f}")
print('Taxable: ', product['taxable'])
print('In Stock:', product['in_stock'])
print('Models:  ')
for model in product['models']:
    print(' ' * 10 + model)

print('\n\n')



#
# Using the mysterious fromkeys and setdefault methods  ------------------
"""
Data dictionaries in Python offer two methods, named fromkeys() and
setdefault(), which are the cause of much head-scratching among
Python learners — and rightly so because it's not easy to find practical
applications for their use. But we’ll take a shot at it and at least show
you what to expect if you ever use these methods in your code.
"""

# The fromkeys() method uses this syntax:
# newdictionaryname = dict.fromkeys(iterable[,value])
"""
Replace the iterable part with any iterable — meaning, something the
code can loop through; a simple list will do. The value part is optional.
If omitted, each key in the dictionary gets a value of None, which is
simply Python's way of saying no value has been assigned to this key in
this dictionary yet.
"""
DWC001 = dict.fromkeys(['name', 'unit_price', 'taxable', 'in_stock', 'models'])
print(DWC001)
# {'name': None, 'unit_price': None, 'taxable': None, 'in_stock': None, 'models': None}


# Create a generic dictionary for products named product.
product = {
    'name': '',
    'unit_price': 0,
    'taxable': True,
    'in_stock': 0,
    'models': []
}
print(product)
# Create a dictionary named DWC001 that has the same keys as product.
DWC001 = dict.fromkeys(product.keys())
# Show what's in the new dictionary.
print(DWC001)
"""
The final print() statement shows what's in the new dictionary. You can
see it has all the same keys as the product dictionary, with each value
set to None:

{'name': None, 'unit_price': None, 'taxable': None, 'in_stock': None, 'models': None}
"""
print()


""" -----------------------------------------------------------------
The .setdefault() value lets you add a new key to a dictionary, with a
predefined value. But .setdefault() only adds a new key and value; it
doesn't alter the value for an existing key, even if that key's value is
None. So it could come in handy after the fact if you defined other
dictionaries and then later wanted to add another property:value pair
only to dictionaries that don't already have that property.
"""
# Create a generic dictionary for products named product.
product = {
    'name': '',
    'unit_price': 0,
    'taxable': True,
    'in_stock': 0,
    'models': []
}
print(product)


# Experimenting with fromkeys and setdefault.
DWC001 = dict.fromkeys(product.keys())
print(DWC001)

DWC001.setdefault('taxable', True)
DWC001.setdefault('models', [])
DWC001.setdefault('reorder_point', 100)

"""
The taxable key in that output, though, is still None,
because setdefault won't change the value of an existing key.
It adds a new key with the default value to a dictionary only if
it doesn't already have that key.

The simple solution would be to use the standard syntax,
dictionaryname[key] = newvalue to change the value of the
extant taxable key from None to True.
"""
DWC001['taxable'] = True
print(DWC001)
print()



#
# Nesting dictionaries  ---------------------------
"""
containingdictionaryname = {
    key: {dictionary},
    key: {dictionary},
    key: {dictionary},
    …
}
"""
products = {
    'RB00111': {'name': 'Ray-Ban Sunglasses', 'price': 112.98, 'models': ['black', 'tortoise']},
    'DWC0317': {'name': 'Drone with Camera', 'price': 72.95, 'models': ['white', 'black']},
    'MTS0540': {'name': 'T-Shirt', 'price': 2.95, 'models': ['small', 'medium', 'large']},
    'ECD2989': {'name': 'Echo Dot', 'price': 29.99, 'models': []}
}
print(products)
