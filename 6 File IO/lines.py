import sys

def get_argument():
    try:
        return sys.argv[1]
    except IndexError:
        print("Too few command-line arguments")
        sys.exit()


def dotPy(file_name):
    return file_name[-3:] == ".py"


def get_lines(file):
    line_count = 0
    for row in file:
        if row:
            if not row.startswith("#"):
                line_count += 1
    return line_count



def main():
    # Check for argument
    file_name = get_argument()
    
    # Check for .py
    if not dotPy(file_name):
        print("Not a Python file")
        sys.exit()

    # Python file list
    python_file = []

    # Try to open the file if there is one
    try:
        with open(f"{file_name}") as file:
            for line in file:
                python_file.append(line.lstrip().rstrip())
    except FileNotFoundError:
        print("File does not exist")
        sys.exit()
    
    # Print lines
    print(get_lines(python_file))


if __name__=="__main__":
    main()