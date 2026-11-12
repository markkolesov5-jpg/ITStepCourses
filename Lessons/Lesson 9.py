#Завдання 1
#Користувач вводить число від 1 до 9. Потрібно вивести
#для цього числа таблицю множення.
#total_sum = 0
#while True:
   # n = int(input("Введіть число n: "))
    #if n < 0 or n > 10:
    #    print("Введене не правильне число")
        #continue
    #print(f"\nТаблиця множення для {n}:")
   # for i in range(1, 11):
        #print(f"{i}х{n}={i * n}")
# Завдання 2
# Користувач вводить свої оцінки поки не введе 0. Після
# чого програма виводить середню оцінку.
total = 0
count = 0

while True:
    grade = int(input("Введіть оцінку: "))

    if grade == 0:
        break

    total += grade
    count += 1

average_grade = total / count
print(f"середня оцінка: {average_grade}")

# Завдання 3
# Напишіть простий калькулятор

print("1. Сума")
print("2. Різниця")
print("3. Добуток")
print("4. Частка")
print("5. Вихід")

num_1 = float(input("Введіть перше число: "))
num_2 = float(input("Введіть друге число: "))

while True:
    command = int(input("Виберіть номер команди: "))

    if command == 5:
        print("Програма завершена")
        break

    if command == 1:
        result = num_1 + num_2
        print(f"Сума = {result}")
        continue

    if command == 2:
        result = num_1 - num_2
        print(f"Різниця = {result}")
        continue

    if command == 3:
        result = num_1 * num_2
        print(f"Добуток = {result}")
        continue

    if command == 4:
        if num_2 == 0:
            print("Помилка: ділення на нуль неможливе!")
        else:
            result = num_1 / num_2
            print(f"Частка = {result}")
        continue

    print("Невідома команда! Виберіть число від 1 до 5.")


# Завдання 4
# Програма повинна зареєструвати рівно 3 учасників. Для
# цього користувач вводить їхні імена, але ім’я admin уже
# зайняте.

count = 0

while count < 3:
    name = input("Введіть ім'я: ")

    if name == "admin":
        print("Це ім'я недоступне")
        continue

    count += 1
    print(f"Учасник №{count}: {name}")



