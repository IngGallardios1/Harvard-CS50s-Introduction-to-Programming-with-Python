from tabulate import tabulate
import sys
import csv


def get_argument():
    try:
        return sys.argv[1]
    except IndexError:
        print("Too few command-line arguments")
        sys.exit()


def dotCSV(file_name):
    return file_name[-4:] == ".csv"


def main():
    # Check for argument
    file_name = get_argument()

    # Check for .csv
    if not dotCSV(file_name):
        print("Not a CSV file")
        sys.exit()
    
    # Initialize menu list
    menu = []

    # Lets try to open the file if there is one
    try:
        with open(f"{file_name}") as file:
            reader = csv.reader(file)
            for row in reader:
                menu.append(row)
    except FileNotFoundError:
        print("File does not exist")
        sys.exit()

    print(tabulate(menu, headers="firstrow", tablefmt="heavy_outline"))


if __name__ == "__main__":
    main()