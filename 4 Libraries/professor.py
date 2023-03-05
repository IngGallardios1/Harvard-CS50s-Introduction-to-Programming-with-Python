import random


def main():
    level = get_level(input("Level: "))
    xlist, ylist, resultList = generate_integer(level)
    score = 0
    for i in range(10):
        lives = 3
        out = True
        while lives > 0 and out:
            try:
                guess = int(input(f"{xlist[i]} + {ylist[i]} = "))
            except ValueError:
                print("EEE")
                lives -= 1
            else:
                if guess == resultList[i]:
                    score += 1
                    out = False
                else:
                    print("EEE")
                    lives -= 1
            if lives == 0:
                print(f"{xlist[i]} + {ylist[i]} = {resultList[i]}")    
    print(f"Score: {score}")



def get_level(s):
    try: 
        if int(s) < 4 and int(s) > 0:
            return int(s)
        else:
            return get_level(input("Level: "))
    except ValueError:
        return get_level(input("Level: "))



def generate_integer(level):
    xlist = []
    ylist = []
    resultList = []
    if level == 1:
        for i in range(10):
            xlist.append(random.randint(1,9))
            ylist.append(random.randint(1,9))
            resultList.append((xlist[i]+ylist[i]))
    elif level == 2:
        for i in range(10):
            xlist.append(random.randint(10,99))
            ylist.append(random.randint(10,99))
            resultList.append((xlist[i]+ylist[i]))
    else:
        for i in range(10):
            xlist.append(random.randint(10,99))
            ylist.append(random.randint(10,99))
            resultList.append((xlist[i]+ylist[i]))
    return xlist, ylist, resultList


if __name__ == "__main__":
    main()