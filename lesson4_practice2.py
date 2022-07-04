#
# 1 --------------------------------------------------------- :
print('\n\n', '---' * 10, '4: practice1')

a = "Hello world"
result = ""
for char in a:
    if char == "o":
        result = result + "a"
    elif char == "l":
        result = result + "e"
    else:
        result = result + char

print(result)




#
# 2 --------------------------------------------------------- :
print('\n\n', '---' * 10, '4: practice2')

a = "Hello world"
print(a)
result2 = ""
i = 0

while i < len(a):
    i += 1
    if a[i] == "l":
        print(i)
        continue

    elif a[i] == "o":
        print(i)
        break


print('\n', '-------------------')
a = "Hello world"
print(a)
result2 = ""
i = 0

