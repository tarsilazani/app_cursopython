from Home import *
st.set_page_config(
    page_title="Financeiro",
    page_icon="💰",
    layout="wide"
)

df=pd.read_excel('Base_FP&A_MRS_Simulada.xlsx')
filtro_ano=st.sidebar.selectbox('Selecione o ano',df['Ano'].unique())
df_filtrado=df[df['Ano']==filtro_ano]

st.header('Indicadores Financeiros')
st.markdown(f"### Ano selecionado: {filtro_ano}")
st.divider()

soma_receita=df_filtrado['Margem_Contribuição_R$'].sum()
soma_toneladas=df_filtrado['Volume_Toneladas'].sum()
soma_custo=df_filtrado['Custo_Operacional_R$'].sum()
receita_por_Tonelada=soma_receita/soma_toneladas
custo_por_Tonelada=soma_custo/soma_toneladas

def formatar_valor(valor):
    if valor >= 1_000_000_000:
        return f"R$ {valor/1_000_000_000:.1f} BI"
    elif valor >= 1_000_000:
        return f"R$ {valor/1_000_000:.1f} MI"
    else:
        return f"R$ {valor:,.2f}"


col1, col2 = st.columns(2)
with col1:
    st.metric(
        "Receita Líquida Total (R$)",
        formatar_valor(soma_receita))
    st.metric(
        "Custo Total (R$)",
        formatar_valor(soma_custo))
with col2:
    st.metric("Receita Líquida por Tonelada (R$)", f"R$ {receita_por_Tonelada:,.2f}")
    st.metric("Custo por Tonelada (R$)", f"R$ {custo_por_Tonelada:,.2f}")

receita_commodity = (df_filtrado.groupby('Commodity')['Margem_Contribuição_R$'].sum().reset_index())
receita_commodity = receita_commodity.sort_values(by='Margem_Contribuição_R$',ascending=False)
receita_commodity['Receita_fmt'] = (
    receita_commodity['Margem_Contribuição_R$'] / 1000000)
grafico_receita_commodity = alt.Chart(receita_commodity).mark_bar(color='#00355B').encode(
    x=alt.X(
        'Commodity:N',
        sort='-y',
        title='Commodity'),
    y=alt.Y(
        'Receita_fmt:Q',
        title='Receita Total (R$)'),
    tooltip=[
        alt.Tooltip('Commodity:N'),
        alt.Tooltip(
            'Receita_fmt:Q',
            title='Receita',
            format=',.2f')]
).properties(
    width=700,
    height=600)

c_1, c_2 = st.columns([3,1])
with c_1:
    st.subheader('Receita por Commodity')
    st.caption('Os valores estão em milhões de reais (R$).')
    st.altair_chart(grafico_receita_commodity, use_container_width=True)
with c_2:

    st.subheader("🏆 Ranking")

    ranking = receita_commodity['Commodity'].tolist()

    for i, commodity in enumerate(ranking[:10], start=1):

        st.markdown(
            f'<div style="background-color:#00355B;padding:12px;border-radius:10px;margin-bottom:8px;color:white;font-size:14px;"><span style="color:#FFCF00;font-weight:bold;">#{i}</span> {commodity}</div>',
            unsafe_allow_html=True
        )

#--------------------- Comentar o uso de IA no design de markdowns mais elaborados ---------------------