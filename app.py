import streamlit as st
import sqlite3
import pandas as pd 

#subir o servidor streamlit e printar uma tabela com os dados do db
def create_conection():
    return sqlite3.connect('banco_redes_sociais.db')

conn = create_conection()

df = pd.read_sql_query('SELECT * FROM tb_uso_redes_sociais;', conn)

# st.write(df)

# calcula a media dos valores somando tudo e dividindo pela quantidade 
st.write(df)
media_tempo_uso = df['Daily_Usage_Time (minutes)'].mean()
emocoes_dominantes = df['Dominant_Emotion'].mode()
media_engajamento = df['Likes_Received_Per_Day'].mean()

st.metric(label="Tempo de uso médio", value=round(media_tempo_uso, 2))
st.metric(label="Emoções dominantes", value=emocoes_dominantes[0])
st.metric(label="Curtidas por dia", value=round(media_engajamento, 2))


st.write(f"Média: {media_tempo_uso}\nEmoção dominante: {emocoes_dominantes[0]} media de engajamento {media_engajamento}")

