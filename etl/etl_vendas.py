import pandas as pd
import sqlite3
import os

# Caminhos
csv_path = './data/vendas.csv'
db_path = './database/vendas.db'

# Criar diretório se não existir
os.makedirs('./database', exist_ok=True)

# Ler CSV
df = pd.read_csv(csv_path, parse_dates=['data'])

# Limpeza básica
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# Criar conexão SQLite
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Criar tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS vendas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data TEXT,
        produto TEXT,
        categoria TEXT,
        preco REAL,
        quantidade INTEGER
    )
''')

# Inserir dados
df.to_sql('vendas', conn, if_exists='replace', index=False)

print("ETL finalizado com sucesso!")

conn.commit()
conn.close()
