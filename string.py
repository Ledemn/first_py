name_1 = 'Це наш перший рядок'
name_2 = "Це наш другий рядок"
name_3 = 'Це наш "другий" рядок'
name_4 = "Це наш 'другий' рядок"

empty = ""

error_1 = "перше, друге, \" третє "
print(error_1)

print("друкуємо зворотній слеш - \\")
print("друкуємо символ табуляції - \t")
print("друкуємо символ табуляції - \\t")
print("друкуємо символ табуляції - d\td")

# name = input("введіть ім'я: ")
# print(f"ваше ім'я {name}")

raw_str = r'ааакпіуп \ аакппкеп'  # raw string
print(raw_str)

a = 'dddd ' + 'ffff'  # 1. складання рядків
print(a)
print("-" * 50)  # 2. множення рядків
print("--" * 25)  # 2. множення рядків

d = "Змінні та типи даних!"  # 3. входження рядків
result = 'та' in d  # булевий тип данних
print(result)
result = 'тe' in d  # булевий тип данних
print(result)

print(d[0])
print(d[1])
print(d[7])
# print(d[0], d[1], d[7])
print(d[-21])
print(d[-1])
print(d[2:12])  # slice нарізання. Діапазон; також працює в зворотньому порядку
print(d[2:12:3])  # slice нарізання. Тут :3 - крок (тобто кожен наступний)

s = "Символи нижнього регістру в верхній."
print(s.upper())