tentativa = 5

while tentativa != 0:
    senha = input("Digite a senha")
    if senha == "123456":
        print("Bem vindo, acesso liberado")
        break
    else:   
        print("esqueci a asneha")
        tentativa -= 1
