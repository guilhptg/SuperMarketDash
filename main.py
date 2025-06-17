import pandas as pd
import plotly.express as px
import streamlit as st
from dash import Dash, html, dcc


# Faturamento por unidade
# Tipo de produto mais vendodo, contribuição por filial
# Desempenho das formas de pagamento
# Como estão as avaliações das filiais


# Configuração para os elementos da página ocuparem a largura total
st.set_page_config(layout='wide')


# Title
st.title('Supermarket - Sales')
st.caption('Created by: Guilherme Portugal')
st.subheader('Seles in Q1 2019')


def csv_to_df(df):
    '''
    Transform .csv files to Pandas DataFrame

    :param df: str - CSV file to transforme a Data Frame with Pandas
    :return: 
    '''

    df = pd.read_csv(df, sep=';', decimal=',')
    
    return df


# DADOS
df = csv_to_df('supermarket_sales.csv')

# Tratamento dos dados
df['Date'] = pd.to_datetime(df['Date'])

# Order ascendente
df = df.sort_values('Date')

# Filtro avançado para identificar o mês pelo ano respectivo
df['Month'] = df['Date'].apply(lambda x: str(x.year) + '-' + str(x.month))


# Select Bar para filtrar os dados por mês
month = st.sidebar.selectbox('Mês', df['Month'].unique())

df_filtred = df[df['Month'] == month]



# Graficos da primeira linha
col1, col2 = st.columns(2)

# Graficos da segunda linha
col3, col4, col5 = st.columns(3)


# Faturamento por unidade
fig_date = px.bar(df_filtred, x='Date', y='Total', color='City', title='Revenue by Day')
col1.plotly_chart(fig_date, use_container_width=True)


# Faturamento por tipo de produto
fig_prod = px.bar(df_filtred, x='Date', y='Product line', color='City', title='Revenue by Product Type', orientation='h')
col2.plotly_chart(fig_prod, use_container_width=True)


# Faturamento por filial
city_total = df_filtred.groupby('City')[['Total']].sum().reset_index()
fig_city = px.bar(city_total, x='City', y='Total', title='Revenue by Branch')
col3.plotly_chart(fig_city, use_container_width=True)



# Faturamento por tipo de pagamento
city_total = df_filtred.groupby('City')[['Total']].sum().reset_index()
fig_king = px.pie(df_filtred, values='Total', names='Payment', title='Revenue by Payment Type')
col4.plotly_chart(fig_king, use_container_width=True)


# Avaliação por filial
city_total = df_filtred.groupby('City')[['Total']].sum().reset_index()
fig_rating = px.bar(df_filtred, x='City', y='Rating', title='Rating by Branch')
col5.plotly_chart(fig_rating, use_container_width=True)

st.markdown('#### Follow me on [guilhptg - GitHub](https://github.com/guilhptg/)')

