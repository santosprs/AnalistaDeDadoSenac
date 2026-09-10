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

print('-'*20)
print(tabela_filmes.loc['B'])
print('-'*20)
print(tabela_filmes.iloc[1:3])
print(tabela_filmes.loc['B':'E'])
print('-'*20)
consulta1 = tabela_filmes.query("faturamento == 5.5")
print(consulta1)
#print(tabela_filmes.query["faturamento (milhões)" == 5.5] #não lê
# print(tabela_filmes.query['ano' == 1995])  ###não lê



# print(serie_impares)

# quadrado_serie_impares = serie_impares*serie_impares
# print(quadrado_serie_impares)


#leitura de arquivos

# leitura_invest = pd.read_excel("base_invest.xlsx")
# print(leitura_invest)