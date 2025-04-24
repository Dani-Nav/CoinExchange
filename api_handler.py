import requests

def get_exchange_rate(base: str, target: str) -> float:
    base = base.upper()
    target = target.upper()

    url = f"https://open.er-api.com/v6/latest/{base}"
    response = requests.get(url)
    data = response.json()

    if data.get("result") != "success":
        raise ValueError("Erro ao acessar a API de câmbio.")

    rates = data.get("conversion_rates", {})
    if target not in rates:
        raise ValueError(f"Moeda de destino '{target}' não encontrada.")

    return rates[target]
