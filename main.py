import requests

def get_crypto_price(symbol):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data.get(symbol, {}).get('usd', 'N/A')

if __name__ == "__main__":
    crypto = input("Enter the cryptocurrency ID (e.g., bitcoin, ethereum): ").lower()
    price = get_crypto_price(crypto)
    print(f"The current price of {crypto} is: ${price}")
