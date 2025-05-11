menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

menu_lower = {}
total = 0
for key, value in menu.items():
    menu_lower[key.lower()] = value
while True:
    try:
        get = input("Item: ").lower()
        total += menu_lower[get]
        print(f"total: ${total:.2f}")

    except KeyError:
        pass
    except EOFError:
        print(f"total: ${total:.2f}")
        break
