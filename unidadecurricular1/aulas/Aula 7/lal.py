def calculadora_v1(num1,num2,operador):

num1=float(input("digite seu primeiro numero"))
num2=float(input("digite seu segundo numero"))

operador=input("informe a operação desejada entre 1. Adição; 2. Subtração; 3. multiplicação; 4. divisão")

match operador:
    case "1":
        print(f"resultado da soma: {num1+num2}.")

    case "2":
        print(f"resutado da subtração{num1-num2}")

    case "3":
        print(f"Resultado da multiplicação:{num1*num2}")

    case "4":
        print(f"resultado da divisã{num1/num2}")

    case _:
        print("informe um numero de operador valido")

