def main():
    plate = input("Plate: ")
    
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    isNumber = False
    if len(s) >6 or len(s)<2:
        return False
    for i in range(len(s)):
        if not s[i].isalpha() and not s[i].isdigit():
            return False
        if i<2 and s[i].isdigit():
            return False
        if isNumber and s[i].isalpha():
            return False
        if i>=2 and s[i].isdigit():
            if not isNumber and s[i] == "0":
                return False
            isNumber = True
    return True


if __name__ == '__main__':
    main()