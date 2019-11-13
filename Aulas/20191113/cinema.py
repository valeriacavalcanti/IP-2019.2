matriz = [False] * 4
for i in range(4):
	matriz[i] = [False] * 6

# Imprimir a matriz
for i in range(4):
	print(matriz[i])

# vendas ... 
linha, coluna = input('Linha e Coluna: ').split()
linha, coluna = int(linha), int(coluna)

while (matriz[linha][coluna] == False):
	matriz[linha][coluna] = True

	# Imprimir a matriz
	for i in range(4):
		print(matriz[i])
		
	linha, coluna = input('Linha e Coluna').split()
	linha, coluna = int(linha), int(coluna)

