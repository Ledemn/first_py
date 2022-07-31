# Chapter 7. Reading Files
print('\n', '-----', 'Opening a File')  # ---------------
"""
! This is done with the open() function.

!! open() returns a "file handle" - a variable used to perform
operations on the file.

!!! Similar to "File -> Open" in Word Processor.

| handle = open(filename, mode) |
"""

fhand = open('main.py')
print(fhand)    # <_io.TextIOWrapper name='main.py' mode='r' encoding='UTF-8'>



#
print('\n\n', '-----', 'The Newline Character', '-----')  # ---------------
stuff = 'Hello\nWorld!'
print(stuff)
stuff = 'X\nY'
print(stuff)
print(len(stuff))   # Newline is still one character - not two.


#
print('\n\n', '-----', 'Reading Files in Python', '-----')  # ---------------
"""
! A file handle open for read can be treated as a sequence of
strings where each line in the file is a string in the sequence.

!! We can use the FOR statement to iterate through a sequence.

!!! Remember - a sequence is an ordered set.
"""

xfile = open('/home/s-li/Documents/disloc_info.txt')
for cheese in xfile:
    print(cheese)

print(type(xfile))



#
print('\n\n', '-----', 'Counting Lines in a File', '-----')  # ---------------
fhand = open('/home/s-li/mbox.txt')
count = 0
for line in fhand:
    count += 1
print('Line Count: ', count)



#
print('\n\n', '-----', 'Reading the *Whole* File', '-----')  # ---------------
# .read()
fhand = open('/home/s-li/mbox.txt')
inp = fhand.read()
print(len(inp))
print(inp[:65])



#
print('\n\n', '-----', 'Searching Through a File', '-----')  # ---------------
"""
We can put an IF statement in our FOR loop to only print
lines that meet some criteria.
"""



#
print('\n', '-----', '_', '-----')  # ---------------


#
print('\n', '-----', '_', '-----')  # ---------------


#
print('\n', '-----', '_', '-----')  # ---------------


#
print('\n', '-----', '_', '-----')  # ---------------

