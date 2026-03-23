# 🧠 Impacto das Redes Sociais na Saúde Mental e no Bem-Estar Emocional

![Status](https://img.shields.io/badge/Status-Planejamento_Concluído-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?logo=pandas&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3.x-003B57?logo=sqlite&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?logo=streamlit&logoColor=white)

Este repositório documenta o Projeto Integrador da disciplina **Desenvolvimento Low Code em Ciência de Dados**, do curso de Análise e Desenvolvimento de Sistemas (ADS) no **Senac**. Atualmente, o projeto encontra-se na **Primeira Etapa (Planejamento e Estruturação)**.

<details>
  <summary><b>📂 Índice (Clique para expandir)</b></summary>
  
  1. [Integrantes do Grupo](#-integrantes-do-grupo)
  2. [Definição da Base de Dados](#-definição-da-base-de-dados)
  3. [Objetivos da Análise](#-objetivos-da-análise)
  4. [Planejamento e Cronograma](#-planejamento-das-tarefas-e-cronograma)
  5. [Transformações de Dados Pretendidas](#-transformações-de-dados-pretendidas)
  6. [Ideia Inicial do Dashboard](#-ideia-inicial-do-dashboard-métricas-e-visualizações)
  7. [Licença](#-licença)
</details>

---

## 👥 Integrantes do Grupo

| Nome | GitHub |
| :--- | :--- |
| **Rafael Caires Pires** | [rafaelcairess](https://github.com/rafaelcairess) |
| **Guilherme Martins** | [Guifarmartins](https://github.com/Guifarmartins) |
| **Vitoria Gomez** | [vitmgomez](https://github.com/vitmgomez) |
| **Ana Flávia Ortiz** | [Ana-Flavia1303](https://github.com/Ana-Flavia1303) |
| **Aline Viana** | — |
| **João** | [euJonh](https://github.com/euJonh) |

---

## 🗄️ Definição da Base de Dados

O projeto utilizará dados que correlacionam o uso de mídias sociais com estados emocionais reportados pelos usuários.

* **Dataset:** [Social Media Usage and Emotional Well-Being](https://www.kaggle.com/datasets/emirhanai/social-media-usage-and-emotional-well-being)
* **Autor:** Julian Emirhan Bulut
* **Fonte:** Kaggle
* **Usabilidade:** 10.0 (Kaggle Score)
* **Armazenamento:** SQLite (armazenamento local para garantir portabilidade entre os integrantes).

### Dicionário de Dados Resumido

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
1. **Associação por Plataforma:** Identificar quais redes possuem maior correlação com índices de ansiedade ou tristeza.
2. **Exposição Temporal:** Verificar se o aumento do tempo de uso diário degrada o humor geral.
3. **Engajamento e Recompensa:** Investigar se o volume de curtidas recebidas influencia a emoção dominante.

---

## 📅 Planejamento das Tarefas e Cronograma

| Etapa | Atividade | Responsável | Status |
| :--- | :--- | :--- | :--- |
| **1** | Planejamento, estruturação do repositório e README inicial. | Rafael Caires Pires | ✅ Concluído |
| **2** | ETL: Limpeza de dados nulos e padronização com Pandas. | Guilherme Martins | 🔜 Próximo semestre |
| **3** | Persistência: Modelagem e carga dos dados no SQLite. | João | 🔜 Próximo semestre |
| **4** | Desenvolvimento do Dashboard interativo no Streamlit. | Ana Flávia Ortiz, Vitoria Gomez e Aline Viana | 🔜 Próximo semestre |
| **5** | Documentação final, testes e revisão técnica. | Todos | 🔜 Próximo semestre |

---

## 🛠️ Transformações de Dados Pretendidas

Para garantir a qualidade da análise, as seguintes transformações serão aplicadas via **Pandas**:
* **Limpeza:** Tratamento de valores ausentes ou inconsistentes.
* **Padronização:** Normalização dos nomes das plataformas e categorias de emoções.
* **Agregação:** Criação de métricas agrupadas por faixa etária e gênero para facilitar a visualização.
* **Carga:** Exportação do DataFrame limpo para uma tabela estruturada no **SQLite**.

---

## 🖥️ Ideia Inicial do Dashboard (Métricas e Visualizações)

O dashboard no Streamlit apresentará as seguintes visões estruturadas:

### 1. Visão Geral (Filtros e KPIs)
No topo (ou na barra lateral do Streamlit), estarão os filtros globais: **Faixa Etária**, **Gênero** e **Plataforma**.

**KPIs Principais (Cards):**
* **Média de Tempo de Uso:** Exibir em minutos ou horas.
* **Emoção Mais Frequente:** Qual sentimento domina o dataset atual.
* **Média de Engajamento:** Média de curtidas recebidas por post.

### 2. Análise por Eixo Temático

**Eixo 1: Associação por Plataforma**
* **Gráfico de Barras Empilhadas (100%):** No eixo X as **Plataformas** e no eixo Y a proporção de **Emoções Dominantes**. *(Insight: mostrará visualmente se o Instagram tem uma fatia de "Ansiedade" maior que o WhatsApp, por exemplo).*
* **TreeMap:** Para mostrar o volume de usuários por plataforma, onde a cor representa a "Emoção Predominante" média daquele grupo.

**Eixo 2: Exposição Temporal (O fator "Tempo")**
* **Gráfico de Dispersão (Scatter Plot):** Eixo X (`Daily Usage Time`) vs. Eixo Y (`Posts per Day`), usando as cores dos pontos para representar a `Dominant Emotion`. *(Insight: ver se quem passa mais tempo tende a cair em emoções negativas).*
* **Gráfico de Densidade/Violino:** Comparando o tempo de uso para cada emoção. *(Insight: "Pessoas que relatam Tristeza passam, em média, mais tempo logadas do que as que relatam Felicidade?")*

**Eixo 3: Engajamento e Recompensa**
* **Histograma de Curtidas:** Para entender a distribuição de "recompensa" dos usuários.
* **Gráfico de Barras de Erro ou Boxplot:** Comparando `Likes Received` por `Dominant Emotion`. *(Insight: Validar a hipótese de que baixo engajamento pode estar correlacionado a sentimentos de Solidão ou Tristeza).*

### 3. Sugestões de Feature Engineering
Para o dashboard ficar mais profissional, as seguintes colunas extras serão criadas no Pandas durante a fase de ETL:
1. **Faixa Etária (Binning):** Transformar a idade exata em categorias (*18-24, 25-34, 35-44, 45+*).
2. **Índice de Engajamento:** Criar uma métrica baseada na razão entre curtidas e posts ($\frac{\text{Likes Received}}{\text{Posts Per Day}}$) para entender a "qualidade" do retorno que o usuário recebe.
3. **Polaridade da Emoção:** Mapear as emoções para *Positiva, Neutra ou Negativa*.

---

## 📄 Licença
Este projeto está licenciado sob a Licença MIT.
