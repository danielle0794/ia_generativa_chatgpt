
def dividir_seguro(x,y):
    resultado = x/y
    return resultado

try:
    x = int(input("Digite um numero: "))
    y = float(input("Digite outro numero: "))

    valor_resultado = dividir_seguro(x,y)

    print(valor_resultado)
    
except ValueError:
    print("Apenas valores numericos são permitidos")
    print("Apenas valores inteiros")

except ZeroDivisionError:
    print("Divisões por zero não são possiveis")

else:
    print("O valor da dividão é: ",valor_resultado)