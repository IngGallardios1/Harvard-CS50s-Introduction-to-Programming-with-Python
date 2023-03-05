import sys
from pyfiglet import Figlet
from random import choice

def main():
    if len(sys.argv) != 1 and len(sys.argv) != 3:
        sys.exit()

    s = input("Input: ")

    figlet = Figlet()

    if len(sys.argv) > 1:
        figlet.setFont(font=sys.argv[2])
    else:
        figlet.setFont(font=choice(figlet.getFonts()))
    
    print(figlet.renderText(s))


if __name__ == "__main__":
    main()