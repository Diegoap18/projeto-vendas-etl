# 🧼 Projeto de Engenharia de Dados: ETL + Dashboard de Vendas

Este projeto simula um pequeno fluxo de dados de vendas com etapas de ETL e visualização analítica. Ideal para quem está começando na área de Engenharia de Dados.

## 🚀 Funcionalidades

- Leitura de dados de vendas (CSV)
- Limpeza de dados com Pandas
- Armazenamento em banco SQLite
- Visualização de dados com gráficos (matplotlib/seaborn)
- Código simples, comentado e modularizado

## 📁 Estrutura do Projeto

projeto_vendas/ <br>
│ ├── data/ <br>
│ └── vendas.csv # Arquivo de dados de entrada <br>
│ ├── database/ <br>
│ └── vendas.db # Banco de dados SQLite gerado <br>
│ ├── etl/ │ └── etl_vendas.py # Script de ETL <br>
│ ├── dashboard/ <br>
│ └── dashboard_vendas.ipynb # Notebook de visualização <br>
│ ├── requirements.txt # Dependências do projeto <br>
├── .gitignore # Ignora arquivos sensíveis e de ambiente <br>
└── README.md <br>
## 📦 Requisitos

- Python 3.9+
- Jupyter Notebook
- Bibliotecas listadas no `requirements.txt`

## 🔧 Como usar

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/projeto-vendas-etl.git
cd projeto-vendas-etl
```

2.Instale as dependências:

```bash
pip install -r requirements.txt
```

3.Execute o script de ETL:

```bash
python etl/etl_vendas.py
```
4.Abra o notebook de visualização:

```bash
jupyter notebook dashboard/dashboard_vendas.ipynb
```

## 📊 Exemplo de Gráficos:
- Vendas por Produto 
- Distribuição por Categoria
- Evolução de Vendas por Dia

## 🧠 Ideal Para:
- Prática de conceitos iniciais de ETL
- Iniciantes em Engenharia de Dados
- Estudo de visualização básica com Python


