"""
Написати прогу, яка визначає яким є число - парним чи непарним.
Якщо залишок від ділення на 2 не дорівнює 0, це непарне число;
якщо дорівнює - парне.
"""

number = float(input("Введіть число: "))

# додати перевірку некоректних данних.
# .isdigit()

if number % 2:
    print("Непарне")
else:
    print("Парне")
