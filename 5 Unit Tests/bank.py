def main():
    users_input = input("Greeting: ")
    print(value(users_input))

def value(greeting):
    if greeting[:5].lower()=="hello":
        return "$0"
    elif greeting[0].lower()=="h":
        return "$20"
    else:
        return "$100"


if __name__ == "__main__":
    main()