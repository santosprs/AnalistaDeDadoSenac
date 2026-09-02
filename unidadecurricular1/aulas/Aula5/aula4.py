# mes = int(input("Informe o mês de seu nascimento:"))


# if mes==1:
#     signo="Aquário"
# elif mes==2:
#     signo="Peixes"
# elif mes==3:
#     signo="Aries"
# elif mes==4:
#     signo="Touro"
# elif mes==5:
#     signo="Gemeos"
# elif mes==6:
#     signo="Cancer"
# elif mes==7:
#     signo="Leão"
# elif mes==8:
#     signo ="Virgem"
# elif mes==9:
#     signo="Libra"
# elif mes==10:
#     signo="Escorpião"
# elif mes==11:
#     signo="Sagitario"
# else:
#     signo="Capricornio"

# print(f"seu signo é {signo}.")



# match mes:
#     case 1:
#         signo="Aquario"
#     case 2:
#         signo="aries"
#     case 3:
#         signo="touro"
#     case 4:
#         signo="gemeos"
#     case 5:
#         signo="cancer"
#     case _:
#         signo="Numero do mes invalido"

# print(f"{signo}.")


#Exercicio 1 Calculo da Lampada












#exercicio 4 codigo de origem de produto



Codigo = int(input("Informe o Codigo do Produto:"))

match Codigo:
    case 1:
        Codigo="Sul"
    case 2:
        Codigo="Norte"
    case 3:
        Codigo="Leste"
    case 4:
        Codigo="Oeste"
    case 5 |6:
        Codigo="Nordeste"
    case 7 | 8 | 9:
        Codigo="Sudeste"
    case 10:
        Codigo="Centro Oeste"
    case 11:
        Codigo="Noroeste"
    case _:
        Codigo="Importado"

print(f"Região do Produto:{Codigo}.")
 