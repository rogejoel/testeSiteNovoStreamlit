import streamlit as st
import pandas as pd
import numpy as np

st.title("Painel de Vendas Interativo 📊")

st.sidebar.header("Filtros do Painel")
mes_selecionado = st.sidebar.selectbox("Escolha o Mês:", ["Janeiro", "Fevereiro", "Março", "Abril"])
meta = st.sidebar.slider("Definir Meta de Vendas (em R$):", 10000, 50000, 30000)

np.random.seed(42)
dados_vendas = pd.DataFrame({'Dia': range(1, 31), 'Vendas_R$': np.random.randint(800, 2500, size=30).cumsum()})
total_vendas = int(dados_vendas['Vendas_R$'].iloc[-1])

col1, col2, col3 = st.columns(3)
with col1: st.metric(label="Mês Selecionado", value=mes_selecionado)
with col2: st.metric(label="Total de Vendas", value=f"R$ {total_vendas:,}")
with col3: st.metric(label="Meta Estipulada", value=f"R$ {meta:,}", delta=f"{total_vendas - meta:+,} p/ Meta")

st.divider()
st.line_chart(dados_vendas.set_index('Dia'))
