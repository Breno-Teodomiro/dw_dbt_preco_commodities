# ========== Import bibliotecas ========== #
import os
import pandas as pd
import yfinance as yf

from sqlalchemy import create_engine
from dotenv import load_dotenv

# ========== Import variaveis de ambiente  ========== #

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_SCHEMA = os.getenv('DB_SCHEMA')

DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_engine(DATABASE_URL)

# ========== Extrair cotação de ativos  ========== #
# CL=F ==> Petroleo
# GC=F ==> Ouro
# SI=F ==> Prata
commodities = ['CL=F', 'GC=F', 'SI=F'] #EQTL3



def buscar_dados_commodities(simbolo, periodo = '1mo', intervalo = '1d'):
    ticker = yf.Ticker(simbolo)
    dados = ticker.history(period = periodo, interval = intervalo)[['Close']]
    dados['simbolo'] = simbolo 
    return dados

def buscar_todos_dados_commodities(commodities):
    todos_dados = []
    for simbolo in commodities:
        dados = buscar_dados_commodities(simbolo)
        todos_dados.append(dados)
    return pd.concat(todos_dados)

def salvar_no_postgres(df, schema='public'):
    df.to_sql('commodities', engine, if_exists='replace', index=True, index_label='Data', schema=schema)

if __name__ == '__main__':
    # Buscar dados de todas as commodities
    dados_commodities = buscar_todos_dados_commodities(commodities)
    
    # Salvar os dados no PostgreSQL
    salvar_no_postgres(dados_commodities)



# ========== Concatenar Ativos (1..2...3) ==> (1) ========== #


