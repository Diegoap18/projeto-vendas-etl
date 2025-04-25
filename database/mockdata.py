import pandas as pd
import random
from datetime import datetime, timedelta
import os

# Parâmetros para geração dos dados
num_registros = 1000
start_date = datetime(2025, 1, 1)
produtos = [
    ("Camiseta", "Acessórios", 29.90),
    ("Notebook", "Eletrônicos", 3500.00),
    ("Mouse", "Eletrônicos", 99.90),
    ("Tênis", "Calçados", 199.90),
    ("Fone de Ouvido", "Eletrônicos", 149.90),
    ("Calça Jeans", "Roupas", 139.90),
    ("Smartphone", "Eletrônicos", 2500.00),
    ("Sandália", "Calçados", 89.90),
    ("Relógio", "Acessórios", 299.90),
    ("Jaqueta", "Roupas", 229.90)
]

# Geração de dados
data = []
for _ in range(num_registros):
    data_venda = start_date + timedelta(days=random.randint(0, 30))
    produto, categoria, preco = random.choice(produtos)
    quantidade = random.randint(1, 5)
    data.append([data_venda.strftime('%Y-%m-%d'), produto, categoria, preco, quantidade])

# Criar DataFrame
df = pd.DataFrame(data, columns=["data", "produto", "categoria", "preco", "quantidade"])

# Criar pasta 'data' se não existir
os.makedirs("data", exist_ok=True)

# Salvar em CSV
df.to_csv("data/vendas.csv", index=False)

print("Dados gerados com sucesso!")

