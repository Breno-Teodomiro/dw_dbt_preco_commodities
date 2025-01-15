# ========== Import bibliotecas ========== #
import os
import pandas as pd
import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError
from dotenv import load_dotenv

# ========== Import variaveis de ambiente  ========== #

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Obter as variáveis do arquivo .env
DB_HOST = os.getenv('POSTGRES_HOST')
DB_PORT = os.getenv('POSTGRES_PORT')
DB_NAME = os.getenv('POSTGRES_DB')
DB_USER = os.getenv('POSTGRES_USER')
DB_PASS = os.getenv('POSTGRES_PASSWORD')

if not all([DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASS]):
    raise ValueError("Uma ou mais variáveis de ambiente do banco de dados não estão definidas no arquivo .env")

# Criar a URL de conexão do banco de dados
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Criar o engine de conexão com o banco de dados
engine = create_engine(DATABASE_URL)

# ========== Extrair dados  ========== #

def get_data():
    query = f"""
    SELECT
        *
    FROM
        public.dm_commodities;
    """
    df = pd.read_sql(query, engine)
    return df

# Configurar a página do Streamlit
st.set_page_config(page_title='Dashboard do diretor', layout='wide')

# Título do Dashboard
st.title('Esse e um texto')

# Descrição
st.write("""
Este dashboard mostra os dados de commodities e suas transações.
""")

# Obter os dados
df = get_data()

st.dataframe(df)