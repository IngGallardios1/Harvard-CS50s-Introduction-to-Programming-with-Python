import sys
import csv


def get_argument():
    try:
        return sys.argv[1], sys.argv[2]
    except IndexError:
        print("Too few command-line arguments")
        sys.exit()


def dotCSV(file_name):
    return file_name[-4:] == ".csv"


def main():
    # Check for argument
    file_name, new_file_name = get_argument()
    
    # Check for .csv
    if not dotCSV(file_name):
        print("first argument, Not a CSV file")
        sys.exit()

    if not dotCSV(new_file_name):
        print("second argument, Not a CSV file")
        sys.exit()

    students = []

    try:
        with open(f"{file_name}") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                house = row["house"]
                last, fisrt = row["name"].split(", ")
                students.append({"first": fisrt, "last": last, "house": house})
    except FileNotFoundError:
        print("File does not exist")
        sys.exit()

    with open(f"{new_file_name}", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in students:
            writer.writerow(row)


if __name__ == "__main__":
    main()