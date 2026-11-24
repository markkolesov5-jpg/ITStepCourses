#Завдання 1
#Користувач вводить свій вік, якщо він працездатного
#віку(18-65) то виведіть фразу «Працездатний/на», інакше
#«Непрацездатний/на»


age = int(input("Введіть свій вік: "))

if 18 <= age <= 65:
    print("Працездатний/на")

else:
    print("Непрацездатний/на")
#Завдання 2
#До завдання 2 з попереднього заняття добавте додаткову
#перевірку: щоб отримати доступ користувач повинен ще й
#ввести правильний логін secret_login = "AliBaba"
#correct_password =  "OpenSesame123"
correct_password =  "OpenSesame123"

correct_login = "AliBaba"

entered_password = input("Введіть пароль: ")

entered_login = input("Ввеідіть логін:")

if entered_password == correct_password and correct_login:
    print("Доступ дозволено")

else:
    print("Доступ заблоковано")
#Завдання 3
#Оформіть чек покупки. Користувач вводить ціну за
#одиницю товару, кількість товару та свій вік.
#Якщо користувач неповнолітній або старший за 65
#років, то застосуйте знижку 15%
age = int(input("Введіть свій вік:"))

price = float(input("Введіть ціну товару:"))

quantity = int(input("Введіть кількість товару:"))

total = price * quantity

if age < 18 or age > 65:
  discount = total * 0.15
  final_amount = total - discount
  print("\n--- ЧЕК ---")
  print(f"Сума без знижки: {total:.2f} грн")
  print(f"Знижка (15%): {discount:.2f} грн")
  print(f"До сплати: {final_amount:.2f} грн")
else:
  final_amount = total
  print("\n--- ЧЕК ---")
  print(f"До сплати: {final_amount:.2f} грн")
#Завдання 4
#Орендувати авто можна лише якщо
#● у вас є ліцензія
#● ви повнолітні
#● ви не потрапляли в дтп
#Оцініть якість написаного коду, спробуйте його
#спростити використавши and\or

has_license = "так"
accidents = "ні"
age = float(input('Введіть свій вік:'))
has_license = input("Чи маєте ви ліцензію?")
accidents = input('Ви потрапляли в інседенти?')
if age >= 18 or has_license or accidents:
    print("Оренда дозволена")

else:
    print("Оренда заборонена")

#Завдання 5
#В службі доставки діє акційна пропозиція, чи дорожча
#покупка тим більша знижка на доставку
purchase_price = float(input("Введіть ціну покупки: "))

base_delivery = 120.0

if purchase_price < 500:
  delivery_discount = 0.0

elif 500 <= purchase_price <= 1000:
  delivery_discount = 0.05

elif 1000 < purchase_price <= 2000:
  delivery_discount = 0.20

else:
  delivery_discount = 1.0


delivery_cost = base_delivery * (1 - delivery_discount)

total_cost = purchase_price + delivery_cost


print(f"Ціна доставки: {delivery_cost:.2f} грн")

print(f"Загальна вартість (покупка + доставка): {total_cost:.2f} грн")








