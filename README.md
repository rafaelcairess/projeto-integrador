# Projeto Integrador - Análise de Dados Low Code 2° Semestre

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=Kaggle&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

📌 Tema do Projeto
Impacto das Redes Sociais na Saúde Mental e no Bem-Estar Emocional

👥 Integrantes
NomeGitHubRafael Caires Pires—Guilherme Martins—Vitoria Gomez@vitmgomezAna Flávia Ortiz—Aline Viana—

🗄️ Definição da Base de Dados

Dataset: Social Media Usage and Emotional Well-Being
Fonte: Kaggle — emirhanai
Usabilidade (Kaggle): 10.0 ⭐
Número de colunas: 8
Banco de Dados (Storage): SQLite

Colunas do Dataset
ColunaDescriçãoUser_IDIdentificador do usuárioAgeIdadeGenderGêneroPlatformPlataforma de rede social utilizadaDaily_Usage_TimeTempo de uso diário (em minutos)Posts_Per_DayNúmero de posts por diaLikes_Received_Per_DayCurtidas recebidas por diaDominant_EmotionEmoção dominante do usuário (ex: Feliz, Ansioso, Triste)
Justificativa da Escolha
O dataset foi escolhido por ter usabilidade 10.0 no Kaggle, apenas 8 colunas bem organizadas e dados limpos — ideal para um primeiro projeto em grupo. Ele abrange exatamente o tema escolhido: o impacto emocional do uso das redes sociais.
O SQLite foi escolhido como banco de dados por ser leve, local e fácil de integrar com o Pandas via to_sql, sem necessidade de configuração de servidor.

🎯 Objetivo da Análise
Este projeto tem como objetivo investigar a relação entre o uso de redes sociais e o bem-estar emocional dos usuários, analisando três eixos principais:

Impacto emocional por plataforma — quais apps estão mais associados a emoções negativas como ansiedade e tristeza
Tempo de uso e saúde mental — se maior tempo nas redes sociais piora o humor geral
Engajamento e bem-estar — se o número de curtidas recebidas influencia a emoção dominante do usuário

O processo completo envolverá ETL com Python e Pandas, armazenamento em SQLite e visualização interativa com Streamlit.

📅 Planejamento das Tarefas
EtapaDescriçãoResponsávelEtapa 1 — Planejamento e EstruturaçãoCriação do repositório no GitHub, definição do dataset e elaboração do READMERafael Caires PiresEtapa 2 — Processo de ETLImportação do .csv, limpeza de dados nulos, padronização de formatos e remoção de inconsistências com PandasA definirEtapa 3 — ArmazenamentoConexão e carregamento dos dados tratados no SQLiteA definirEtapa 4 — Desenvolvimento do DashboardCriação de visualizações e métricas interativas com StreamlitA definirEtapa 5 — Documentação e Entrega FinalRevisão do código, testes do dashboard e gravação da apresentaçãoRafael Caires Pires + Todos

🖥️ Ideia Inicial do Dashboard
O dashboard será desenvolvido em Streamlit e apresentará os seguintes indicadores e visualizações:
📊 Cards no topo

Total de usuários analisados
Emoção mais comum entre os usuários
Plataforma com maior tempo médio de uso

📈 Aba 1 — Perfil dos Usuários

Gráfico de barras: distribuição de usuários por plataforma
Gráfico de pizza: distribuição por gênero e faixa etária

😰 Aba 2 — Plataforma x Emoção

Gráfico de barras agrupado: qual plataforma está mais associada a cada emoção dominante
Filtro interativo por gênero e faixa etária

⏱️ Aba 3 — Tempo de Uso x Humor

Scatter plot: tempo de uso diário (minutos) x emoção dominante
Análise de tendência: mais horas nas redes = emoção mais negativa?

❤️ Aba 4 — Curtidas x Bem-Estar

Scatter plot: curtidas recebidas por dia x emoção dominante
Comparação: usuários com mais curtidas são mais felizes?

📋 Aba 5 — Dados Brutos

Tabela interativa com filtros por plataforma, gênero e emoção


🛠️ Tecnologias Utilizadas

Python — linguagem principal
Pandas — tratamento e transformação dos dados (ETL)
SQLite — armazenamento dos dados tratados
Streamlit — desenvolvimento do dashboard interativo
GitHub — versionamento e colaboração


📄 Licença
Este projeto está licenciado sob a Licença MIT.


Projeto desenvolvido para a disciplina de Projeto Integrador (PI) — Desenvolvimento Low Code em Ciência de Dados | Senac EAD
