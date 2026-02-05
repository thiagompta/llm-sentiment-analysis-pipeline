from dotenv import load_dotenv
from groq import Groq
import pandas as pd
import csv
import os

load_dotenv()
client_groq = Groq(api_key=os.getenv("GROQ_API_KEY"))

df = pd.read_csv("reviews.csv")
sentimentos = []
def gerar_sentimento():
    for review in df["reviewText"]:
        response = client_groq.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[{"role": "user", "content": f"""Você irá analisar a resenha que eu te mandarei abaixo, e retorna com uma análise de sentimento.
                    Você deve responder APENAS com uma das seguintes palavras: 'Positiva', 'Negativa' ou 'Neutra',indicando o sentimento relativo aquela resenha específica.
                    Exemplos:"Eu adorei esse produto" -> Positiva
                    "Gostei, mas não é nada de especial" -> Neutra
                    "Odiei esse produto" -> Negativa'
                    Texto:{review}"""}],temperature=0)
        sentimento = response.choices[0].message.content.strip()
        sentimentos.append(sentimento) 

GERAR_SENTIMENTOS = False  # mude para True quando quiser gerar, condição para não gastar a IA KKK

if GERAR_SENTIMENTOS:
    gerar_sentimento()
    df["sentimento"] = sentimentos
    df.to_csv("reviews_com_sentimento.csv", index=False)
else:
    df = pd.read_csv("reviews_com_sentimento.csv")
df_negativas = df[df["sentimento"] == 'Negativa']
df_negativas_unidas = "#####".join(df_negativas["reviewText"])
resposta = client_groq.chat.completions.create(model="openai/gpt-oss-20b", 
                                               messages=[{"role": "user", "content":f"""Você vai receber varias resenhas negativas de analises de um produto
                                               e eu quero que encontre as categorias diferentes para os tipos de reclamações. Cada categoria deve ser definida por UMA UNICA PALAVRA.
                                                          Depois, eu quero que você me retorne APENAS um texto no formato JSON, contendo apenas três chaves:
                                                          -'resenha_original': irá conter a renhas original em inglês.
                                                          -'resenha_pt': irá conter a resenha traduzida para o português;
                                                          -'categoria': ira conter a categoria dentre as 5 definidas por você em que a resenha se encaixa.
                                                          não esqueça de listar quais as categorias que você escolheu.
                                               Segue as resenhas separadas por ##### e as respostas precisam ser em portugues BR {df_negativas_unidas}"""}],temperature=0)
palavras = resposta.choices[0].message.content
print (palavras)
