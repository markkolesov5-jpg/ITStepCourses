
#name =  input("Введіть ваше ім'я")
#print("Ввів ім'я", name)
#age=45
#age = input("Введіть свій вік:")
#print("Ввів вік", age )
#age = int(age)
#Завдання Користувач вводить суму на рахунку в банку та суму
#покупки. Виведіть на екран залишок коштів
balance=1455.5
purchase=567.5
balance = float(input("Введіть суму на рахунку: "))
purchase = float(input("Введіть суму покупки: "))
print(balance - purchase)
#ЗавданняНапишіть програму яка запитує в користувача ціну
#однієї чашки кави(може бути з копійками) та кількість
#чашок.
price =57
quantity=4
price = float(input("Введіть ціну однієї чашки:"))
quantity= float(input("Введіть кількість чашок кави:"))
print(price*quantity)
#Завдання 3 Потрібно порахувати площу прямокутника. Але
#програма видає помилку
width=25
height=10
width_str=input("Введіть ширину")
height_str=input("Введіть довжину")
area=(width*height)
print("Площа дорівнює" , area)
width=int(width_str)
height=int(height_str)
#Ви обідаєте з друзями в ресторані і вирішуєте скільки
#залишити чайових.
#Користувач вводить суму рахунку та відсоток
#чайових(наприклад 10, 15 чи 20).
#Виведіть чайові та загальну суму на окремих рядках з
#підписами

bill = float(input("Введіть суму рахунку: "))
tip_percent = int(input("Введіть відсоток чайових: "))

tip = bill*tip_percent / 100
total = bill+tip


print("Чайові:", tip)
print("Загальна сума:", total)
bill=4500
tip_percent=30
#Завдання 5 Потрібно спланувати витрати на поїздку.
#Користувач вводить
#відстань в км
#витрати пального на 100 км в літрах
#ціна 1 л пального
#Виведіть на екран кількість пального та його ціну
dictance =float(input("Введіть відстань: "))
fuel_consumption=float(input("Введіть витрати пального на 100 км в літрах "))
fuel_price=float(input("Введіть цінy 1 л пального "))
fuel_amount=dictance*fuel_consumption/100
total_price=fuel_amount*fuel_price
print("Кількість пального:", fuel_amount, "л")
print("Загальна вартість пального:", total_price, "грн")
#Завдання 6 Користувач вводить два числа, програма повинна
#вивести суму, різницю та добуток. Але програма не працюєЗапустіть код. Самостійно виправте помилку
num1 = int(input("перше число: "))
num2 = int(input("друге число: "))
result = num1 + num2
result1 = num1 - num2
result2 = num1 * num2
print(result)
print(result1)
print(result2)
#Завдання 7 Ви вирішили покинути ресторан.
#У завданні 4 модифікуйте код так, щоб ще вводилась
#кількість людей і виводило на екран скільки має заплатити
#кожен(включно з чайовими)
bill = float(input("Введіть суму рахунку: "))
tip_percent = int(input("Введіть відсоток чайових: "))
people_count=int(input("Введіть кількість людей:"))

tip = bill*tip_percent / 100
total = bill+tip
amount_per_person =bill/people_count


print("Чайові:", tip)
print("Загальна сума:", total)
print("Сума на кожну людинк",amount_per_person)







