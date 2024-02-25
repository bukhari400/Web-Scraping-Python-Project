import requests

def fetch_ohlcv():
    url = "https://rest.coinapi.io/v1/ohlcv/BINANCE_SPOT_ETH_BTC/history?period_id=1MTH&time_start=2023-03-01T00:00:00"
    headers = { "X-CoinAPI-Key": "8ad531c1-9185-4c5f-9c12-786e5e6280bd" }  # Replace with your API key

    response = requests.get(url, headers=headers)

    # Check if the response is successful
    if response.status_code == 200:
        if response.content:
            return response.json()
        else:
            print("Response is empty.")
            return None
    else:
        # Handle other HTTP status codes
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None
    
print(fetch_ohlcv())