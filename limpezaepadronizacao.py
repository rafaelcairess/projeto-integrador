#---------------------LIMPEZA E PADRONIZAÇAO---------------------------
import pandas as pd
pd.options.mode.chained_assignment = None

# Leitura dos 3 arquivos CSV e união em um único DataFrame
df_csv = pd.concat([
    pd.read_csv("data/raw/train.csv", on_bad_lines="skip"),
    pd.read_csv("data/raw/test.csv",  on_bad_lines="skip"),
    pd.read_csv("data/raw/val.csv",   on_bad_lines="skip"),
], ignore_index=True)
df_csv

df_csv.head(10)

df_csv.info()

df_csv.describe()

df_csv.isnull().sum()

# Verifica e remove linhas duplicadas
total_duplicadas = df_csv.duplicated().sum()
print(f"Total de linhas duplicadas: {total_duplicadas}")

df_csv = df_csv.drop_duplicates(keep="first")

total_duplicadas = df_csv.duplicated().sum()
print(f"Total de linhas duplicadas: {total_duplicadas}")

# Padroniza os nomes das plataformas para evitar inconsistências
correcoes = {
"snapchat" : "Snapchat",
"telegram": "Telegram",
"linkedin": "Linkedin",
"facebook": "Facebook",
"instagram": "Instagram",
"twitter": "Twitter",
"whatsapp": "Whatsapp",                            
}
df_csv["Platform"] = df_csv["Platform"].replace(correcoes)

# Padroniza os valores de gênero para garantir consistência
correcao = {
"female" : "Female",
"male": "Male",
"non-binary": "Non-binary",
}
df_csv["Gender"] = df_csv["Gender"].replace(correcao)

# Remove linhas com valores de gênero inválidos (lixo que não foi corrigido)
generos_validos = ["Female", "Male", "Non-binary"]
df_csv = df_csv[df_csv["Gender"].isin(generos_validos)]

# Converte Age pra numérico e remove valores fora do intervalo esperado
df_csv["Age"] = pd.to_numeric(df_csv["Age"], errors="coerce")
df_csv = df_csv[df_csv["Age"].between(10, 100)]

print(df_csv["Dominant_Emotion"].unique())

# Padroniza os valores de emoção dominante
correcaob = {
"neutral" : "Neutral",
"anxiety": "Anxiety",
"sadness": "Sadness",
"happiness": "Happiness",
"boredom": "Boredom",
"anger": "Anger",                                          
}
df_csv["Dominant_Emotion"] = df_csv["Dominant_Emotion"].replace(correcaob)