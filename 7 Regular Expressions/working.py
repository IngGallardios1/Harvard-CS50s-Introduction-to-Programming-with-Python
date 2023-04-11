import re


def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        print("VALUE ERROR")


def convert(s):
    if matches := re.search(
        r"([0-1][0-2]|[0-9])(:[0-5][0-9]|) (AM|PM) to ([0-1][0-2]|[0-9])(:[0-5][0-9]|) (AM|PM)"
        , s):
        startH, startM, endH, endM = matches.group(1,2,4,5)

        # Make sure the hours be in 24 hour format
        if matches.group(3) == "PM":
            startH = str(int(startH) + 12)
        if matches.group(6) == "PM":
            endH = str(int(endH) + 12)

        # Make sure hours are 2 digits
        if len(startH) == 1:
            startH = "0" + startH
        if len(endH) == 1:
            endH = "0" + endH

        # Make sure to convert 24:00 to 00:00
        if startH == "24":
            startH = "00"
        if endH == "24":
            endH = "00"
        
        # Make sure minutes exists
        if startM == "":
            startM = ":00"
        if endM == "":
            endM = ":00"
        
        return f"{startH}{startM} to {endH}{endM}"
    raise ValueError
        

if __name__ == "__main__":
    main()