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


def main():
    items = []

    try:
        while True:
            user = input("Item: ").strip().title()
            if user in menu:
                items.append(user)
                print("Total:", total(items))
            else:
                print("Enter again")
    except EOFError:
        print("Total:", total(items))

def total(items):
    total = sum(menu[item] for item in items)
    return f"${total:.2f}"


if __name__ == "__main__":
    main()
