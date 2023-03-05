import sys


def main():
    string = "Adieu, adieu, to "
    myList = []
    while True:
        try:
            name = input("Name: ")
        except EOFError:
            print()
            break
        myList.append(name)

    if len(myList) == 1:
        string += myList[0]
        print(string)
        sys.exit()
    elif len(myList) == 2:
        string += myList[0] + " and " + myList[1]
        print(string)
        sys.exit()
    else:
        for name in myList[:-2]:
            string += name + ", "
        string += myList[1] + " and " + myList[2]
        print(string)


if __name__ == "__main__":
    main()