#aula1#

import pandas as pd #alias 'pd'
import numpy as np #alias 'np'
import openpyxl

numeros_impares = [43,55,1,3,11,27,109]
numeros_seq = [2,3,4,5,6,6,7]
#print(type(numeros_impares))

serie_impares = pd.Series(numeros_impares)
# #print(serie_impares)
# print(type(serie_impares))

# print(serie_impares[3])

# print(serie_impares.sum())
# print(serie_impares.median())
# print(serie_impares.min())
# print(serie_impares.max())
# print(len(serie_impares))
# print(serie_impares.describe())
# print(serie_impares[serie_impares>50])

serie2_impares = pd.Series(numeros_impares,index = ['a','b','c','d','e','f','g'])
# print(serie2_impares)


#aula2#

filmes = {
    'titulo':["Lagoa Azul","Agente Secreto","Genio Indomavel","A Freira","Brinquedo Assasino","Top Gun"],
    'categoria':["romance","ação","Drama","Terror","Comedia","Aventura"],
    'ano':["1980","2025","1997","2018","1988","1996"],
    'faturamento': [6,5,4,2,3,7]
}

indices = ['A','B','C','D','E','F']

tabela_filmes = pd.DataFrame(filmes,index=indices)


# print(type(tabela_filmes))
# print(tabela_filmes)
# print(type(tabela_filmes))
# print(tabela_filmes)
# print(type(tabela_filmes))

# print('-'*20)
# print(tabela_filmes.loc['B'])
# print('-'*20)
# print(tabela_filmes.iloc[1:3])
# print(tabela_filmes.loc['B':'E'])
# print('-'*20)
# consulta1 = tabela_filmes.query("faturamento == 5.5")
# print(consulta1)
#print(tabela_filmes.query["faturamento (milhões)" == 5.5] #não lê
# print(tabela_filmes.query['ano' == 1995])  ###não lê



# print(serie_impares)

# quadrado_serie_impares = serie_impares*serie_impares
# print(quadrado_serie_impares)


#leitura de arquivos

# leitura_invest = pd.read_excel("base_invest.xlsx")
# print(leitura_invest)  



#Aula3## #steamdb#

df_transacoes = pd.read_excel('base_invest.xlsx', sheet_name='Transacoes')
df_ativo = pd.read_excel('base_invest.xlsx', sheet_name='Ativo')

#max min
#pergunta1##

# df_compra = df_transacoes[df_transacoes['operacao']== 'compra']
# df_venda = df_transacoes[df_transacoes['operacao']== 'venda']

# max_compra_preco = df_compra['preco'].max()
# min_compra_preco =df_compra['preco'].min()
# max_venda_preco = df_venda['preco'].max()
# min_venda_preco = df_venda['preco'].min()
# print(max_compra_preco)

#pergunta2##

df_transacoes['valor_total'] = df_transacoes['quantidade'] * df_transacoes['preco']
#print(df_transacoes)

valor_por_ativo = df_transacoes.groupby('id_ativo')['valor_total'].sum()
print(valor_por_ativo)
id_ativo_maior_valor = valor_por_ativo.idxmax()
print(id_ativo_maior_valor)
cnpj_maior_valor = df_ativo[df_ativo['id_ativo'] == id_ativo_maior_valor]['cnpj'].iloc[0]

print(" ---CNPJ com o ativo de maior valor ---")
print(f"O CNPJ para o ativo com o maior valor total é; {cnpj_maior_valor}")
print("\n")


#pergunta3##

