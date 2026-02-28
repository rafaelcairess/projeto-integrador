# 🧠 Impacto das Redes Sociais na Saúde Mental e no Bem-Estar Emocional

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?logo=pandas&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3.x-003B57?logo=sqlite&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?logo=streamlit&logoColor=white)

Este repositório documenta a **Primeira Etapa (Planejamento e Estruturação)** do Projeto Integrador da disciplina **Desenvolvimento Low Code em Ciência de Dados**, do curso de Análise e Desenvolvimento de Sistemas (ADS) no **Senac EAD**.

---

## 👥 Integrantes do Grupo

| Nome | GitHub |
| :--- | :--- |
| **Rafael Caires Pires** | [rafaelcairess](https://github.com/rafaelcairess) |
| **Guilherme Martins** | [Guifarmartins](https://github.com/Guifarmartins) |
| **Vitoria Gomez** | [vitmgomez](https://github.com/vitmgomez) |
| **Ana Flávia Ortiz** | — |
| **Aline Viana** | — |
| **João** | — |

---

## 🗄️ Definição da Base de Dados

O projeto utilizará dados que correlacionam o uso de mídias sociais com estados emocionais reportados pelos usuários.

* **Dataset:** *Social Media Usage and Emotional Well-Being*
* **Fonte:** Kaggle (Autor: emirhanai)
* **Usabilidade:** 10.0 (Kaggle Score)
* **Armazenamento:** SQLite (armazenamento local para garantir portabilidade entre os integrantes).

### Dicionário de Dados

| Variável | Descrição |
| :--- | :--- |
| `User_ID` | Identificador único do registro |
| `Age` | Idade do usuário |
| `Gender` | Gênero do usuário |
| `Platform` | Plataforma de rede social analisada |
| `Daily_Usage_Time` | Tempo médio de exposição diária (minutos) |
| `Posts_Per_Day` | Volume de postagens diárias |
| `Likes_Received_Per_Day` | Volume de curtidas recebidas por dia |
| `Dominant_Emotion` | Emoção predominante (Ansiedade, Felicidade, Tristeza, etc.) |

---

## 🎯 Objetivos da Análise

A pesquisa busca identificar padrões estatísticos entre o consumo de conteúdo digital e a saúde mental através dos seguintes eixos:

1.  **Associação por Plataforma:** Identificar quais redes possuem maior correlação com índices de ansiedade ou tristeza.
2.  **Exposição Temporal:** Verificar se o aumento do tempo de uso diário degrada o humor geral.
3.  **Engajamento e Recompensa:** Investigar se o volume de curtidas recebidas influencia a emoção dominante.

---

## 📅 Planejamento das Tarefas e Cronograma

| Etapa | Atividade | Responsável | Status |
| :--- | :--- | :--- | :--- |
| **1** | Planejamento, estruturação do repositório e README inicial. | Rafael Caires Pires | Concluído |
| **2** | ETL: Limpeza de dados nulos e padronização com Pandas. | A definir | Pendente |
| **3** | Persistência: Modelagem e carga dos dados no SQLite. | A definir | Pendente |
| **4** | Desenvolvimento do Dashboard interativo no Streamlit. | A definir | Pendente |
| **5** | Documentação final, testes e revisão técnica. | Todos | Pendente |

---

## 🛠️ Transformações de Dados Pretendidas

Para garantir a qualidade da análise, as seguintes transformações serão aplicadas via **Pandas**:
* **Limpeza:** Tratamento de valores ausentes ou inconsistentes.
* **Padronização:** Normalização dos nomes das plataformas e categorias de emoções.
* **Agregação:** Criação de métricas agrupadas por faixa etária e gênero para facilitar a visualização.
* **Carga:** Exportação do DataFrame limpo para uma tabela estruturada no **SQLite**.

---

## 🖥️ Ideia Inicial do Dashboard (Métricas e Visualizações)

O dashboard no Streamlit apresentará as seguintes visões:
* **Métricas Principais (KPIs):** Total de usuários, emoção predominante e média de tempo de uso.
* **Gráficos de Distribuição:** Perfis demográficos (idade/gênero) dos usuários analisados.
* **Análise de Correlação:** Gráficos de dispersão correlacionando tempo de uso vs. emoções.
* **Comparativo de Plataformas:** Ranking de plataformas por tipo de impacto emocional.
* **Visualização de Dados Brutos:** Tabela interativa com filtros dinâmicos para exploração.

---

## 📄 Licença

Este projeto está licenciado sob a Licença MIT.
