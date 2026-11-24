#Завдання 1
#Користувач вводить радіус кола. Потрібно обрахувати
#площу круга та вивести результат з двома знаками після коми.
#Розтавте команди нижче у правильному порядку та
#додайте підписи з описом що робить команда(є
#продовження на наступній сторінці)

pi = 3.1415
radius = float(input("Введіть радіус: "))
area = pi * radius ** 2
print(f"Площа кола: {area:.2f}")

#Завдання 2
#Користувач вводить ціну однієї кружки та загальний
#бюджет. Виведіть скільки кружок можна купити

price_of_one_cup = float(input("Введіть ціну однієї кружки:"))
budget = float(input("Введіть бюджет:"))

count = budget // price_of_one_cup

print(f"Можна купити: {count} кружки")

#Завдання 3
#Користувач вводить довжину в метрах. Виведіть цю
#довжину в футах та ярдах
METERS_TO_FEET = 3.28084
METERS_TO_YARDS = 1.09361
length_meters = float(input("Введіть довжину в метрах:"))

length_foot = length_meters * METERS_TO_FEET

length_yards = length_meters * METERS_TO_YARDS

print(f"Довжина в футах: {length_foot:.2f}")
print(f"Довжина в ярдах: {length_yards:.2f}")

#Завдання 4
#У завданні 2 виведіть ще залишок коштів

price_of_one_cup = float(input("Введіть ціну однієї кружки:"))
budget = float(input("Введіть бюджет:"))

count = budget // price_of_one_cup
remainder = budget % price_of_one_cup

print(f"Можна купити: {count} кружки")
print(f"Залишок (через %): {remainder}")

#Завдання 5
#Користувач вводить загальну кількість хвилин.
#Переведіть їх у години та хвилини.

total_minutes = int(input("Введіть кількість хвилин: "))

hours = total_minutes // 60
minutes = total_minutes % 60

print(f"Годин: {hours}")
print(f"Хвилин: {minutes}")
#Завдання 6
#Користувач вводить кількість яблук та молока(у літрах).
#Виведіть скільки він може спекти пирогів.
#Виведіть скільки яблук та молока залишиться.

APPLE_PER_PIE = 4
MILK_PER_PIE = 1.2

total_apples = int(input("Введіть кількість яблук:"))
total_milk = float(input("Введіть кількість молока (л): "))

pies_from_apples = total_apples // APPLE_PER_PIE
pies_from_milk = int(total_milk // MILK_PER_PIE)

pies_count = min(pies_from_apples, pies_from_milk)

remaining_apples = total_apples - (pies_count * APPLE_PER_PIE)
remaining_milk = total_milk - (pies_count * MILK_PER_PIE)

print(f"Можна спекти пирогів: {pies_count}")
print(f"Залишиться яблук: {remaining_apples}")
print(f"Залишиться молока: {remaining_milk:.1f}")
#Завдання 7
# вводить суму вкладу в банк та відсоток
#ставки.
#● Обчисліть скільки користувач отримує через 5 років,
#якщо кожного року сума вкладу збільшується на даний
#відсоток
#● Виведіть суму вкладу кожного року окремо
#nitial_deposit = float(input("Введіть суму вкладу:"))
#interest_rate = int(input("Введіть відсоток ставки:"))

# Вхідні дані
deposit = float(input("Введіть суму вкладу: "))
rate = float(input("Введіть відсоток ставки (%): "))

# 1 рік
deposit = deposit + (deposit * rate / 100)
print(f"Сума через 1 рік: {deposit:.2f}")

# 2 рік
deposit = deposit + (deposit * rate / 100)
print(f"Сума через 2 роки: {deposit:.2f}")

# 3 рік
deposit = deposit + (deposit * rate / 100)
print(f"Сума через 3 роки: {deposit:.2f}")

# 4 рік
deposit = deposit + (deposit * rate / 100)
print(f"Сума через 4 роки: {deposit:.2f}")

# 5 рік
deposit = deposit + (deposit * rate / 100)
print(f"Сума через 5 років: {deposit:.2f}")

#Завдання 8
#Користувач вводить кількість днів. Виведіть скільки це
#років, тижнів та днів.

count_of_days = int(input("Введіть кількість "))



