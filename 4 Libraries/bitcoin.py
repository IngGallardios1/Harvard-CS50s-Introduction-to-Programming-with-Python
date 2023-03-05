import requests
import sys


def main():
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit()
    else:
        try:
            bitcoin = float(sys.argv[1])
        except ValueError:
            print("Command-line argument is not a number")
            sys.exit()
    
    try:
        coinDesks = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        print("Ups")
        sys.exit()
    else:
        coinDesks = coinDesks.json()
        usdPrice = coinDesks["bpi"]["USD"]["rate_float"]
        amount = usdPrice * bitcoin
        print(f"${amount:,.4f}")
        

if __name__ == "__main__":
    main()
