def main():
    s = input("Input: ")
    print("Output:", shorten(s))


def shorten(word):
    newString = ""
    vowels = "aeiouAEIOU"
    for character in word:
        if character not in vowels:
            newString += character
    return newString


if __name__ == "__main__":
    main()