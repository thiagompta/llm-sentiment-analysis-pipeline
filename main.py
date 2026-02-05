import os
from dotenv import load_dotenv
from groq import Groq
from google import genai
import pandas as pd
import csv
import random
import numpy as np

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
client_groq = Groq(api_key=os.getenv("GROQ_API_KEY"))

def gerar_dados():
    produtos = ["Notebook", "Smartphone", "Fone de Ouvido", "Monitor", "Teclado","Mouse", "Impressora", "Tablet", "Smartwatch", "Câmera"]
    categorias = ["Eletrônicos", "Informática", "Acessórios", "Periféricos"]
    dados = []
    for _ in range(50):
        dados.append({
            "produto": random.choice(produtos),
            "categoria": random.choice(categorias),
            "preco": round(random.uniform(50, 5000), 2),          # preço em reais
            "quantidade_vendida": random.randint(1, 1000),         # unidades vendidas
            "avaliacao": round(random.uniform(1, 5), 1)          # nota de 1 a 5
        })
    df = pd.DataFrame(dados)
    df.to_csv("produtos.csv", index=False, encoding="utf-8-sig")

df = pd.read_csv("produtos.csv")
df.index = df.index + 1
#print(df[df['categoria'] == 'Eletrônicos']) somente produtos de categoria eletronicos
#print(df[df['avaliacao'] < 2.0]) pordutos com avaliacão menor que 2
#print(df[(df['categoria'] == 'Eletrônicos') & (df['preco'] >= 1000)]) produtos da categoria eletrônicos maior R$1000
#print(df.iloc[10:20]) produtos da linha 11 até a 20
df_indice = df.set_index("produto")

def ajustar_indice_produto(df_indice):
    df_indice = df_indice.copy()
    df_indice.index = [f"Produto {i}" for i in range(1, len(df_indice) + 1)]
    return df_indice

df_indice = ajustar_indice_produto(df_indice)

print(df_indice)
