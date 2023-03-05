def main():
    bandera = True
    months = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
    ]
    while bandera:
        user_input= input("Date: ")
        try:
            month, day, year = user_input.split("/")
            day = int(day)
            month = int(month)
        except ValueError:
            pass
        else:
            if (month > 0 and month <= 12) and (day > 0 and day <= 31):
                print(f"{year}-{month:02}-{day:02}")
                bandera = False
        try:
            month, day, year = user_input.split()
            day = day.replace(",", "")
            day = int(day)
        except ValueError:
            pass
        else:
            if month in months and day > 0 and day <= 31:
                month = months.index(month) + 1
                print(f"{year}-{month:02}-{day:02}")
                bandera = False


if __name__ == "__main__":
    main()