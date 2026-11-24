# Завдання 1
# Користувач вводить рядок та символ. Порахуйте скільки
# разів цей символ зустрічається у рядку.


# text = input("Введіть рядок:")
# symbol = input("Введіть символ:")
#
# print(f"Кількість входжень символу '{symbol}': {text.count(symbol)}")
#
#
#
# count = 0
# text = input("Введіть рядок:")
# symbol = input("Введіть символ:")
#
# for ch in text:
#     if ch == symbol:
#         count += 1
#
#
# print(f"Цей символ зустрівся {count} разів")

# Завдання 2
# Користувач вводить рядок. Виведіть наступну
# інформацію:
# ● кількість символів
# ● чи є там слово python
# ● кількість шиплячих літер – szh

# text = input("Введіть рядок: ")
#
# char_count = len(text)
# has_python = "python" in text
#
# sibilant_count = 0
# for ch in text:
#     if ch in "szhSZH":
#         sibilant_count += 1
#
# print(f"Кількість символів: {char_count}")
# print(f"Чи є слово python: {'Так' if has_python else 'Ні'}")
# print(f"Кількість літер s, z, h: {sibilant_count}")

# Завдання 3
# Користувач вводить тест. Потрібно замінити всі пробіли
# на дефіси. Виправіть помилку в коді

# text = input("Введіть текст: ")
#
# result = text.replace(" ", "-")
# print(f"Змінений текст: {result}")

# Завдання 4
# Користувач вводить рядок та слово. Порахуйте скільки
# разів це слово зустрічається у рядку.

# text = input("Введіть рядок: ")
# word = input("Введіть слово: ")
#
# words = text.split()
# count = words.count(word)
#
# print(f"Слово '{word}' зустрічається {count} разів")


# Завдання 5
# При оформлені посилки заборонено перевозити
# наступні речі:
# ● ножі
# ● гроші
# ● сильні отрути

items = input("Введіть ваші речі: ")
items = items.lower()

if "ніж" in items or "гроші" in items or "отрута" in items:
    print("У вас є речі які заборонено перевозити")
else:
    print("Оформлено доставку")
