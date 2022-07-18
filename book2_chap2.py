# Chapter 2: Controlling the Action
# Making Decisions with if  -----------------------------
# The result of a simple if when the condition proves true:
sun = "down"
if sun == "down":
    print("Good night!")    # Good night!
print("I'm here.", '\n')    # I'm here.


# Result of simple if when the condition proves false:
sun = "up"
if sun == "down":
    print("Good night!")
print("I'm here.", '\n')    # I'm here.


total = 100
sales_tax_rate = 0.065
taxable = True
if taxable:
    print(f"Subtotal: ${total:.2f}")
    sales_tax = total * sales_tax_rate
    print(f"Sales Tax: ${sales_tax:.2f}")
    total = total + sales_tax
print(f"Total: ${total:.2f}", '\n')


# if condition:
#   do indented lines here
#   ...
# else:
#   do indented lines here
#   ...
# do remaining un-indented lines no matter what

# Print an initial greeting based on the time of day:
import datetime as dt
now = dt.datetime.now()
if now.hour < 12:
    print("Good morning")
else:
    print("Good afternoon")
print("I hope you are doing well!", '\n')


#
# Handling multiple else statements with elif.
light_color = "green"
if light_color == "green":
    print("Go")                                     # Go
elif light_color == "red":
    print("Stop")
print("This code executes no matter what", '\n')    # This code executes no matter what


#
# Ternary operations.
age = 31
if age < 21:
    beverage = "milk"
elif age >= 21 and age < 80:
    beverage = "beer"
else:
    beverage = "prune juice"
print(f"Have a {beverage.title()}.", '\n')


#
# Repeating a Process with for
""" --------------------------------------------------------
With for, you generally get a fixed number of loops,
one for each item in a range or one for each item in a list.
------------------------------------------------------------

Looping through numbers in a range

for x in range(y):
   do this
   do this
   ...
un-indented code is executed after the loop"""
for x in range(1, 11):
    print(x)
print("All done.", '\n')


#
# Looping through a string
"""Using range() in a for loop is optional. You can replace range with a
string, and the loop repeats once for each character in the string.

for x in string
    do this
    do this
    …
do this when the loop is done
"""
for x in "snorkel":
    print(x)
print("Done.", '\n')


#
# Looping through a list
for x in ["The", "rain", "in", "Spain"]:
    print(x)
print("Done", '\n')


#  -----------------------------
# Bailing out of a loop:    blank - adjective (EMPTY)
"""
for x in items:
    if condition:
    [do this … ]
    break
do this
"""
answers = ["A", "C", "B", "D"]
for answer in answers:
    if answer == "":
        print("Incomplete")
        break
    print(answer)
print("Loop is done", '\n')


answers = ["A", "C", "", "D"]           # ""
"""
the third item in the list is blank, as indicated by "",
which is an empty string
"""
for answer in answers:
    if answer == "":
        print("Incomplete")             # ""
        break
    print(answer)
print("Loop is done", '\n')



#
# Looping with continue  -----------------------------
answers = ["A", "C", "", "D"]
for answer in answers:
    if answer == "":
        print("Incomplete")
        continue
    print(answer)
print("Loop is done", '\n\n')



#
# Nesting loops  -----------------------------
for outer in ["First", "Second", "Third"]:
    print(outer)
    # Inner loop
    for inner in range(3):
        print(inner + 1)

print("Both loops are done", '\n\n')



#
# Looping with while
""" ------------------------------------------------------------------------------
With a while loop, the loop keeps going as long as (while) some condition is true.
----------------------------------------------------------------------------------
while condition:
    do this …
    do this …
do this when the loop is done
"""
counter = 65
while counter < 91:
    print(str(counter) + "=" + chr(counter))
    counter += 1
print("All done.", "\n\n")



#
# Starting while loops over with continue
import random
print("Odd numbers")
counter = 0
while counter < 10:
    # Get a random number
    number = random.randint(1, 999)
    if int(number / 2) == number / 2:
        # If it's an even number, don't print it.
        continue
    # Otherwise, if it's odd, print it and increment the counter.
    print(number)
    # Increment the loop counter.
    counter += 1
print("Loop is done.", "\n")


"""
------------ My Version ------------
"""
import random
print("Odd numbers:")
counter = 0
while counter < 10:
    # Get a random number
    number = random.randint(1, 999)
    if number % 2 == 0:
        # If it's an even number, don't print it.
        continue
    # Otherwise, if it's odd, print it and increment the counter.
    print(f"counter_{counter + 1} is {number}")
    # Increment the loop counter.
    counter += 1
print("Loop is done.", "\n\n")



#
# Breaking while loops with break  -----------------------------
"""
while condition1:
    do this
    …
    if condition2:
        break
do this when the loop is done
"""
import random
print("Numbers that aren't evenly divisible by 5")
counter = 0
while counter < 10:
    # Get a random number
    number = random.randint(1, 999)
    if int(number / 5) == number / 5:
        # If it's evenly divisible by 5, bail out.
        break
    # Otherwise, print it and keep going for a while.
    print(number)
    # Increment the loop counter.
    counter += 1
print("Loop is done", "\n")
