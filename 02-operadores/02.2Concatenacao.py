#1.concatenação simple de variaveis de texto

nome = "Maria"
sobrenome = "da silva"
nome_completo = nome + " "+ sobrenome

print("nome completo: ",nome_completo)

#2.concatenação combinando texto com numero
idade = 32
mensagem = "Olá, meu nome é " + nome_completo + " e eu tenho " + str(idade) + " anos"
print(mensagem)

nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a primeira nota: "))
nota_3 = float(input("Digite a primeira nota: "))

media = (nota_1 + nota_2 + nota_3)/3

print(f"A media das notas é: {media:.2f}")
print(f"A media das notas é: {round(media,2)}")
print("A media das notas é: ",media)