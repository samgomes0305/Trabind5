# Importando as bibliotecas necessárias
import pandas as pd
import streamlit as st

# Dados
data = {
    'Ability to impact': [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    'HRBP': [31, 11, 65, 14, 137, 16, 128, 18, 31, 105, 9],
    'Exit survey': [23, 15, 44, 39, 171, 24, 78, 30, 22, 37, 21]
}
index = ['Training', 'Conflict with others', 'Lack of recognition', 'Workload', 'Career advancement', 'Pay', 'Type of work', 'Career change', 'Commute', 'Relocation', 'Illness']

# Criando um DataFrame
df = pd.DataFrame(data, index=index)

# Título do dashboard
st.title('Análise de Atrito na Organização de Marketing')

# Subtítulo
st.subheader('Razões para saída dos funcionários')

# Adicionando um seletor de gráfico
chart_type = st.selectbox('Selecione o tipo de gráfico', ['Barra', 'Linha', 'Área'])

# Adicionando um seletor de colunas
selected_columns = st.multiselect('Selecione as colunas para visualizar', df.columns)

# Mostrando o DataFrame com base nas colunas selecionadas
st.dataframe(df[selected_columns])

# Exibindo o gráfico escolhido
if chart_type == 'Barra':
    st.bar_chart(df[selected_columns])
elif chart_type == 'Linha':
    st.line_chart(df[selected_columns])
elif chart_type == 'Área':
    st.area_chart(df[selected_columns])
