"""
Написати прогу, яка визначає тварину.
Якщо "Meow" - кіт, якщо "Bark" - пес,
i якщо інший звук - "Unknown animal".
"""

sound = input("Звір, дай ГОЛОС!: ")
# змінити залежність від регістру та мови

if sound == "Meow":
    print("Кіт")
elif sound == "Bark":
    print("Пес")
else:
    print("Unknown animal")
