import requests
import streamlit as st

def get_exchange_rate(base: str, target: str) -> float:
    url = f"https://open.er-api.com/v6/latest/{base}"
    response = requests.get(url)
    data = response.json()

    st.write(data)  # 👈 ISSO VAI MOSTRAR A RESPOSTA NA TELA DO APP

    if data.get('result') != 'success':
        raise ValueError("Erro ao acessar a API de câmbio.")

    if target not in data.get('conversion_rates', {}):
        raise ValueError(f"Moeda de destino '{target}' não encontrada.")

    return data['conversion_rates'][target]
