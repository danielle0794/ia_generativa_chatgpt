import csv

dados_tabela = [
    ["nome","Cargo","Idade"],
    ["Carlos","Estagiário","32"],
    ["Danielle","Auxiliar administrivo","23"],
    ["Mario","Almoxarife","28"]
]

with open("08.2-funcionario.csv","w",encoding="utf-8",newline="") as arquivo_csv:
    escrever = csv.writer(arquivo_csv)
    escrever.writerows(dados_tabela)

