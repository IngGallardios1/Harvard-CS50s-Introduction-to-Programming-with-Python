def main():
    fraction = input("Fraction: ")
    fuel = convert(fraction)
    print(gauge(fuel))


def convert(fraction):
    x, y = fraction.split("/")
    try:
        x = int(x)
        y = int(y)
        if x>y:
            raise ValueError
    except ValueError:
        pass
    try:
        fuel = (x/y)*100
    except ZeroDivisionError:
        pass
    return fuel


def gauge(percentage):
    if percentage < 1:
        return "E"
    elif percentage > 99:
        return "F"
    else:
        return f"{round(percentage)}%"


if __name__ == "__main__":
    main()