# 🧠 Impacto das Redes Sociais na Saúde Mental e no Bem-Estar Emocional

![Status](https://img.shields.io/badge/Status-Em_Execução-blue)
![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?logo=pandas&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3.x-003B57?logo=sqlite&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?logo=streamlit&logoColor=white)

Este repositório documenta o Projeto Integrador da disciplina **Desenvolvimento Low Code em Ciência de Dados**, do curso de Análise e Desenvolvimento de Sistemas (ADS) no **Senac**. Atualmente, o projeto encontra-se na **Segunda Etapa (Execução)**.

## Dashboard Online

Acesse o dashboard publicado: [clique aqui](https://projeto-integrador-dodphybvdpndcejzzmzmyy.streamlit.app)

---

<details>
  <summary><b>📂 Índice (Clique para expandir)</b></summary>
  
  1. [Integrantes do Grupo](#-integrantes-do-grupo)
  2. [Definição da Base de Dados](#-definição-da-base-de-dados)
  3. [Objetivos da Análise](#-objetivos-da-análise)
  4. [Planejamento e Cronograma](#-planejamento-das-tarefas-e-cronograma)
  5. [Transformações de Dados Aplicadas](#-transformações-de-dados-aplicadas)
  6. [Dashboard (Métricas e Visualizações)](#-dashboard-métricas-e-visualizações)
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
| **Aline Viana** | [Alineviana3589](https://github.com/Alineviana3589) |
| **João** | [euJonh](https://github.com/euJonh) |

---

## 🗄️ Definição da Base de Dados

O projeto utilizou dados que correlacionam o uso de mídias sociais com estados emocionais reportados pelos usuários.

* **Dataset:** [Social Media Usage and Emotional Well-Being](https://www.kaggle.com/datasets/emirhanai/social-media-usage-and-emotional-well-being)
* **Autor:** Julian Emirhan Bulut
* **Fonte:** Kaggle
* **Usabilidade:** 10.0 (Kaggle Score)
* **Armazenamento:** SQLite (garante portabilidade entre os integrantes)

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
| **2** | ETL: Limpeza de dados nulos e padronização com Pandas. | Guilherme Martins | ✅ Concluído |
| **3** | Persistência: Modelagem e carga dos dados no SQLite. | João | ✅ Concluído |
| **4** | Desenvolvimento do Dashboard interativo no Streamlit. | Ana Flávia Ortiz, Vitoria Gomez e Aline Viana | ✅ Concluído |
| **5** | Documentação final, testes e revisão técnica. | Todos | 🔜 Em andamento |

---

## 🛠️ Transformações de Dados Aplicadas

As seguintes transformações foram aplicadas via **Pandas** para garantir a qualidade da análise:

* **Limpeza:** Remoção de registros com valores de gênero inválidos e idades fora do intervalo esperado (10–100).
* **Deduplicação:** Identificação e remoção de linhas duplicadas entre os arquivos train, test e val.
* **Padronização:** Normalização dos nomes das plataformas e categorias de emoções (capitalização consistente).
* **Carga:** Exportação do DataFrame limpo para a tabela `tb_uso_redes_sociais` no banco SQLite.

---

## 🖥️ Dashboard (Métricas e Visualizações)

O dashboard foi desenvolvido em Streamlit e publicado em produção. Abaixo estão as visões implementadas:

### 1. Visão Geral (Filtros e KPIs)

Na barra lateral estão os filtros globais que afetam todos os gráficos simultaneamente:

- **Plataforma** — seleção múltipla entre as 7 redes sociais do dataset
- **Gênero** — seleção única: Todos, Feminino, Masculino ou Não-binário
- **Faixa Etária** — seleção única: Todas, 18–24, 25–34, 35–44 ou 45+
- **Cores por Emoção** — paleta customizável pelo usuário via color picker

**KPIs exibidos:**
- **Tempo médio de uso** — média de minutos diários no dataset filtrado
- **Emoção mais frequente** — emoção dominante entre os registros filtrados
- **Curtidas por dia** — média de curtidas recebidas por dia

<img width="1284" height="794" alt="Dashboard - KPIs e Associação por Plataforma" src="https://github.com/user-attachments/assets/ac039097-6f36-45f8-847f-529643469bdb" />

### 2. Análise por Eixo Temático

**Eixo 1: Associação por Plataforma**
Gráfico de barras empilhadas mostrando a distribuição de emoções dominantes em cada rede social. Permite identificar quais plataformas estão associadas a estados emocionais mais negativos ou positivos.

**Eixo 2: Exposição Temporal**
Gráfico de dispersão relacionando tempo de uso diário (eixo X) com volume de postagens por dia (eixo Y), com os pontos coloridos pela emoção dominante do usuário.

<img width="1324" height="634" alt="Dashboard - Exposição Temporal" src="https://github.com/user-attachments/assets/c927aa4c-9da9-431b-858c-28b931d56cf4" />

**Eixo 3: Engajamento e Recompensa**
Boxplot comparando a distribuição de curtidas recebidas por dia para cada emoção dominante, evidenciando se usuários com maior engajamento reportam emoções distintas.

<img width="1335" height="730" alt="Dashboard - Engajamento e Recompensa" src="https://github.com/user-attachments/assets/c69d38c7-bbf9-4f1c-b02c-cb0586e5f319" />

### 3. Feature Engineering aplicado

As seguintes transformações foram aplicadas durante o ETL:

1. **Faixa Etária (Binning):** Idades agrupadas em categorias (18–24, 25–34, 35–44, 45+)
2. **Tradução das categorias:** Emoções e gêneros traduzidos para português na camada de exibição, mantendo o banco de dados em inglês
3. **Limpeza de dados inválidos:** Remoção de registros com gênero e idade fora dos valores esperados do dataset

---

## 📄 Licença
Este projeto está licenciado sob a Licença MIT.
