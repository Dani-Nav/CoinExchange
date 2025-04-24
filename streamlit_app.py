import streamlit as st
from api_handler import get_exchange_rate


st.set_page_config(page_title="Conversor de Moedas", layout="centered")
st.title("💱 Conversor de Moedas em Tempo Real")

moeda_origem = st.selectbox("Moeda de origem", ["USD", "EUR", "BRL", "JPY", "GBP"])
moeda_destino = st.selectbox("Moeda de destino", ["USD", "EUR", "BRL", "JPY", "GBP"])
quantia = st.number_input("Valor a converter", min_value=0.0, format="%.2f")

if st.button("Converter"):
    try:
        taxa = get_exchange_rate(moeda_origem, moeda_destino)
        convertido = quantia * taxa
        st.success(f"{quantia:.2f} {moeda_origem} = {convertido:.2f} {moeda_destino}")
    except Exception as e:
        st.error(f"Erro ao consultar taxa de câmbio: {e}")
