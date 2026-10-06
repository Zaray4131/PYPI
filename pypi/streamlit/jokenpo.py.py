import streamlit as st
import random

st.set_page_config(page_title="Jokenpô", page_icon="✊", layout="centered")

st.title("✊✋✌️ Pedra, Papel e Tesoura")
st.write("Escolha sua jogada e tente vencer o computador!")

# 1. Inicializa o placar na memória do Streamlit
if "vitorias" not in st.session_state:
    st.session_state.vitorias = 0
if "derrotas" not in st.session_state:
    st.session_state.derrotas = 0
if "empates" not in st.session_state:
    st.session_state.empates = 0

# Opções de jogada
opcoes = ["Pedra ✊", "Papel ✋", "Tesoura ✌️"]

# 2. Interface de escolha do jogador
st.subheader("Sua vez:")
col1, col2, col3 = st.columns(3)

jogada_usuario = None

with col1:
    if st.button("✊ Escolher Pedra", use_container_width=True):
        jogada_usuario = "Pedra ✊"
with col2:
    if st.button("✋ Escolher Papel", use_container_width=True):
        jogada_usuario = "Papel ✋"
with col3:
    if st.button("✌️ Escolher Tesoura", use_container_width=True):
        jogada_usuario = "Tesoura ✌️"

# 3. Lógica do Jogo (Executada após o clique do botão)
if jogada_usuario:
    # Computador faz a escolha dele
    jogada_computador = random.choice(opcoes)
    
    st.markdown("---")
    st.write(f"Você escolheu: **{jogada_usuario}**")
    st.write(f"O computador escolheu: **{jogada_computador}**")
    
    # Determina o resultado
    if jogada_usuario == jogada_computador:
        st.info("🤝 É um Empate!")
        st.session_state.empates += 1
    elif (
        (jogada_usuario == "Pedra ✊" and jogada_computador == "Tesoura ✌️") or
        (jogada_usuario == "Papel ✋" and jogada_computador == "Pedra ✊") or
        (jogada_usuario == "Tesoura ✌️" and jogada_computador == "Papel ✋")
    ):
        st.success("🎉 Você Ganhou!")
        st.session_state.vitorias += 1
    else:
        st.error("😢 O Computador Ganhou!")
        st.session_state.derrotas += 1

# 4. Exibe o Painel de Placar
st.markdown("---")
st.subheader("🏆 Placar")
col_vit, col_der, col_emp = st.columns(3)

col_vit.metric("Vitórias", st.session_state.vitorias)
col_der.metric("Derrotas", st.session_state.derrotas)
col_emp.metric("Empates", st.session_state.empates)

# Botão para resetar o jogo
if st.button("Zerar Placar 🔄"):
    st.session_state.vitorias = 0
    st.session_state.derrotas = 0
    st.session_state.empates = 0
    st.rerun()
