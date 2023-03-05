from random import randint
import sys

def main():
    while True:
        level = input("Level: ")
        try:
            target = randint(1,int(level))
            break
        except ValueError:
            pass
    while True:
        guess = input("Guess: ")
        try:
            guess = int(guess)
        except ValueError:
            pass
        else:
            if guess > target:
                print("Too large!")
            elif guess < target:
                print("Too small!")
            else:
                print("Just right!")
                sys.exit()


if __name__ == "__main__":
    main()
    