import sqlite3 

#conecta o arquivo da database
connection = sqlite3.connect('banco_redes_sociais.db')

#cria um objeto cursor para executar os co0mandos
 
cursor = connection.cursor()


#cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;") 
# cursor.execute("SELECT * FROM tb_uso_redes_sociais")
# rows = cursor.fetchall()

# for row in rows:
#     print(row)

cursor.execute("SELECT * FROM tb_uso_redes_sociais limit 0 ")

nome_das_colunas = [descricao[0] for descricao in cursor.description]

#User_ID', 'Age', 'Gender', 'Platform', 'Daily_Usage_Time (minutes)',
#  'Posts_Per_Day', 'Likes_Received_Per_Day', 'Comments_Received_Per_Day', 
# 'Messages_Sent_Per_Day', 'Dominant_Emotion

print(nome_das_colunas)

connection.close()
