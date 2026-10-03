#função completa que verifica se o numero é par
def e_par(numero):
    if numero % 2 == 0:
        return True
    else:
        False

#Usando o retorno da função em uma estrutura if e Else
if e_par(2001):
    print("O numero é par.")
else:
    print("O numero é impar.")
