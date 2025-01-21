import pandas as pd
import random
from faker import Faker
from datetime import timedelta
from datetime import date

# Instância do Faker
fake = Faker('pt_BR')
Faker.seed(42)
random.seed(42)

# Lista de IDs de produtos a serem excluídos das vendas
produtos_excluidos = {4, 7, 9, 14, 34}

# IDs de produtos que não estão na tabela de produtos
produtos_fora_catalogo = [80, 123, 444]

# Gerar tabela de vendas com sazonalidade e distribuição não uniforme
def gerar_tabela_vendas():
    vendas = []
    inicio = pd.Timestamp('2013-01-01')
    fim = pd.Timestamp('2023-12-31')

    # Produtos populares (1 a 10)
    produtos_populares = list(range(1, 11))

    # Loop por cada mês nos últimos 10 anos
    data_atual = inicio
    while data_atual <= fim:
        mes = data_atual.month

        # Definir o número de vendas com sazonalidade
        if mes == 11:  # Black Friday
            num_vendas = random.randint(2000, 3000)
        elif mes == 2:  # Volta às aulas / Carnaval
            num_vendas = random.randint(1500, 2500)
        else:
            num_vendas = random.randint(1000, 1500)

        # Gerar vendas para o mês atual
        for _ in range(num_vendas):
            # Selecionar produtos do catálogo ou fora dele
            if random.random() < 0.95:  # 95% de chance de escolher produtos do catálogo
                id_produto = random.choices(
                    population=range(1, 51),  # Todos os produtos
                    weights=[5 if p in produtos_populares else 1 for p in range(1, 51)],
                    k=1
                )[0]
                # Excluir produtos com IDs indesejados
                if id_produto in produtos_excluidos:
                    continue
            else:  # 5% de chance de escolher produtos fora do catálogo
                id_produto = random.choice(produtos_fora_catalogo)

            vendas.append({
                'id_venda': len(vendas) + 1,
                'id_cliente': random.randint(1, 500),  # 500 clientes únicos
                'id_produto': id_produto,
                'quantidade': random.randint(1, 5),
                'data_venda': fake.date_between(start_date=data_atual, end_date=data_atual + timedelta(days=30))
            })

        # Avançar para o próximo mês
        data_atual += pd.DateOffset(months=1)
    return pd.DataFrame(vendas)

# Gerar tabela de clientes com nomes separados
def gerar_tabela_clientes():
    clientes = []
    for i in range(1, 501):  # 500 clientes únicos
        nome_completo = fake.name()
        partes = nome_completo.split()
        primeiro_nome = partes[0]
        ultimo_nome = partes[-1]
        segundo_nome = " ".join(partes[1:-1]) if len(partes) > 2 else None
        clientes.append({
            'id_cliente': i,
            'primeiro_nome': primeiro_nome,
            'segundo_nome': segundo_nome,
            'ultimo_nome': ultimo_nome,
            'cidade': fake.city(),
            'idade': random.randint(18, 65),
            'data_cadastro': fake.date_between(start_date=date(2012, 1, 1), end_date=date(2023, 1, 1))
        })
    return pd.DataFrame(clientes)

# Gerar tabela de produtos com preços condizentes
def gerar_tabela_produtos():
    produtos = []
    categorias = {
        'Eletrônicos': (500, 2000),
        'Móveis': (200, 1000),
        'Roupas': (50, 300),
        'Beleza': (20, 150),
        'Alimentos': (10, 100)
    }

    for i in range(1, 51):  # 50 produtos únicos
        categoria = random.choice(list(categorias.keys()))
        preco_min, preco_max = categorias[categoria]
        produtos.append({
            'id_produto': i,
            'nome_produto': fake.word().capitalize(),
            'categoria': categoria,
            'preco_unitario': round(random.uniform(preco_min, preco_max), 2)
        })
    return pd.DataFrame(produtos)

# Gerando as tabelas
tabela_vendas = gerar_tabela_vendas()
tabela_clientes = gerar_tabela_clientes()
tabela_produtos = gerar_tabela_produtos()

# Exibindo uma amostra dos dados gerados
print("Tabela de Vendas:")
print(tabela_vendas.head())
print("\nTabela de Clientes:")
print(tabela_clientes.head())
print("\nTabela de Produtos:")
print(tabela_produtos.head())

# Salvando as tabelas em arquivos CSV
tabela_vendas.to_csv('tabela_vendas.csv', index=False)
tabela_clientes.to_csv('tabela_clientes.csv', index=False)
tabela_produtos.to_csv('tabela_produtos.csv', index=False)
