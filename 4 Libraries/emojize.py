from emoji import emojize


def main():
    users_input = input("Input: ")
    emoji = emojize(users_input, language="en")
    print(f"Output: {emoji}")


if __name__ == "__main__":
    main()