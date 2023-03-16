import sys
from PIL import Image, ImageOps


def get_argument():
    try:
        return sys.argv[1], sys.argv[2]
    except IndexError:
        print("Too few command-line arguments")
        sys.exit()


def check_image(file_name):
    return file_name[-4:] == ".png" or file_name[-5:] == ".jpeg" or file_name[-4:] == ".jpg"


def edit_photo(input, output):
    try:
        shirt = Image.open("shirt.png")
        with Image.open(input) as input:
            input_cropped = ImageOps.fit(input, shirt.size)
            input_cropped.paste(shirt, mask = shirt)
            input_cropped.save(output)
    except FileNotFoundError:
        sys.exit(f"Input does not exist")


def main():
    # Check for argument
    file_name, new_file_name = get_argument()
    
    # Check for image
    if not check_image(file_name):
        print("first argument, Not a image file")
        sys.exit()

    # Check for image
    if not check_image(new_file_name):
        print("second argument, Not a image file")
        sys.exit()

    # Check if both arguments have the same extension
    if file_name[-4:] != new_file_name[-4:]:
        print("Input and output have different extensions")
        sys.exit()
    else:
        edit_photo(sys.argv[1], sys.argv[2])
    

if __name__ == "__main__":
    main()