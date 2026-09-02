inicio = float(input("Km no início do dia: "))
fim = float(input("Km no final do dia: "))
litros = float(input("Litros de combustível gastos: "))
valor_recebido = float(input("Valor recebido dos passageiros: R$ "))

distancia = fim - inicio

consumo = distancia / litros

gasto_combustivel = litros * 6.15

lucro = valor_recebido - gasto_combustivel

print("Consumo médio:", consumo, "km/L")
print("Lucro líquido: R$", lucro)