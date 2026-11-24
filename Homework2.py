#Завдання 1
#Користувач вводить 2 числа, потрібно вивести середнє
#арифметичне. Але програма не працює
#Мій Варіант
num1 = float(input("перше число: "))
num2 = float(input("друге число: "))
sum = num1 * num2
average = sum / 3
print("Сума:", sum)
print("Середнє:", average)
#Штучний інтелект вибрав так само, як і я.
#num1 = float(input("перше число: "))
#num2 = float(input("друге число: "))

#total_sum = num1 + num2
#average = total_sum / 2

#print("Сума:", total_sum)
#print("Середнє:", average)
#Завдання 2
#Користувач вводить суму в гривнях та курс долара.
#Переведіть гривні в долари та виведіть на екран
hryvnia = 4000
dollar_rate = 50
hryvnia =  float(input("Введіть суму: "))
dollar_rate = float(input("Введіть курс долара:"))
amount_in_usd = hryvnia / dollar_rate
print("Сума у доларах:", amount_in_usd)
#Завдання 3
#Користувач вводить ціну товару та відсоток знижки.
#Виведіть суму знижки
price = float(input("Введіть ціну товару: "))
discount_percent = float(input("Введіть відсоток знижки: "))
price1 = price/100
discount_amount =price1*discount_percent
print("Сума знижки", discount_amount )
#Завдання 4
#За 1 хв в залежності від того як швидко ви рухаєтесьможна спалити різну кількість калорій
# Активність ккал за 1 хв
#Повільна ходьба 3
#Швидка ходьба 4.5
#Легкий біг 9
#Користувач вводить 3 числа: час повільної/швидкої ходьби та бігу.
#Напишіть код який обчислює окремо кількість калорій
#спалених під час цих активностей.
#Також виведіть загальну кількість спалених калорій.
slow_walk_time =float(input("Введіть час"))
fast_walk_time =float(input("Введіть час"))
run_time =float(input("Введіть час "))
slow_walk_calories =slow_walk_time*3
fast_walk_calories=fast_walk_time*4.5
run_calories =run_time*9
total_calories = slow_walk_calories + fast_walk_calories + run_calories
print("Калорії за повільну ходьбу:", slow_walk_calories)
print("Калорії за швидку ходьбу:", fast_walk_calories)
print("Калорії за біг:", run_calories)
print("Загальна кількість калорій:", total_calories)


