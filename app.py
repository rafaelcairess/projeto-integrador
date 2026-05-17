import streamlit as st
import sqlite3
import pandas as pd 
import plotly.express as px
import numpy 

# Conecta ao banco de dados
def create_conection():
    return sqlite3.connect('banco_redes_sociais.db')

conn = create_conection()

df = pd.read_sql_query('SELECT * FROM tb_uso_redes_sociais;', conn)

# Título
st.title("Redes Sociais e Bem-Estar Emocional")
st.divider()

# Calcula as métricas
media_tempo_uso = df['Daily_Usage_Time (minutes)'].mean()
emocoes_dominantes = df['Dominant_Emotion'].mode()
media_engajamento = df['Likes_Received_Per_Day'].mean()

# Exibe os KPIs em colunas
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Tempo de uso médio", value=f"{round(media_tempo_uso, 1)} min")

with col2:
    st.metric(label="Emoção mais frequente", value=emocoes_dominantes[0])

with col3:
    st.metric(label="Curtidas por dia", value=round(media_engajamento, 1))
 
st.title("Associação por plataforma") #botar titulo nos outros eixos
st.divider() # colocar faixa que divide sessões em todos

#Eixo 1 - Associação por plataforma
df_contagem = df.groupby(['Platform', 'Dominant_Emotion']).size().reset_index(name='Contagem')

st.bar_chart(
    data=df_contagem,
    x="Platform",
    y="Contagem",
    color="Dominant_Emotion",
    x_label="Plataforma",
    y_label="Quantidade de Emoções"
)

st.title("Exposição temporal")
st.divider()

#Eixo 2 - grafico de dispersão - Exposição temporal
st.scatter_chart(
    data=df,
    x='Daily_Usage_Time (minutes)',
    y='Posts_Per_Day',
    color='Dominant_Emotion',
    x_label='Uso diario',
    y_label='Postagens por dia',
    
)
# deixando assim por enquanto

st.title("Engajamento e recompensa")
st.divider()

# Eixo 3: Engajamento e recompensa 
fig_box = px.box(df, x='Dominant_Emotion', y='Likes_Received_Per_Day', title='inserir explicação aqui')
st.plotly_chart(fig_box)

