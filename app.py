import streamlit as st
import sqlite3
import pandas as pd 
import plotly.express as px

# Conecta ao banco de dados
@st.cache_data
def create_conection():
    conn = sqlite3.connect('banco_redes_sociais.db')
    df = pd.read_sql_query('SELECT * FROM tb_uso_redes_sociais;', conn)
    conn.close()
    return df

df_raw = create_conection()

# Configuração da página
st.set_page_config(page_title="Redes Sociais & Bem-Estar Emocional", page_icon="🧠", layout="wide")

# Sidebar - Filtros globais
with st.sidebar:
    st.header("🔎 Filtros")

    plataformas = sorted(df_raw['Platform'].dropna().unique())
    sel_plataforma = st.multiselect('Plataforma', options=plataformas, default=plataformas)

    generos = sorted(df_raw['Gender'].dropna().unique())
    sel_genero = st.multiselect('Gênero', options=generos, default=generos)

    # Faixa etária (bins definidos no planejamento do projeto)
    bins   = [0, 24, 34, 44, 120]
    labels = ['18–24', '25–34', '35–44', '45+']
    df_raw['Age'] = pd.to_numeric(df_raw['Age'], errors='coerce')
    df_raw['Faixa_Etaria'] = pd.cut(df_raw['Age'], bins=bins, labels=labels, right=True)
    sel_faixa = st.multiselect('Faixa Etária', options=labels, default=labels)

    st.divider()

    # Paleta de cores por emoção - escolha livre
    st.header("🎨 Cores por Emoção")
    emocoes = sorted(df_raw['Dominant_Emotion'].dropna().unique())
    cores_padrao = {
        "Happiness":  "#4CAF50",
        "Sadness":    "#5C9BD6",
        "Anxiety":    "#FF7043",
        "Anger":      "#E53935",
        "Neutral":    "#90A4AE",
        "Boredom":    "#AB47BC",
        "Agression":  "#FF6F00",
    }
    EMOTION_COLORS = {}
    for emocao in emocoes:
        padrao = cores_padrao.get(emocao, "#888888")
        EMOTION_COLORS[emocao] = st.color_picker(emocao, value=padrao)

# Aplica os filtros em todo o df
df = df_raw[
    df_raw['Platform'].isin(sel_plataforma) &
    df_raw['Gender'].isin(sel_genero) &
    df_raw['Faixa_Etaria'].isin(sel_faixa)
]

if df.empty:
    st.warning("Nenhum dado encontrado para os filtros selecionados.")
    st.stop()

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

fig_bar = px.bar(
    df_contagem,
    x='Platform',
    y='Contagem',
    color='Dominant_Emotion',
    color_discrete_map=EMOTION_COLORS,
    barmode='stack',
    labels={'Platform': 'Plataforma', 'Contagem': 'Quantidade de Emoções', 'Dominant_Emotion': 'Emoção'},
)
st.plotly_chart(fig_bar, use_container_width=True)

st.title("Exposição temporal")
st.divider()

#Eixo 2 - grafico de dispersão - Exposição temporal
fig_scatter = px.scatter(
    df,
    x='Daily_Usage_Time (minutes)',
    y='Posts_Per_Day',
    color='Dominant_Emotion',
    color_discrete_map=EMOTION_COLORS,
    labels={'Daily_Usage_Time (minutes)': 'Uso diário (min)', 'Posts_Per_Day': 'Postagens por dia', 'Dominant_Emotion': 'Emoção'},
    opacity=0.7,
)
st.plotly_chart(fig_scatter, use_container_width=True)
# deixando assim por enquanto

st.title("Engajamento e recompensa")
st.divider()

# Eixo 3: Engajamento e recompensa 
fig_box = px.box(
    df,
    x='Dominant_Emotion',
    y='Likes_Received_Per_Day',
    color='Dominant_Emotion',
    color_discrete_map=EMOTION_COLORS,
    labels={'Dominant_Emotion': 'Emoção dominante', 'Likes_Received_Per_Day': 'Curtidas recebidas por dia'},
)
fig_box.update_layout(showlegend=False)
st.plotly_chart(fig_box, use_container_width=True)