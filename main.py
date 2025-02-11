import pandas as pd
import plotly.express as px
import streamlit as st



# Faturamento por unidade
# Tipo de produto mais vendodo, contribuição por filial
# Desempenho das formas de pagamento
# Como estão as avaliações das filiais



st.set_page_config(layout='wide')

def csv_to_df(df):
    '''
    Transform .csv files to Pandas DataFrame

    :param csv file 
    '''
    df = pd.read_csv(df, sep=';', decimal=',')
    df.info()
    return df

# DADOS

df = csv_to_df('supermarket_sales.csv')
df

# Tratamento dos dados
df['Date'] = pd.to_datetime(df['Date'])

df = df.sort_values('Date')

df['Month'] = df['Date'].apply(lambda x: str(x.year) + '-' + str(x.month))
# display(df)

month = st.sidebar.selectbox('Mês', df['Month'].unique())

df_filtred = df[df['Month'] == month]



# Graficos da primeira linha
col1, col2 = st.columns(2)

# Graficos da segunda linha
col3, col4, col5 = st.columns(3)


# Faturamento por unidade
fig_date = px.bar(df_filtred, x='Date', y='Total', color='City', title='Faturamento por dia')
col1.plotly_chart(fig_date, use_container_width=True)


# Faturamento por tipo de produto
fig_prod = px.bar(df_filtred, x='Date', y='Product line', color='City', title='Faturamento por tipo de produto', orientation='h')
col2.plotly_chart(fig_prod, use_container_width=True)


# Contruibuição por filial
city_total = df_filtred.groupby('City')[['Total']].sum().reset_index()
fig_city = px.bar(city_total, x='City', y='Total', title='Faturamento por filial')
col3.plotly_chart(fig_city, use_container_width=True)



# Contruibuição por filial
city_total = df_filtred.groupby('City')[['Total']].sum().reset_index()
fig_king = px.pie(df_filtred, values='Total', names='Payment', title='Faturamento por tipo de pagamento')
col4.plotly_chart(fig_king, use_container_width=True)


# Contruibuição por filial
city_total = df_filtred.groupby('City')[['Total']].sum().reset_index()
fig_rating = px.bar(df_filtred, x='City', y='Rating', title='Avaliação')
col5.plotly_chart(fig_rating, use_container_width=True)