import sqlite3
import pandas as pd
from datetime import datetime
import sys
import os

# Adiciona o diretório src ao PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from src.load.load import save_to_db

df = pd.read_json('data/data.jsonl', lines=True)

# Setar o pandas para mostrar todas as colunas
pd.options.display.max_columns = None

def correct_price_format(price):
    # Se já for numérico, retorna como float
    if isinstance(price, (int, float)):
        return float(price)
    
    # Remove R$, espaços e caracteres não numéricos
    price_str = str(price).replace('R$', '').replace(' ', '')
    
    # Se o preço não tem separadores, retorna direto como float
    if '.' not in price_str and ',' not in price_str:
        return float(price_str)
    
    # Verifica se é formato brasileiro (1.149,00) ou americano (1,149.00)
    if '.' in price_str and ',' in price_str:  # Formato brasileiro
        price_str = price_str.replace('.', '').replace(',', '.')
    elif ',' in price_str and '.' in price_str:  # Formato americano (improvável no ML)
        price_str = price_str.replace(',', '')
    elif price_str.count('.') == 1 and len(price_str.split('.')[1]) == 3:  # Caso 1.149
        price_str = price_str.replace('.', '')
    
    return float(price_str)



df['_datetime'] = datetime.now()
df['_source'] = "https://lista.mercadolivre.com.br/celular"

# Tratar nulos
df['old_price'] = df['old_price'].fillna('0')
df['new_price'] = df['new_price'].fillna('0')
df['reviews_rating_number'] = df['reviews_rating_number'].fillna('0')
df['reviews_amount'] = df['reviews_amount'].fillna('(0)')

# Garantir que estão como strings antes de usar .str
df['old_price'] = df['old_price'].apply(correct_price_format)
df['new_price'] = df['new_price'].apply(correct_price_format)
df['reviews_amount'] = df['reviews_amount'].astype(str).str.replace(r'[\(\)]', '', regex=True)

# Converter para números
df['old_price'] = df['old_price'].astype(float)
df['new_price'] = df['new_price'].astype(float)
df['reviews_rating_number'] = df['reviews_rating_number'].astype(float)
df['reviews_amount'] = df['reviews_amount'].astype(int)



# Tratar os preços como floats e calcular os valores totais
# Manter apenas produtos com preço entre 1000 e 10000 reais
df = df[
    (df['old_price'] >= 400) & (df['old_price'] <= 10000) &
    (df['new_price'] >= 400) & (df['new_price'] <= 10000)
]

# print(df)

# Conectar ao banco de dados SQLite (ou criar um novo)
save_to_db(df, 'data/phones.db')