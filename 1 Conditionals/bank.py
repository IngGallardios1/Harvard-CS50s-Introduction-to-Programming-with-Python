def main():
    users_input = input("Greeting: ").lower()

    if users_input[:5]=="hello":
        print("$0")
    elif users_input[0]=="h":
        print("$20")
    else:
        print("$100")


if __name__ == "__main__":
    main()