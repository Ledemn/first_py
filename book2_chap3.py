# Chapter 3: Speeding Along with Lists and Tuples
# Defining lists
# Working with lists
# Understanding tuples
# Checking out sets


# Defining and Using Lists  -------------------------------------------
scores = [88, 92, 78, 90, 98, 84]
students = ["Mark", "Amber", "Todd", "Anita", "Sandy"]
print(scores, students, "\n")


#
# Referencing list items by position  -------------------------------------------
# listname[x]
print(students[0])  # students[0] would be spoken as “students sub zero.”
print(scores[4], '\n')


#
# Looping through a list  -------------------------------------------
"""
for score in scores:
    print(score)
"""
for score in scores:
    print(score)
print("Done", '\n')



#
# Seeing whether a list contains an item  -------------------------------------------
# Is Anita in the list?
has_anita = "Anita" in students
print(has_anita)
has_bob = "Bob" in students
print(has_bob)



#
# Getting the length of a list  -------------------------------------------
print(len(students), '\n')



#
# Adding an item to the end of a list  -------------------------------------------
"""
use the .append() method with the value you want to add inside the parentheses.
The .append() method always adds to the end of the list.
"""
print(students)
# Add the name Goober to the list
students.append("Goober")
new_student = "Amanda"
print(students)
students.append(new_student)
print(students)

if new_student in students:
    print(new_student + " already in the list.", '\n\n')
else:
    students.append(new_student)
    print(new_student + " added to the list.", '\n\n')



#
"""  ----------------------------------------------------------
Inserting an item into a list:
listname.insert(position, item)
"""
# Create a list of strings (names).
students = ["Mark", "Amber", "Todd", "Anita", "Sandy"]
print(students)

student_name = "Lupe"
# Add student name to front of the list.
students.insert(0, student_name)

# Show me the new list.
print(students, '\n\n')



#
# Changing an item in a list:  -------------------------------------------
# listname[index] = newvalue
# Create a list of strings (names).
students = ["Mark", "Amber", "Todd", "Anita", "Sandy"]
students[3] = "Hobart"
print(students, '\n')



#
# Combining lists:  -------------------------------------------
# original_list.extend(additional_items_list)
# Create two lists of Names.
list1 = ["Zara", "Lupe", "Hong", "Alberto", "Jake"]
list2 = ["Huey", "Dewey", "Louie", "Nader", "Bubba"]
# Add list2 names to list1.
list1.extend(list2)
# Print list 1.
print(list1, '\n')



#
# Removing list items  -------------------------------------------
# remove() method
# Create a list of strings.
letters = ["A", "B", "C", "D", "C", "E", "C"]
"""
If you need to remove all of an item, you can use a while loop to repeat
the .remove as long as the item still remains in the list.

while "C" in letters:
    letters.remove("C")
"""
# Remove "C" from the list.
letters.remove("C")
# Show me the new list.
print(letters, '\n')


# Create a list of strings.
letters = ["A", "B", "C", "D", "E", "F", "G"]

# Make a copy of first list item then remove it from the list.
first_removed = letters.pop(0)
# Make a copy of last list item then remove it from the list.
last_removed = letters.pop()

# Show me the new list.
print(letters)
print(first_removed + " and " + last_removed + " were removed from the list.", '\n')


"""
Python also offers a del (short for delete) command that deletes any
item from a list based on its index number (position).
"""
# Create a list of strings.
letters = ["A", "B", "C", "D", "E", "F", "G"]
# Remove item sub 2.
del letters[2]          # "C"
print(letters, '\n')



#
# Clearing out a list  -------------------------------------------
# Create a list of strings.
letters = ["A", "B", "C", "D", "E", "F", "G"]
# Clear the list of all entries.
letters.clear()
# Show me the new list.
print(letters, '\n')



#
# Counting how many times an item appears in a list  ------------------
"""
listname.count(x)

When trying to combine numbers and strings to form a message,
you have to convert the numbers to strings using the str()
function.
"""



#
# Finding an list item's index  -------------------------------------------
""" .index() method:
listname.index(x)
"""
# Create a list of strings.
grades = ["C", "B", "A", "D", "C", "B", "C"]
# Decide what to look for
look_for = "F"
# See if the item is in the list.
if look_for in grades:
    print(str(look_for) + " is at index " + str(grades.index(look_for)))
else:
    # If not in the list, don't even try for index number.
    print(str(look_for) + " isn't in the list.", "\n")



#
# Alphabetizing and sorting lists  -------------------------------------------
"""
Python offers a sort() method for sorting lists. In its simplest form, it
alphabetizes the items in the list (if they’re strings). If the list contains
numbers, they’re sorted smallest to largest.

listname.sort()
"""
names = ["Zara", "Lupe", "Hong", "Alberto", "Jake", "Tyler"]
numbers = [14, 0, 56, -4, 99, 56, 11.23]

names.sort()
numbers.sort()

print(names)
print(numbers)
"""
If your list contains strings with a mixture of uppercase and
lowercase letters, and if the results of the sort don't look right, try
replacing .sort() with .sort(key=lambda s: s.lower()) and
then running the code again.
"""
