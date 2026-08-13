import streamlit as st

st.title("Meu Chatbot Interativo 🤖")

if "historico" not in st.session_state:
    st.session_state.historico = []

for mensagem in st.session_state.historico:
    with st.chat_message(mensagem["autor"]):
        st.write(mensagem["texto"])

if pergunta := st.chat_input("Diga algo para o robô..."):
    with st.chat_message("user"):
        st.write(pergunta)
    st.session_state.historico.append({"autor": "user", "texto": pergunta})

    resposta_robo = f"Você disse: '{pergunta}'. Que legal! Eu sou um robô feito em Streamlit."
    with st.chat_message("assistant"):
        st.write(resposta_robo)
    st.session_state.historico.append({"autor": "assistant", "texto": resposta_robo})
