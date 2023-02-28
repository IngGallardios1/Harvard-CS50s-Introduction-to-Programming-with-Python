def identify(user_input):
    str = user_input.split(".")[1]
    match str:
        case "gif" | "jpg" | "jpeg" | "png":
            return "image/"+str
        case "pdf" | "txt" | "zip":
            return "file/"+str
        case _:
            return "Unknown type"

def main():
    user_input = input("File name: ")
    print(identify(user_input))


if __name__ == "__main__":
    main()