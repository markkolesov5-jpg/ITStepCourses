while True:
    print("Меню:")
    print("1. Вибрати піцу")
    print("2. Вихід")

    choice = input("Оберіть пункт: ")

    if choice == "1":
        print("Ціни на піцу:")
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
        print("Замовлено", pizza + ",", count, "шт")
    elif choice == "2":
        print("До побачення!")
        break
    else:
        print("Невірний вибір")
