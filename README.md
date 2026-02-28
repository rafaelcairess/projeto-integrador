# Impacto das Redes Sociais na Saúde Mental e no Bem-Estar Emocional

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?logo=pandas&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3.x-003B57?logo=sqlite&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?logo=streamlit&logoColor=white)

Este projeto de análise de dados foi desenvolvido como parte da disciplina de **Projeto Integrador: Desenvolvimento Low Code em Ciência de Dados** do curso de Análise e Desenvolvimento de Sistemas (ADS)

---

## 👥 Integrantes do Grupo

| Nome | GitHub |
| :--- | :--- |
| **Rafael Caires Pires** | [Perfil](https://github.com/rafaelcairess) |
| **Guilherme Martins** | [Perfil](https://github.com/Guifarmartins) |
| **Vitoria Gomez** | [Perfil](https://github.com/vitmgomez) |
| **Ana Flávia Ortiz** | — |
| **Aline Viana** | — |

---

## 🗄️ Definição da Base de Dados

A base de dados selecionada compreende métricas de comportamento digital e indicadores de bem-estar emocional auto-relatados.

* **Dataset:** *Social Media Usage and Emotional Well-Being*
* **Fonte:** Kaggle (Autor: emirhanai)
* **Qualidade de Usabilidade:** 10.0 (Kaggle Score)
* **Armazenamento:** SQLite (escolhido pela portabilidade e integração nativa com o ecossistema Python).

### Dicionário de Dados

| Variável | Descrição Técnica |
| :--- | :--- |
| `User_ID` | Identificador único do registro |
| `Age` | Idade do usuário |
| `Gender` | Gênero do usuário |
| `Platform` | Plataforma de rede social analisada |
| `Daily_Usage_Time` | Tempo médio de exposição diária (minutos) |
| `Posts_Per_Day` | Volume de postagens diárias |
| `Likes_Received_Per_Day` | Volume de curtidas recebidas por dia |
| `Dominant_Emotion` | Classificação da emoção predominante (ex: Ansiedade, Felicidade, Tristeza) |

---

## 🎯 Objetivos da Análise

A pesquisa busca identificar padrões estatísticos entre o consumo de conteúdo digital e a saúde mental, concentrando-se em:

1. **Associação por Plataforma:** Mapear a correlação entre plataformas específicas e o índice de emoções negativas.
2. **Exposição Temporal:** Analisar se o aumento no tempo de uso diário impacta diretamente no humor reportado.
3. **Validação Social:** Investigar a influência do engajamento (curtidas recebidas) no estado emocional do usuário.

---

## 📅 Planejamento de Execução

| Etapa | Atividades | Responsável |
| :--- | :--- | :--- |
| **I — Estruturação** | Criação do repositório, documentação inicial e configuração do dataset. | **Rafael Caires Pires** |
| **II — Processo de ETL** | Tratamento de dados nulos, padronização e limpeza de inconsistências. | A definir |
| **III — Persistência** | Modelagem e carga dos dados tratados no banco de dados SQLite. | A definir |
| **IV — Visualização** | Desenvolvimento do dashboard analítico em ambiente Streamlit. | A definir |
| **V — Entrega Final** | Testes de funcionalidade e revisão técnica. | Todos |

---

## 🖥️ Estrutura do Dashboard (Streamlit)

O painel interativo será organizado de forma modular para facilitar a interpretação dos resultados:

* **Painel de Indicadores (KPIs):** Volume total de amostras, emoção predominante e plataforma com maior retenção.
* **Análise Demográfica:** Distribuição de usuários segmentada por gênero, faixa etária e plataforma.
* **Correlação Plataforma x Emoção:** Análise comparativa para identificar tendências emocionais por rede social.
* **Análise de Exposição:** Gráfico de dispersão relacionando minutos de uso com a variação do humor.
* **Engajamento e Bem-Estar:** Estudo sobre o impacto quantitativo das curtidas na percepção emocional.
* **Consulta de Dados:** Módulo de dados brutos com filtros dinâmicos para auditoria.

---

## 🛠️ Tecnologias e Ferramentas

* **Linguagem:** Python 3.x
* **Manipulação de Dados:** Pandas
* **Armazenamento:** SQLite
* **Interface:** Streamlit
* **Controle de Versão:** Git / GitHub

---

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para detalhes.
