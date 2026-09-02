def calcular_imc(peso, altura):
   imc = peso/(altura*altura)
   return imc

peso = float(input("Digite seu Peso:"))
altura = float(input("Digite sua Altura:"))

def obter_classificacao(imc):
    return imc

    if imc >18.5:
        print("Abaixo do Peso")
    elif imc >24.9:
        print("peso Normal")
    elif imc >29.9:
        print("Sobrepeso") 
    else:
        print("obesidade")








