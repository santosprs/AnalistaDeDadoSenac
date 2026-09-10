import pandas as pd 
import numpy as np 

filmes = {
    'titulo':["Lagoa Azul","Agente Secreto","Genio Indomavel"],
    'categoria':["romance","ação","Drama"],
    'ano':["1980","2025","1997"]
}
tabela_filmes = pd.DataFrame(filmes)

print(filmes)
print(type(filmes))
print(tabela_filmes)
print(type(tabela_filmes))

print(serie_impares)

quadrado_serie_impares = serie_impares*quadrado_serie_impares
print(quadrado_serie_impares)


#leitura de arquivos

# leitura_invest = pd.read_excel