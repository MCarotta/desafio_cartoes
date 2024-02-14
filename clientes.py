#%%
# importar biblioteca pandas. 
import pandas as pd

# Leitura do arquivo CSV
tabela = pd.read_csv('C:\\Users\\mcaro\\Google Drive\\Hashtag\\ClientesBanco.csv', encoding='latin1')

# Exibição da tabela
print(tabela)


# %%
# Listar informações da tabela
print(tabela.info())


# %%
# Remover linhas "na" da tabela
import pandas as pd
tabela = pd.read_csv('C:\\Users\\mcaro\\Google Drive\\Hashtag\\ClientesBanco.csv', encoding='latin1')
tabela = tabela.dropna()
print(tabela.info())


# %%
# Exibindo as principais estatíticas da tabela
import pandas as pd
tabela = pd.read_csv('C:\\Users\\mcaro\\Google Drive\\Hashtag\\ClientesBanco.csv', encoding='latin1')
tabela = tabela.dropna()
print(tabela.describe())


# %%
# Exibindo as principais estatísticas da tabela com duas casas decimais
import pandas as pd
tabela = pd.read_csv('C:\\Users\\mcaro\\Google Drive\\Hashtag\\ClientesBanco.csv', encoding='latin1')
tabela = tabela.dropna()
print(tabela.describe(). round(2))


# %%
# Quantidade de clientes Ativos versus Cancelados
qtd_categoria = tabela['Categoria'].value_counts()
print(qtd_categoria)


# %%
# Percentual de clientes Ativos versus Cancelados
perc_categoria = tabela['Categoria'].value_counts(normalize=True).round(2)
print(perc_categoria)

# %%
# Comparando: Clientes Ativos versus Clientes Cancelados
# Histograma Contagem de Clientes x Idade
import plotly.express as px
grafico = px.histogram(tabela, x='Idade', color='Categoria')
grafico.show()


# %%
# Listando todas as colunas da tabela
import plotly.express as px
for coluna in tabela:
    print(coluna)


# %%
# Comparando: Clientes Ativos versus Clientes Cancelados
# Histogramas diversos com todas as variaveis das colunas
import plotly.express as px
for coluna in tabela:
    print(coluna)
    grafico = px.histogram(tabela, x=coluna, color='Categoria', title=f'Histograma de {coluna}', width=700, height=500)
    grafico.show()
# %%
