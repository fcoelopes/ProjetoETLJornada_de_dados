import requests
import time

CURRENCY = "USD"
criptomoeda = ["XRP"]

def get_price(criptomoeda):
    prices = {}

    for criptomoeda in criptomoeda:
        url = f"https://api.coinbase.com/v2/prices/{criptomoeda}-{CURRENCY}/buy"
        response = requests.get(url)
        prices[criptomoeda] = response.json()
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    return {
        "prices": prices,
        "timestamp": timestamp
    }


print(get_price(criptomoeda))