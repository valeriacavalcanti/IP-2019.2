numeros = []
positivos = []
pares = []

for i in range(10):
	numeros.append(int(input()))
	if (numeros[i] > 0):
		positivos.append(numeros[i])
	if (numeros[i] % 2 == 0):
		pares.append(numeros[i])

print(numeros)
print(positivos)
print(pares)