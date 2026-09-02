potencia_lampada = float(input("Digite a potência da lâmpada: "))
largura = float(input("Digite a largura do cômodo: "))
comprimento = float(input("Digite o comprimento do cômodo: "))

area = largura * comprimento

potencia_necessaria = area * 3

quantidade_lampadas = potencia_necessaria / potencia_lampada

print("Área do cômodo:", area, "m²")
print("Potência necessária:", potencia_necessaria, "W")
print("Quantidade de lâmpadas:", quantidade_lampadas)