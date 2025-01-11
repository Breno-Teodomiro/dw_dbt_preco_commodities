# ========== Import bibliotecas ========== #


import os
import pandas as pd
import yfinance as yf

from sqlalchemy import create_engine
from dotenv import load_dotenv

# ========== Import variaveis de ambiente  ========== #



# ========== Extrair cotação de ativos  ========== #
# CL=F ==> Petroleo
# GC=F ==> Ouro
# SI=F ==> Prata
commodities = ['CL=F', 'GC=F', 'SI=F']

def buscar_dados_commodities(simbolo, periodo = '5y', intervalo = '1d'):
    ticker = yf.Ticker('CL=F')
    dados = ticker.history(period = periodo, interval = intervalo)[['Close']]
    dados['simbolo'] = simbolo 
    return dados

print(consultar_commodities('CL=F'))


# ========== Concatenar Ativos (1..2...3) ==> (1) ========== #


