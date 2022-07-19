# Book2: Chap3. Tuples and Sets
#
# What's a Tuple and Who Cares?  -------------------------------------------
"""
a tuple is just an immutable list (like that tells you a lot).
In other words, a tuple is a list, but you can’t change
it after it’s defined.

The syntax for creating a tuple is the same as the syntax for creating a
list, except you don’t use square brackets. You have to use parentheses,
like this:
"""
prices = (29.95, 9.98, 4.95, 79.98, 2.95)
print(len(prices))
print(prices.count(4.95))
print(4.95 in prices)
print()

# Loop through and display each item in the tuple.
for price in prices:
    print(f"${price:.2f}")
print()

# You can't change the value of an item in a tuple using this kind of syntax:
# prices[1] = 234.56    TypeError: 'tuple' object does not support item assignment
"""
Any method that alters, or even just copies, data in a list causes an error
when you try it with a tuple. So the list methods .append(), .clear(),
.copy(), .extend(), .insert(), .pop(), .remove(), .reverse(), and
.sort() would fail when working with tuples. In short, a tuple makes
sense if you want to show data to users without giving them any means
to change any of the information.
"""


#
# Working with Sets  --------------------------------------
"""
The difference between a set and a list is that the items in a set have no specific order.
Even though you may define the set with the items in a certain order,
none of the items get index numbers to identify their position.
"""
sample_set = {1.98, 98.9, 74.95, 2.5, 1, 16.3}
# You can add a single new item to a set using .add()
sample_set.add(11.23)

"""
You can also add multiple items to a set using .update(). But the items
you're adding should be defined as a list in square brackets, as in the
following example:
"""
sample_set.update([88, 123.45, 2.98])
print(sample_set)

# Make a copy and show the copy.
ss2 = sample_set.copy()
print(ss2)
print(len(ss2))
print()

print("Loop through set and print each item right-aligned and formated.")
for s in ss2:
    print(f"{s:>6.2f}")

"""
Lists and tuples are two of the most commonly used Python data
structures. Sets don’t seem to get as much play as the other two, but it’s
good to know about them. A fourth — and widely used — Python data
structure is the data dictionary, which you learn about in the next
chapter.
"""
