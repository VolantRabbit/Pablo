import requests

def get_exchange_rates():
    currency_code = input().strip().lower()
    url = f"http://www.floatrates.com/daily/{currency_code}.json"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        usd_data = data.get("usd")
        eur_rate = data.get("eur", {}).get("rate", None)

        if usd_data:
            print(usd_data)
        else:
            print("USD rate not available.")

        if eur_rate:
            print(f"Exchange rate for {currency_code.upper()} to EUR: {eur_rate}")
        else:
            print("EUR rate not available.")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    except ValueError:
        print("Error parsing JSON response.")

if __name__ == "__main__":
    get_exchange_rates()
