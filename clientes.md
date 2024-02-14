
### Desafio
#### Em uma empresa de cartões de crédito, o número de clientes que cancelam seus cartões têm aumentado significativamente. Quais insights você pode extrair a partir da base de dados disponibilizada no link abaixo:

#### Referência: https://www.kaggle.com/sakshigoyal7/credit-card-customers

### O que temos?

#### A base de dados possui informações dos clientes ativos e cancelados.

### Iniciando a análise

#### Todas as análises foram feitas em Python 3.12 a partir do VSCode em uma máquina Windows

1. Importar a biblioteca Pandas e exibir dados da tabela

```python
import pandas as pd

# Carrega os dados do arquivo CSV
tabela = pd.read_csv('C:\\Users\\mcaro\\Google Drive\\Hashtag\\ClientesBanco.csv', encoding='latin1')

# Exibe uma amostra da tabela de dados usando print()
print(tabela)
```

2. Listar informações da tabela

```python
# Exibe o tipo de dado em cada coluna da tabela
print(tabela.info())
```

3. Remover linhas com dados faltantes

```python
# Remover linhas "na" da tabela
import pandas as pd
tabela = pd.read_csv('C:\\Users\\mcaro\\Google Drive\\Hashtag\\ClientesBanco.csv', encoding='latin1')
tabela = tabela.dropna()
print(tabela.info())
```

4. Exibir as principais estatísticas das variávei de dados

```python
# Exibindo as principais estatíticas da tabela
import pandas as pd
tabela = pd.read_csv('C:\\Users\\mcaro\\Google Drive\\Hashtag\\ClientesBanco.csv', encoding='latin1')
tabela = tabela.dropna()
print(tabela.describe())
```

5. Exibir principais estatísticas das variávei de dados com duas casas decimais

```python
# Exibindo as principais estatíticas da tabela
import pandas as pd
tabela = pd.read_csv('C:\\Users\\mcaro\\Google Drive\\Hashtag\\ClientesBanco.csv', encoding='latin1')
tabela = tabela.dropna()
print(tabela.describe(). round(2))
```

6. Quantificar Clientes Ativos e Clientes Cancelados

```python
# Quantidade de clientes Ativos versus Cancelados
qtd_categoria = tabela['Categoria'].value_counts()
print(qtd_categoria)

# Percentual de clientes Ativos versus Cancelados
perc_categoria = tabela['Categoria'].value_counts(normalize=True).round(2)
print(perc_categoria)
```

7. Comparando: Clientes Ativos versus Clientes Cancelados

```python
# Histograma Contagem de Clientes x Idade
import plotly.express as px
grafico = px.histogram(tabela, x='Idade', color='Categoria')
grafico.show()
```

8. Exibir colunas da tabela

```python
# Listando colunas da tabela
import plotly.express as px
for coluna in tabela:
    print(coluna)
```

9. Exibir histograma de clientes Ativos versus Cancelados a partir das variaveis de colunas

```python
# Histogramas diversos com todas as variaveis das colunas
import plotly.express as px
for coluna in tabela:
    print(coluna)
    grafico = px.histogram(tabela, x=coluna, color='Categoria', title=f'Histograma de {coluna}', width=700, height=500)
    grafico.show()
```
