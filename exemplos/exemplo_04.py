import requests
import time
import logfire

CURRENCY = "BRL"
criptomoeda = ["SOL"]

def get_price(criptomoeda):
    prices = {}

    try:
        for criptomoeda in criptomoeda:
            url = f"https://api.coinbase.com/v2/prices/{criptomoeda}-{CURRENCY}/buy"
            prices[criptomoeda] = requests.get(url).json()["data"]["amount"]
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return {
            "prices": prices,
            "timestamp": timestamp
        }
    
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer requisição: {e}")
        return None

def transform_data(data):
    return data


if __name__ == "__main__":
    #logfire.log("Iniciando a aplicação", "INFO")
    data = get_price(criptomoeda)
    print(data)