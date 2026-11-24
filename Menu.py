pizzas = []
counts = []
costs = []
total_pizzas = 0

while True:
    print("\nМеню:")
    print("1. Вибрати піцу")
    print("2. Вихід")
    print("3. Показати замовлення")

    choice = input("Оберіть пункт: ")

    if choice == "1":
        print("Маргарита – 150 грн")
        print("Пепероні – 180 грн")
        print("Чотири сири – 200 грн")

        pizza = input("Введіть назву піци: ")
        if pizza == "Маргарита":
            price = 150
        elif pizza == "Пепероні":
            price = 180
        elif pizza == "Чотири сири":
            price = 200
        else:
            print("Такої піци немає!")
            continue

        count = int(input("Введіть кількість: "))
        if count <= 0:
            print("Кількість має бути більше 0!")
            continue

        if total_pizzas + count > 15:
            print("Загальна кількість піц не може бути більше 15!")
            continue

        cost = price * count
        total_pizzas = total_pizzas + count

        pizzas.append(pizza)
        counts.append(count)
        costs.append(cost)

        print("Замовлено", pizza + ",", count, "шт")
    elif choice == "2":
        print("До побачення!")
        break
    elif choice == "3":
        total_price = 0
        print("========== ВАШЕ ЗАМОВЛЕННЯ ==========")
        print("Піца            Кількість  Вартість")
        print("--------------------------------------")
        for i in range(len(pizzas)):
            print(f"{pizzas[i]:<15} {counts[i]:<10} {costs[i]} грн")
            total_price = total_price + costs[i]
        print("--------------------------------------")
        print("Загальна вартість:", total_price, "грн")
        print("======================================")
        print("Дякуємо за замовлення!")
    else:
        print("Невірний вибір")
