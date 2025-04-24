import requests
import streamlit as st

def get_exchange_rate(base: str, target: str) -> float:
    base_upper = base.upper()
    target_upper = target.upper()
    url = f"https://open.er-api.com/v6/latest/{base_upper}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        st.write(data)  # só durante o debug

        if data.get('result') != 'success':
            raise ValueError(f"Erro ao acessar a API de câmbio: {data.get('error-description', 'Erro desconhecido')}")

        rates = data.get('rates', {})  # ✅ Use 'rates' em vez de 'conversion_rates'
        if not rates:
            raise ValueError("Resposta da API não continha as taxas de câmbio.")

        if base_upper == target_upper:
            return 1.0

        if target_upper in rates:
            return rates[target_upper]
        else:
            raise ValueError(f"Moeda de destino '{target_upper}' não encontrada para a base '{base_upper}'.")

    except requests.exceptions.RequestException as e:
        raise Exception(f"Erro de conexão com a API: {e}")
    except ValueError as ve:
        raise ValueError(str(ve))
    except Exception as e:
        raise Exception(f"Ocorreu um erro inesperado: {e}")
