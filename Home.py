import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

import streamlit as st

# -----------------------------
# Configuração da página
# -----------------------------
st.set_page_config(
    page_title="Dashboard FP&A Ferroviário",
    page_icon="🚂",
    layout="wide"
)

# -----------------------------
# Home
# -----------------------------
st.title("🚂 Dashboard FP&A Ferroviário")

st.markdown("""
### Bem-vindo

Este dashboard foi desenvolvido para acompanhar indicadores financeiros e operacionais da MRS, com foco em análises de FP&A (Financial Planning & Analysis).

A proposta é transformar dados em informações estratégicas por meio de visualizações interativas e análises comparativas.
""")

# -----------------------------
# Objetivos
# -----------------------------
st.markdown("""
<style>

.main {
    background-color: #F5F7FA;
}

.bloco {
    background-color: #00355B;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.bloco_2 {
    background-color: #FFCF00;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}            
.titulo {
    color: #00355B;
    font-size: 42px;
    font-weight: 700;
}

.subtitulo {
    color: #5B657A;
    font-size: 18px;
    margin-bottom: 30px;
}

</style>
""", unsafe_allow_html=True)


c1, c2 = st.columns([1,1])

# -----------------------------------
# COLUNA 1
# -----------------------------------

with c1:

    st.markdown("<div class='bloco'>", unsafe_allow_html=True)

    st.image('imagem_ferrovia2.jpg', width=420)

    st.subheader("🎯 Objetivos do Projeto")

    st.markdown("""
    - Monitorar o desempenho financeiro da operação  
    - Acompanhar custos, receitas e eficiência operacional  
    - Facilitar análises gerenciais e tomada de decisão  
    - Explorar tendências e evolução dos indicadores  
    """)

    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


# -----------------------------------
# COLUNA 2
# -----------------------------------

with c2:

    st.markdown("<div class='bloco'>", unsafe_allow_html=True)

    st.subheader("📂 Páginas Disponíveis")

    st.markdown("""

     🏠 Home  
    Visão geral do projeto e navegação

    💰 Indicadores Financeiros  
    Análises de receita, custos e margem

    🚆 Operações Ferroviárias  
    Volume transportado e indicadores operacionais

    """)

    st.image('imagem_ferrovia1.jpg', width=420)

st.markdown("<div class='bloco_2'>", unsafe_allow_html=True)


# -----------------------------
# Rodapé
# -----------------------------
st.divider()

st.caption("Projeto final — Dashboard FP&A Ferroviário")