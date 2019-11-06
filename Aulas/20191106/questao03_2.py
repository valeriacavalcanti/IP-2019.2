numeros = [0] * 6
qtde = 0

while (qtde < 6):
	num = int(input())
	existe = False
	for i in range(qtde):
		if (num == numeros[i]):
			existe = True
			break
	if (existe == False):
		numeros[qtde] = num
		qtde += 1

print(numeros)