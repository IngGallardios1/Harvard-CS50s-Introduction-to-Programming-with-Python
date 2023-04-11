import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r"src=\"(https?://(www\.)?youtube.com/embed/xvFZjo5PgG0\")", s, re.IGNORECASE):
        return matches.group(1).replace("embed/", "")
    else:
        return None


if __name__ == "__main__":
    main()