import requests

def get_exchange_rate(base: str, target: str) -> float:
    url = f"https://open.er-api.com/v6/latest/{base}"
    response = requests.get(url)
    data = response.json()

    if data['result'] != 'success':
        raise ValueError("Erro ao acessar a API de câmbio.")

    if target not in data['conversion_rates']:
        raise ValueError(f"Moeda de destino '{target}' não encontrada.")

    return data['conversion_rates'][target]
