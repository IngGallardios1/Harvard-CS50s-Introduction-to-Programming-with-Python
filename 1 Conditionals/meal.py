def main():
    user_input = input("What time is it? ")
    print(convert(user_input))


def convert(time):
    hours = int(time.split(":")[0])
    if hours <= 8 and hours >= 7:
        return "breakfast time"
    elif hours <= 13 and hours >= 12:
        return "lunch time"
    elif hours <= 19 and hours >= 18:
        return "dinner time"
    else:
        return ""


if __name__ == "__main__":
    main()