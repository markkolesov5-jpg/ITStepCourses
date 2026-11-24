#Каса кінотеатру розраховує вартість квитка в залежності
#від віку користувача:
#Вік <12
#Ціна квитка 80 грн
#12-65 65+
#200 грн 120 грн
#Користувач вводить свій вік, виведіть вартість квитка.
#Також програма в кінці повинна побажати гарного дня.
PRICE_CHILD = 80
PRICE_ADULT = 200
PRICE_SENIOR = 120
age = int(input("Введіть свій вік:"))

if age < 12:
    print(f"Ціна вашого квитка {PRICE_CHILD} грн")
    print("Бажаємо вам гарного дня")

elif 12 <= age <= 65:
    print(f"Ціна вашого квитка {PRICE_ADULT} грн")
    print("Бажаємо вам гарного дня")

elif age > 65:
    print(f"Ціна вашого квитка {PRICE_SENIOR} грн")
    print("Бажаємо вам гарного дня")

#Завдання 2
#Інший розробник намагався написати програму яка
#автоматично визначає категорію товару за її вагою, але
#програма завжди видає “Дрібна посилка”
#Виправіть проблему

weight = float(input("Введіть вагу товару в кг: "))

if weight < 1:
        print("Дрібна посилка")
elif weight < 5:
        print("Середня посилка")
elif weight < 10:
        print("Велика посилка")
else:
    print("Надважка посилка")

#Завдання 3
#Користувач вводить назву місяця та число. Потрібно
#вивести яке сьогодні свято.
#Якщо сьогодні звичайний день то так і сказати
#користувачу.
#див наступну сторінку
NEW_YEAR = "1 січня"
VALENTINES_DAY = "14 лютого"
CHRISTMAS = "25 грудня"
APRIL_FOOLS_DAY = "1 квітня"
date = input("Введіть назву місяця та число:")

if date == NEW_YEAR:
    print("Новий рік")

elif date == VALENTINES_DAY:
    print("День св. Валентина")

elif date == CHRISTMAS:
    print("Різдво")

elif date == APRIL_FOOLS_DAY:
    print("День сміху")

else:
    print("Сьогодні звичайний день")

#Завдання 4
#У завданні 1 треба купити білети трьом людям.
#Змініть код таким чином щоб можна було ввести три
#числа(вік трьох людей) та вивести скільки коштує білет
#для кожної людини окремо.
#Також вивести загальну суму.
PRICE_CHILD = 80
PRICE_ADULT = 200
PRICE_SENIOR = 120

age1 = int(input("Введіть вік першої людини: "))
age2 = int(input("Введіть вік другої людини: "))
age3 = int(input("Введіть вік третьої людини: "))

price1 = 0
price2 = 0
price3 = 0

if age1 < 12:
    price1 = PRICE_CHILD
elif 12 <= age1 <= 65:
    price1 = PRICE_ADULT
else:
    price1 = PRICE_SENIOR

if age2 < 12:
    price2 = PRICE_CHILD
elif 12 <= age2 <= 65:
    price2 = PRICE_ADULT
else:
    price2 = PRICE_SENIOR

if age3 < 12:
    price3 = PRICE_CHILD
elif 12 <= age3 <= 65:
    price3 = PRICE_ADULT
else:
    price3 = PRICE_SENIOR

total_sum = price1 + price2 + price3

print(f"Вартість квитка для 1-ї людини: {price1} грн")
print(f"Вартість квитка для 2-ї людини: {price2} грн")
print(f"Вартість квитка для 3-ї людини: {price3} грн")
print(f"Загальна сума до сплати: {total_sum} грн.")
print("Гарного дня!")



#Завдання 5

product = input("Введіть назву товару: ")


if product == "алкоголь" or product == "тютюн":
    # Введення віку покупця
    age = int(input("Введіть ваш вік: "))

    if age >= 18:
       print("Дозволено до продажу")
    else:
       print("Заборонено до продажу")


elif product == "ліки":

    prescription = input("У вас є рецепт від лікаря? ")

    if prescription == "так":
       print("Дозволено до продажу")
    else:
       print("Заборонено до продажу")


else:
   print("Дозволено до продажу")