from Home import *

st.set_page_config(
    page_title="Operacional",
    page_icon="🔩", 
    layout="wide"
)
df=pd.read_excel('Base_FP&A_MRS_Simulada.xlsx')
filtro_ano=st.sidebar.selectbox('Selecione o ano',df['Ano'].unique())
df_filtrado=df[df['Ano']==filtro_ano]

st.header('Indicadores Operacionais')
st.markdown(f"### Ano selecionado: {filtro_ano}")
st.divider()

heatmap_df = (
    df_filtrado
    .groupby(['Região', 'Commodity'])
    .agg({
        'Margem_Contribuição_R$': 'sum',
        'Volume_Toneladas': 'sum'
    })
    .reset_index())

#------------------------ Exibir o dataframe para analisarmos como ficam os dados agrupados ------------------------

#st.dataframe(heatmap_df)

# receita por tonelada
heatmap_df['Receita_Ton'] = (
    heatmap_df['Margem_Contribuição_R$']
    / heatmap_df['Volume_Toneladas'])


#----------------------Reproduzir o erro de botar darkblues no scheme ----------------------

heatmap = alt.Chart(heatmap_df).mark_rect().encode(
    x=alt.X(
        'Região:N',
        title='Região'),
    y=alt.Y(
        'Commodity:N',
        title='Commodity'),
    color=alt.Color(
        'Receita_Ton:Q',
        title='Receita/Ton (R$)',
        scale=alt.Scale(scheme='blues')),
    tooltip=[
        alt.Tooltip(
            'Commodity:N',
            title='Commodity'),
        alt.Tooltip(
            'Região:N',
            title='Região'),
        alt.Tooltip(
            'Receita_Ton:Q',
            title='Receita/Ton',
            format=',.2f')]
            ).properties(
    width=700,
    height=400)

st.subheader("💡 Heatmap de Receita por Tonelada")
st.caption("Análise da receita por tonelada transportada, segmentada por região e commodity.")
st.subheader("")
st.altair_chart(heatmap,use_container_width=True)

painel_operacional = (
    df_filtrado
    .groupby('Commodity')
    .agg({
        'Volume_Toneladas': 'sum',
        'Margem_Contribuição_R$': 'sum',
        'Custo_Operacional_R$': 'sum'
    })
    .reset_index()
)

# -----------------------------
# 1. Receita por tonelada
# -----------------------------

painel_operacional['Receita_Ton'] = (
    painel_operacional['Margem_Contribuição_R$']
    / painel_operacional['Volume_Toneladas']
)

# -----------------------------
# 2. Custo por tonelada
# -----------------------------

painel_operacional['Custo_Ton'] = (
    painel_operacional['Custo_Operacional_R$']
    / painel_operacional['Volume_Toneladas']
)

# -----------------------------
# 3. Índice de Performance Operacional
# -----------------------------

painel_operacional['IPO'] = (
    painel_operacional['Volume_Toneladas']
    / painel_operacional['Custo_Operacional_R$']
)

# -----------------------------
# 4. Capacidade utilizada (%)
# -----------------------------

painel_operacional['Capacidade_Max'] = (
    painel_operacional['Volume_Toneladas'].max() * 1.2
)

painel_operacional['Utilizacao_%'] = (
    painel_operacional['Volume_Toneladas']
    / painel_operacional['Capacidade_Max']
) * 100

# -----------------------------
# Visualização final
# -----------------------------

painel_operacional = painel_operacional[[
    'Commodity',
    'Volume_Toneladas',
    'Receita_Ton',
    'Custo_Ton',
    'IPO',
    'Utilizacao_%'
]]

# ordenando por volume
painel_operacional = painel_operacional.sort_values(
    by='Volume_Toneladas',
    ascending=False
)

#st.dataframe(painel_operacional)

from utils.utils import formatar_valor

commodity_select = st.selectbox(
    'Selecione a Commodity',
    painel_operacional['Commodity'].unique())

dados_commodity = painel_operacional[
    painel_operacional['Commodity'] == commodity_select
].iloc[0]

col1, col2 = st.columns(2)

with col1:

    st.markdown(
        f"""
        <div style="
            background-color:#00355B;
            padding:18px;
            border-radius:12px;
            margin-bottom:12px;
            color:white;
        ">
            <h4>🚂 Volume Transportado</h4>
            <h2>{dados_commodity['Volume_Toneladas']:,.0f} ton</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    #<h2>{formatar_valor(dados_commodity['Volume_Toneladas'])}</h2>

    st.markdown(
        f"""
        <div style="
            background-color:#FFCF00;
            padding:18px;
            border-radius:12px;
            color:white;
        ">
            <h4>💰 Receita por Tonelada</h4>
            <h2>R$ {dados_commodity['Receita_Ton']:,.2f}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:

    st.markdown(
        f"""
        <div style="
            background-color:#FFCF00;
            padding:18px;
            border-radius:12px;
            margin-bottom:12px;
            color:white;
        ">
            <h4>📊 Índice Operacional</h4>
            <h2>{dados_commodity['IPO']:.6f}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div style="
            background-color:#00355B;
            padding:18px;
            border-radius:12px;
            color:white;
        ">
            <h4>⚙️ Utilização da Capacidade</h4>
            <h2>{dados_commodity['Utilizacao_%']:.1f}%</h2>
        </div>
        """,
        unsafe_allow_html=True
    )