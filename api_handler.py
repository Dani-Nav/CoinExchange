import requests
import streamlit as st

def get_exchange_rate(base: str, target: str) -> float:
    url = f"https://open.er-api.com/v6/latest/{base}"
    response = requests.get(url)
    data = response.json()

    st.write(data)  # só durante o debug

    if data.get('result') != 'success':
        raise ValueError("Erro ao acessar a API de câmbio.")

    rates = data.get('conversion_rates', {})
    target = target.upper()  # ✅ garantir que está em MAIÚSCULO

    if target not in rates:
        raise ValueError(f"Moeda de destino '{target}' não encontrada.")

    return rates[target]
