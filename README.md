# LLM Sentiment Analysis Pipeline

Este repositório apresenta um **estudo prático de uso de Large Language Models (LLMs)** aplicados à **análise de sentimento e categorização de feedbacks de usuários**, utilizando **Python, Pandas e a API da Groq**.

O projeto simula um cenário real de **análise de reviews de produtos**, passando por todas as etapas de um pipeline moderno de NLP com LLMs.

---

## 📌 Objetivos do Projeto

- Ler e manipular dados estruturados a partir de arquivos CSV
- Classificar automaticamente o **sentimento de reviews** (Positiva, Negativa ou Neutra)
- Persistir os resultados em um novo dataset
- Filtrar reviews negativas
- Agrupar e analisar reclamações recorrentes
- Extrair **categorias de reclamações** usando LLM
- Aplicar boas práticas de controle de custo, idempotência e reutilização de código

---

## 🧠 Conceitos Trabalhados

- NLP (Natural Language Processing)
- Análise de Sentimento
- Prompt Engineering
- Pós-processamento de respostas de LLM
- Pipeline de dados com Pandas
- Controle de execução de IA (flags)
- Tratamento de Rate Limit
- Normalização de texto
- Extração de insights (Voice of Customer)

---

## 🗂 Estrutura do Projeto
├── csv/
├── modulo-6/
├── .env
├── .gitignore
├── desafio.py
├── main.py
├── reviews.csv
├── reviews_com_sentimento.csv


---

## ⚙️ Tecnologias Utilizadas

- Python 3.10+
- Pandas
- Groq API
- Modelo: `openai/gpt-oss-20b`
- python-dotenv

---

## 🔑 Configuração do Ambiente

1. Clone o repositório
2. Crie um arquivo `.env` na raiz do projeto:
   
```env
GROQ_API_KEY=your_api_key_here
🚀 Funcionalidades
✔ Classificação de Sentimento

Cada review é classificada como:

Positiva

Negativa

Neutra

O resultado é salvo no arquivo:

reviews_com_sentimento.csv

✔ Controle de Execução da IA

Para evitar uso desnecessário de tokens, o pipeline permite ativar/desativar chamadas ao LLM:

GERAR_SENTIMENTOS = False

✔ Análise de Reclamações Negativas

Filtragem automática de reviews negativas

Agrupamento dos textos

Extração de 5 categorias principais de reclamações, cada uma representada por uma única palavra

Exemplo de saída:

['Durabilidade', 'Velocidade', 'Compatibilidade', 'Capacidade', 'Suporte']

📊 Casos de Uso Reais

Análise de feedback de clientes

Monitoramento de satisfação

Identificação de pontos críticos em produtos

Estudos de UX / CX

Pré-processamento de dados para BI

🧩 Aprendizados Principais

LLMs devem ser usados com contrato de saída bem definido

Nunca confiar no formato bruto da resposta

Separar geração de dados de análise

Controlar custo e volume de tokens

Pipelines de NLP precisam ser reprodutíveis e seguros

👨‍💻 Autor

Projeto desenvolvido como estudo prático de Engenharia de IA / NLP com LLMs, focado em aplicação real e boas práticas de produção.