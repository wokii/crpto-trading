import requests


base_url = "https://api2.binance.com"

def get_url(api):
    return f"{base_url}{api}"


if __name__ == "__main__":
    ping_api = "/api/v3/ping"
    server_time_api = "/api/v3/time"
    exchange_info = "/api/v3/exchangeInfo"

    apis = [ping_api, server_time_api, exchange_info]

    for api in apis:
        print(f"sending request to {api}")
        x = requests.get(get_url(ping_api))

        print(x.json())