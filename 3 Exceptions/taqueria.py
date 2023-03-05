def taqueria(key):
    menu = {
                "Baja Taco": 4.00,
                "Burrito": 7.50,
                "Bowl": 8.50,
                "Nachos": 11.00,
                "Quesadilla": 8.50,
                "Super Burrito": 8.50,
                "Super Quesadilla": 9.50,
                "Taco": 3.00,
                "Tortilla Salad": 8.00
            }
    return menu.get(key.title())


def main():
    total = 0.00
    while True:
        prompt = input("Item: ")
        try:
            total += taqueria(prompt)
        except TypeError:
            break
        print(f"Total: ${total:.2f}")


if __name__ == "__main__":
    main()