codigo = int(input("Digite o código: "))

match codigo:
    case 1:
        print("Sul")
    case 2:
        print("Norte")
    case 3:
        print("Leste")
    case 4:
        print("Oeste")
    case 5 | 6:
        print("Nordeste")
    case 7 | 8 | 9:
        print("Sudeste")
    case _:
        if 10 <= codigo <= 20:
            print("Centro-Oeste")
        elif 21 <= codigo <= 30:
            print("Nordeste")
        else:
            print("Importado")