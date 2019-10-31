numeros = [0]*10

for i in range(10):
	numeros[i] = (i + 1) * 10

for i in range(10):
	for j in range(i + 1):
		print(numeros[j], end=' s')
	print()

