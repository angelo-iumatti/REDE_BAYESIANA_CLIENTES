import streamlit as st
from modelo import calcular_probabilidade_compra

st.set_page_config(page_title="Análise de Compra com Rede Bayesiana", layout="centered")

st.title("🛍️ Rede Bayesiana: Probabilidade de Compra")

st.markdown("Preencha as informações do comportamento do cliente:")

hist = st.selectbox("🛒 Histórico de Compras", ["sim", "nao"])
tempo = st.selectbox("⏱️ Tempo no Site", ["muito", "pouco"])
inter = st.selectbox("🎯 Interação com Promoções", ["sim", "nao"])

if st.button("Calcular Probabilidade de Compra"):
    evidencias = {
        "HistoricoCompras": hist,
        "TempoNoSite": tempo,
        "InteracaoPromocao": inter
    }

    resultado = calcular_probabilidade_compra(evidencias)

    st.subheader("📊 Resultado:")
    st.success(f"✔️ Compra: **{resultado['Compra']*100:.1f}%**")
    st.error(f"❌ Não Compra: **{resultado['Nao_Compra']*100:.1f}%**")
