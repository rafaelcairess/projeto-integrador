import streamlit as st
import sqlite3
import pandas as pd 
import plotly.express as px

#subir o servidor streamlit e printar uma tabela com os dados do db
def create_conection():
    return sqlite3.connect('banco_redes_sociais.db')

conn = create_conection()

df = pd.read_sql_query('SELECT * FROM tb_uso_redes_sociais;', conn)

# st.write(df)

# .mean() calcula a media dos valores somando tudo e dividindo pela quantidade 
st.write(df)
media_tempo_uso = df['Daily_Usage_Time (minutes)'].mean()
emocoes_dominantes = df['Dominant_Emotion'].mode()
media_engajamento = df['Likes_Received_Per_Day'].mean()

# Criação de cards
st.metric(label="Tempo de uso médio", value=round(media_tempo_uso, 2))
st.metric(label="Emoções dominantes", value=emocoes_dominantes[0])
st.metric(label="Curtidas por dia", value=round(media_engajamento, 2))

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