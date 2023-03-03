def camelFunc(s):
    snake = ""
    for character in s:
        if character.isupper():
            snake += "_" + character.lower()
        else:
            snake += character
    return snake


def main():
    s = input("camelCase: ")
    print("snake_case:", camelFunc(s))


if __name__ == '__main__':
    main()