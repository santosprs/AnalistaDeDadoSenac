nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
optativa = float(input("Digite a nota da optativa (-1 se não fez): "))

if optativa != -1:
    if nota1 < nota2:
        nota1 = optativa
    else:
        nota2 = optativa

media = (nota1 + nota2) / 2

print("Média:", media)

if media >= 6:
    print("Aprovado")
elif media < 3:
    print("Reprovado")
else:
    print("Recuperação")