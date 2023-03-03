def shortenString(s):
    newString = ""
    vowels = "aeiou"
    for character in s:
        if character not in vowels:
            newString += character
    return newString


def main():
    s = input("Input: ")
    print("Output:", shortenString(s))


if __name__ == '__main__':
    main()