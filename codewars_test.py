print("Find the smallest integer in the array")
""" ---------------------------------
def findSmallestInt(arr):
    #sort array
    arr.sort()
    return arr[0]
"""


def findSmallestInt(arr):
    return min(arr)


# ---------------------------------------------------------
print('\n', "Expressions Matter")
""" -------------------------------------------------

Given three integers a ,b ,c, return the largest number obtained after inserting the following operators
and brackets: +, *, ().
In other words, try every combination of a,b,c with [*+()], and return the Maximum Obtained

1 !!!!!!
def expression_matter(a, b, c):
    return max(a*b*c, a+b+c, (a+b)*c, a*(b+c))


2 --------------
def expression_matter(a, b, c):
    cases = [a + b + c]
    cases.append(a * b * c)
    cases.append((a * b) + c)
    cases.append((a + b) * c)
    cases.append(a + (b * c))
    cases.append(a * (b + c))
    return max(cases)
"""


def expression_matter(a, b, c):
    result1 = a * (b + c)
    result2 = a * b * c
    result3 = a + b * c
    result4 = (a + b) * c
    result5 = a + b + c
    result = [result1, result2, result3, result4, result5]

    return max(result)  # highest achievable result


print(expression_matter(1, 2, 3))





# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------








## print('\n', "KataTrain <8kyu> | Parse nice int from char problem")
"""  ---------------------------------
You ask a small girl,"How old are you?"
She always says, "x years old", where x is a random number between 0 and 9.

Write a program that returns the girl's age (0-9) as an integer.

Assume the test input string is always a valid string.
For example, the test input may be "1 year old" or "5 years old".
The first character in the string is always a number.


def get_age(age):
    #your code here

"""
