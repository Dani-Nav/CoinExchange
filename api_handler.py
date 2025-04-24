import requests

def get_exchange_rate(base: str, target: str) -> float:
    url = f"https://api.exchangerate.host/latest?base={base}&symbols={target}"
    response = requests.get(url)
    data = response.json()
    return data['rates'][target]
