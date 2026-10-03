#Exemplo de encadeamento/aninhamento

tem_cartao = True
saldo = 100

if tem_cartao:
    if saldo >= 100:
        print("Compra aprovada, saldo suficiente")
    else:
        print("Compra negada, saldo insuficiente")
else:
    print("Erro, cartão não inserido")
