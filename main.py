import pandas as pd
import plotly.express as px
import streamlit as st 

# lendo dataset
df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')

# modificando nome das colunas
df = df.rename(columns={'newDeaths': 'Novos óbitos','newCases': 'Novos casos','deaths_per_100k_inhabitants': 'Óbitos por 100 mil habitantes','totalCases_per_100k_inhabitants':'Casos por 100 mil habitantes'})

# selecao do estado
estados = list(df['state'].unique())
state = st.sidebar.selectbox('Selecione o estado', estados)

# selecao das colunas
colunas = ['Novos óbitos','Novos casos','Óbitos por 100 mil habitantes','Casos por 100 mil habitantes']
column = st.sidebar.selectbox('Selecione a informação desejada:', colunas)

# selecao das linhas dos estados 
df = df[df['state'] == state]

# configurando graficos
fig = px.line(df, x="date", y=column, title=column + ' - ' + state)
fig.update_layout( xaxis_title='Data', yaxis_title=column.upper(), title = {'x':0.5})

# configurando titulo
st.title('DADOS COVID-19 - BRASIL')
# st.write('Nessa aplicação, o usuário tem a opção de escolher o estado e o tipo de informação para mostrar o gráfico. Utilize o menu lateral para alterar a mostragem.')

st.plotly_chart(fig, use_container_width=True)

# configurando nota de rodape
st.caption('Dados obtidos em: https://github.com/wcota/covid19br')