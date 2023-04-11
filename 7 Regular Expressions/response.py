from validator_collection import validators, checkers, errors


def validate_response(response):
    if checkers.is_email(response):
        return "Valid"
    return "Invalid"


def main():
    print(validate_response(input("Enter your email: ")))


if __name__ == '__main__':
    main()