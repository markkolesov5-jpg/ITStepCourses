# Завдання 1
# Напишіть програму для роботи онлайн магазину.
PRICE_PILLOW = 650
PRICE_BLANKET = 1700
PRICE_LAMP = 500
PRICE_KEYCHAIN = 60


qty_pillow = 0
qty_blanket = 0
qty_lamp = 0
qty_keychain = 0
print("--ТОВАРИ--")

print("Подушка - 650 грн")
print("Ковдра – 1700 грн")
print("Лампа – 500 грн")
print("брелок – 60 грн")

print("--МЕНЮ ДІЙ--")

print("1.Додати товар")
print("2.Видалити товар")
print("3.Очистити кошик")
print("4.Показати вміст кошики та суму покупки")
print("5.Вихід")

while True:
    choice = input("\nВиберіть номер дії (1-5): ")

    if choice == "1":
        product = input("Введіть назву товару (подушка, ковдра, лампа, брелок): ")

        if (
            product != "подушка"
            and product != "ковдра"
            and product != "лампа"
            and product != "брелок"
        ):
            print("Помилка: такого товару немає в асортименті.")
            continue

        quantity_str = input("Введіть кількість (від 1 до 10): ")

        if (
            quantity_str != "1"
            and quantity_str != "2"
            and quantity_str != "3"
            and quantity_str != "4"
            and quantity_str != "5"
            and quantity_str != "6"
            and quantity_str != "7"
            and quantity_str != "8"
            and quantity_str != "9"
            and quantity_str != "10"
        ):
            print("Помилка: введіть число від 1 до 10.")
            continue

        quantity = int(quantity_str)

        if product == "подушка":
            qty_pillow = qty_pillow + quantity
        elif product == "ковдра":
            qty_blanket = qty_blanket + quantity
        elif product == "лампа":
            qty_lamp = qty_lamp + quantity
        elif product == "брелок":
            qty_keychain = qty_keychain + quantity

        print("Успішно додано товар!")

    elif choice == "2":
        product = input(
            "Введіть назву товару для видалення (подушка, ковдра, лампа, брелок): "
        )

        if (
            product != "подушка"
            and product != "ковдра"
            and product != "лампа"
            and product != "брелок"
        ):
            print("Помилка: такого товару немає в асортименті.")
            continue

        quantity_str = input("Введіть кількість для видалення: ")

        if (
            quantity_str != "1"
            and quantity_str != "2"
            and quantity_str != "3"
            and quantity_str != "4"
            and quantity_str != "5"
            and quantity_str != "6"
            and quantity_str != "7"
            and quantity_str != "8"
            and quantity_str != "9"
            and quantity_str != "10"
        ):
            print("Помилка: введіть число від 1 до 10.")
            continue

        quantity = int(quantity_str)

        current_qty = 0
        if product == "подушка":
            current_qty = qty_pillow
        elif product == "ковдра":
            current_qty = qty_blanket
        elif product == "лампа":
            current_qty = qty_lamp
        elif product == "брелок":
            current_qty = qty_keychain

        if quantity > current_qty:
            print("Помилка: у кошику немає стільки такого товару.")
        else:
            if product == "подушка":
                qty_pillow = qty_pillow - quantity
            elif product == "ковдра":
                qty_blanket = qty_blanket - quantity
            elif product == "лампа":
                qty_lamp = qty_lamp - quantity
            elif product == "брелок":
                qty_keychain = qty_keychain - quantity
            print("Товар успішно видалено.")

    elif choice == "3":
        qty_pillow = 0
        qty_blanket = 0
        qty_lamp = 0
        qty_keychain = 0
        print("Кошик повністю очищено.")

    elif choice == "4":
        print("\n--- ВМІСТ ВАШОГО КОШИКА ---")
        total_sum = 0
        is_empty = True

        if qty_pillow > 0:
            cost = qty_pillow * PRICE_PILLOW
            print("Подушка:", qty_pillow, "шт. x", PRICE_PILLOW, "грн =", cost, "грн")
            total_sum = total_sum + cost
            is_empty = False

        if qty_blanket > 0:
            cost = qty_blanket * PRICE_BLANKET
            print("Ковдра:", qty_blanket, "шт. x", PRICE_BLANKET, "грн =", cost, "грн")
            total_sum = total_sum + cost
            is_empty = False

        if qty_lamp > 0:
            cost = qty_lamp * PRICE_LAMP
            print("Лампа:", qty_lamp, "шт. x", PRICE_LAMP, "грн =", cost, "грн")
            total_sum = total_sum + cost
            is_empty = False

        if qty_keychain > 0:
            cost = qty_keychain * PRICE_KEYCHAIN
            print(
                "Брелок:", qty_keychain, "шт. x", PRICE_KEYCHAIN, "грн =", cost, "грн"
            )
            total_sum = total_sum + cost
            is_empty = False

        if is_empty:
            print("Ваш кошик порожній.")
        else:
            print("ЗАГАЛЬНА СУМА ПОКУПКИ:", total_sum, "грн")

    elif choice == "5":
        print("Дякуємо, що скористалися нашим магазином!")
        break

    else:
        print("Помилка: вибрано неіснуючу дію. Введіть номер від 1 до 5.")
