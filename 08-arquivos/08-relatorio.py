# o modo w cria o arquivo "realtorio.txt" na pasta raiz do projeto
with open("08-relatorio.txt","a",encoding="utf-8") as arquivo:
    arquivo.write("\nPrimeira linha: atenção a primeira linha foi escrita\n")
    arquivo.write("\nSegunda linha: Dados salvos pelo Python\n")