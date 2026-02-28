# 🧠 Impacto das Redes Sociais na Saúde Mental e no Bem-Estar Emocional

![GitHub License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)

Este projeto foi desenvolvido para a disciplina de **Projeto Integrador (PI) — Desenvolvimento Low Code em Ciência de Dados** do curso de ADS no **Senac EAD**. O objetivo é analisar como diferentes plataformas e padrões de uso de redes sociais influenciam o estado emocional dos usuários.

---

## 👥 Integrantes

| Nome | GitHub |
| :--- | :--- |
| **Rafael Caires Pires** | [RafaelCairesPires](https://github.com/RafaelCairesPires) |
| **Guilherme Martins** | — |
| **Vitoria Gomez** | [@vitmgomez](https://github.com/vitmgomez) |
| **Ana Flávia Ortiz** | — |
| **Aline Viana** | — |

---

## 🗄️ Definição da Base de Dados

O dataset escolhido oferece uma visão detalhada do comportamento digital e sentimentos auto-relatados.

* **Fonte:** [Kaggle — Social Media Usage and Emotional Well-Being](https://www.kaggle.com/datasets/emirhanai/social-media-usage-and-emotional-well-being)
* **Usabilidade:** 10.0 ⭐
* **Armazenamento:** SQLite (escolhido pela leveza e integração nativa com Python/Pandas).

### Colunas do Dataset

| Coluna | Descrição |
| :--- | :--- |
| `User_ID` | Identificador único do usuário |
| `Age` | Idade |
| `Gender` | Gênero |
| `Platform` | Plataforma utilizada (Instagram, TikTok, etc.) |
| `Daily_Usage_Time` | Tempo de uso diário (em minutos) |
| `Posts_Per_Day` | Número de publicações diárias |
| `Likes_Received_Per_Day` | Curtidas recebidas por dia |
| `Dominant_Emotion` | Emoção predominante (Ex: Feliz, Ansioso, Triste) |

> **Justificativa:** A escolha do SQLite permite um fluxo de ETL (Extract, Transform, Load) simplificado, utilizando o método `to_sql` do Pandas, ideal para projetos ágeis sem a necessidade de servidores de banco de dados complexos.

---

## 🎯 Objetivo da Análise

Investigar a correlação entre o engajamento digital e a saúde mental através de três eixos fundamentais:

1.  **Impacto por Plataforma:** Identificar quais redes possuem maior associação com emoções negativas.
2.  **Tempo de Uso:** Verificar se a exposição prolongada degrada o humor geral.
3.  **Engajamento Social:** Analisar se a validação externa (curtidas) influencia a emoção dominante.

---

## 📅 Planejamento das Tarefas

| Etapa | Descrição | Responsável |
| :--- | :--- | :--- |
| **1 — Estruturação** | Repositório, Dataset e Documentação (README) | **Rafael Caires Pires** |
| **2 — ETL** | Limpeza, padronização e tratamento com Pandas | A definir |
| **3 — Storage** | Carregamento dos dados no SQLite | A definir |
| **4 — Dashboard** | Desenvolvimento da interface no Streamlit | A definir |
| **5 — Finalização** | Revisão, testes e gravação da apresentação | **Todos** |

---

## 🖥️ Arquitetura do Dashboard (Streamlit)

O dashboard será dividido em abas estratégicas para facilitar a interpretação:

* **📊 Sumário (Cards):** Total de usuários, emoção predominante e plataforma com maior tempo de uso.
* **📈 Perfil dos Usuários:** Distribuição por gênero, idade e plataforma.
* **😰 Plataforma x Emoção:** Cruzamento de dados para identificar tendências emocionais por app.
* **⏱️ Tempo de Uso x Humor:** Gráfico de dispersão analisando a correlação entre minutos online e humor.
* **❤️ Curtidas x Bem-Estar:** Comparação entre engajamento recebido e estado emocional.
* **📋 Dados Brutos:** Tabela completa com filtros dinâmicos para exploração livre.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python
* **Manipulação de Dados:** Pandas
* **Banco de Dados:** SQLite
* **Visualização:** Streamlit
* **Versionamento:** GitHub

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---
*Este projeto é parte integrante da formação acadêmica no Senac EAD.*
