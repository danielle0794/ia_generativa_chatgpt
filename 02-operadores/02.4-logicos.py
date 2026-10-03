#1.Operador AND (E) - Retorna True apenas se tods as condições forem verdadeiras

tem_sol = True
tem_dinheiro = True
vai_praia = tem_sol and tem_dinheiro

print("Vai a praia (AND):",vai_praia)

# 2. operador OR (ou) - retorna True se pelomenos uma ocndição for verdadeira
tem_carro = False
tem_bicicleta = True

pode_viajar = tem_carro or tem_bicicleta

print("Vai vijar? ",pode_viajar)

#3. Operador  NOT (NÃO) - INVERTE O VALOR LOGICO

chovendo = False
fazer_caminhada = not chovendo
print("Fazer caminhada (NOT): ", fazer_caminhada)