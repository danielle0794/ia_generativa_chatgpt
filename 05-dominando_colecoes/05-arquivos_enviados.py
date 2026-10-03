#Lista de arquivos encontrados no diretorio
arquivos_enviados = ["menu.pdf","foto.png","cardapio.pdf","manual.pdf","contatos.pdf","contrato.PDF","virus.exe","relatorio.pdf","anotacoes.txt"]

#lista de arquivos pdf (vazia)
pdfs_validos = []


for arquivo in arquivos_enviados:
    if arquivo.lower().endswith(".pdf"): #endswith serve para verificar o final do arquivo (Alt + Z coloca o curso para escrever na linha de baixo e manter no mesmo codigo)
        pdfs_validos.append(arquivo)

print("Lista completa",arquivos_enviados)
print("Arquivos de PDF",pdfs_validos)
