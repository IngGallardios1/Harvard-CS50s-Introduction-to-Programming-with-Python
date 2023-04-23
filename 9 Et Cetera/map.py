def main():
    yellMap("this", "is", "a", "test")
    yellListComprehension("this", "is", "a", "test")


def yellMap(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)


def yellListComprehension(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased) 


if __name__ == '__main__':
    main()