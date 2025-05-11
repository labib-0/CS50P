import requests
import json
import sys

try:
    if len(sys.argv) == 2:
        try:
            amount_input = float(sys.argv[1])
            r = requests.get("https://api.coincap.io/v2/assets/bitcoin")
            dic = r.json()
            data = dic["data"]
            priceUsd = float(data["priceUsd"])
            amount = priceUsd * amount_input
            print(f"${amount:,.4f}")
        except ValueError:
            print("Command-line argument is not a valid number")
            sys.exit(1)
    elif len(sys.argv) < 2:
        print("Missing command-line argument")
        sys.exit(1)
    else:
        print("Command-line argument is not a valid number")
        sys.exit(1)
except requests.RequestException:
    sys.exit(1)
