import json
import requests
import sys

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=4ebdbffe41810cef127cd28c1b90cba1dc052372f8da801bbf7f7f1cb5bc2512")
    o = response.json()
    for data in o:
        price = data[priceUsd]
    arg = float(sys.argv[1])
    print(arg)
    amount = int(price) * arg
    print(f"{amount:,.4f}")
except requests.RequestException:
    print("")
except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)
except IndexError:
    print("Missing command-line argument")
    sys.exit(1)
