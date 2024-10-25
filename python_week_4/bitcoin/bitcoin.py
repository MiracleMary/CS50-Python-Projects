import requests
import sys

def get_bitcoin():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        return data["bpi"]["USD"]["rate_float"]
    except requests.RequestException as e:
        print(e)
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        print("command line is not a number")
        sys.exit(1)

    bitcoin_price = get_bitcoin()
    total = bitcoins * bitcoin_price
    print(f"${total:,.4f}")


if __name__ == "__main__":
    main()
