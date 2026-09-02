comprimento = float(input("Digite o comprimento da cozinha: "))
largura = float(input("Digite a largura da cozinha: "))
altura = float(input("Digite a altura da cozinha: "))

area_paredes = (2 * comprimento * altura) + (2 * largura * altura)

caixas = area_paredes / 1.5

print("Área total das paredes:", area_paredes, "m²")
print("Quantidade de caixas de azulejos:", caixas)