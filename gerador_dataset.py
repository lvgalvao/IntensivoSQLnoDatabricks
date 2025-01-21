import pandas as pd
import random
from faker import Faker

# Instância do Faker
fake = Faker('pt_BR')
Faker.seed(42)
random.seed(42)

# Tabela 1: Vendas
def gerar_tabela_vendas():
    vendas = []
    for i in range(1, 1001):  # 1000 vendas
        vendas.append({
            'id_venda': i,
            'id_cliente': random.randint(1, 50),  # 50 clientes únicos
            'id_produto': random.randint(1, 20),  # 20 produtos únicos
            'quantidade': random.randint(1, 5),
            'valor_venda': round(random.uniform(10, 500), 2),
            'data_venda': fake.date_between(start_date='-1y', end_date='today')
        })
    return pd.DataFrame(vendas)

# Tabela 2: Clientes
def gerar_tabela_clientes():
    clientes = []
    for i in range(1, 51):  # 50 clientes únicos
        clientes.append({
            'id_cliente': i,
            'nome_cliente': fake.name(),
            'cidade': fake.city(),
            'idade': random.randint(18, 65),
            'data_cadastro': fake.date_between(start_date='-2y', end_date='-1y')
        })
    return pd.DataFrame(clientes)

# Tabela 3: Produtos
def gerar_tabela_produtos():
    produtos = []
    for i in range(1, 21):  # 20 produtos únicos
        produtos.append({
            'id_produto': i,
            'nome_produto': fake.word().capitalize(),
            'categoria': random.choice(['Eletrônicos', 'Móveis', 'Roupas', 'Beleza', 'Alimentos']),
            'preco_unitario': round(random.uniform(20, 1000), 2)
        })
    return pd.DataFrame(produtos)

# Gerando as tabelas
tabela_vendas = gerar_tabela_vendas()
tabela_clientes = gerar_tabela_clientes()
tabela_produtos = gerar_tabela_produtos()

# Exibindo as tabelas
print("Tabela de Vendas")
print(tabela_vendas.head())
print("\nTabela de Clientes")
print(tabela_clientes.head())
print("\nTabela de Produtos")
print(tabela_produtos.head())

# Salvando as tabelas em CSV para uso posterior
tabela_vendas.to_csv('tabela_vendas.csv', index=False)
tabela_clientes.to_csv('tabela_clientes.csv', index=False)
tabela_produtos.to_csv('tabela_produtos.csv', index=False)
