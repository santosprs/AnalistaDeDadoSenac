for i in range(12):
    print(f"\nCandidato {i + 1}")

    ano_nascimento = int(input("Digite o ano de nascimento: "))

    idade = 2026 - ano_nascimento

    if idade < 18:
        print("Não pode participar.")
    else:
        nome = input("Digite o nome: ")
        telefone = input("Digite o telefone: ")
        email = input("Digite o email: ")

        print("Cadastro realizado com sucesso!")