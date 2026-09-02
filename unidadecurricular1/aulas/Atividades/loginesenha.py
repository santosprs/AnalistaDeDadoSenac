usuario_correto = "admin"
senha_correta = "123456"

tentativas = 3

while tentativas > 0:
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Login realizado com sucesso!")
        break
    else:
        tentativas = tentativas - 1
        print("Dados incorretos.")

if tentativas == 0:
    print("Usuário bloqueado.")