from datetime import date, datetime
import inflect
import sys


def main():
    # Get date of birth from the user
    user_birth = get_date(input("Enter your date of birth (YYYY-MM-DD): "))

    minutes = get_minutes(user_birth)

    # Print the number of minutes using inflect lybrary
    p = inflect.engine()
    time_to_words = p.number_to_words(minutes, andword="")
    print(f"{time_to_words} minutes")


def get_date(date):
    try:
        return datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        sys.exit("Invalid date format")


def get_minutes(date):
    # Get today´s date
    today = date.today()

    # Get difference between today and date of birth
    difference = today - date

    # Get the number of minutes between today and date of birth
    minutes = round(difference.total_seconds() / 60)

    return minutes


if __name__ == "__main__":
    main()