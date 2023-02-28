def interpreter(user_input):
    x = float(user_input.split(" ")[0])
    y = user_input.split(" ")[1]
    z = float(user_input.split(" ")[2])
    match y:
        case "+":
            return x+z
        case "-":
            return x-z
        case "*":
            return x*z
        case "/":
            return x/z
        case _:
            return 0


def main():
    user_input = input("Expression: ")
    print("{:.1f}".format(interpreter(user_input)))


if __name__ == "__main__":
    main()