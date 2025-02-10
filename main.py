import pandas as pd
import plotly.express as px
import streamlit as st


print('Hello world')

df = pd.read_csv('supermarket_sales.csv', sep=';', decimal=',')
# display(df)
# df.info()

# Tratamento dos dados
df['Date'] = pd.to_datetime(df['Date'])

df = df.sort_values('Date')

df['Month'] = df['Date'].apply(lambda x: str(x.year) + '-' + str(x.month))
# display(df)

month = st.sidebar.selectbox('Mês', df['Month'].unique())

df_filtred = df[df['Month'] == month]



# Faturamento por unidade
# Tipo de produto mais vendodo, contribuição por filial
# Desempenho das formas de pagamento
# Como estão as avaliações das filiais


col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

# Faturamento por unidade
fig_date = px.bar(df_filtred, x='Date', y='Total', color='City', title='Faturamento por dia')
col1.plotly_chart(fig_date)


# Faturamento por tipo de produto
fig_prod = px.bar(df_filtred, x='Date', y='Product line', color='City', title='Faturamento por tipo de produto', orientation='h')
col2.plotly_chart(fig_prod)


city_total = df_filtred.groupby('City')[['Total']].sum().reset_index()

fig_city = px.bar(df_filtred, x='City', y='Total', title='Faturamento por tipo de produto', orientation='h')
col3.plotly_chart(fig_city)