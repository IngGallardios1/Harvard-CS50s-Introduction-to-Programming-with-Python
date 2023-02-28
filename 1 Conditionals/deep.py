def main():
    users_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
    match users_input:
        case "42":
            print("Yes")
        case "Forty Two":
            print("Yes")
        case "forty-two":
            print("Yes")
        case _:
            print("No")


if __name__ == "__main__":
    main()