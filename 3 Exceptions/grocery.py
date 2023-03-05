def main():
    grocerys = {}
    while True:
        try:
            prompt = input("").upper()
        except EOFError:
            break
        if prompt in grocerys:
            grocerys[prompt] += 1
        else:
            grocerys[prompt] = 1
    for item in sorted(grocerys.keys()):
        print(grocerys[item], item)


if __name__ == "__main__":
    main()