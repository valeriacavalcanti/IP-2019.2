numeros = [0]*10
positivos = [0] * 10
pares = [0] * 10
qtPos = qtPar = 0

for i in range(10):
	numeros[i] = int(input())
	if (numeros[i] > 0):
		positivos[qtPos] = numeros[i]
		qtPos += 1
	if (numeros[i] % 2 == 0):
		pares[qtPar] = numeros[i]
		qtPar += 1

print(numeros)
print(positivos[0:qtPos])
print(pares[0:qtPar])
