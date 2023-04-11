import re


def main():
    print(count(input("Text: ")))

# Count of um in text
def count(s):
    if matches := re.findall(r"\bum\b", s, re.IGNORECASE):
        return len(matches)
    return 0


if __name__ == "__main__":
    main()