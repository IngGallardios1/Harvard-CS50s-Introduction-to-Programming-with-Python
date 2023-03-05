def validate_input(prompt):
    while True:
        x, y = input(prompt).split("/")
        try:
            x = int(x)
            y = int(y)
            return x, y
        except ValueError:
            pass


def main():
    while True:
        x, y = validate_input("Fraction: ")
        try:
            fuel = (x/y)*100
        except ZeroDivisionError:
            pass
        else:
            if fuel <= 100:
                break
    if fuel < 1:
        print("E")
    elif fuel > 99:
        print("F")
    else:
        print(f"{round(fuel)}%")


if __name__ == "__main__":
    main()