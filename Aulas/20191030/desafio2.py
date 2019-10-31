numeros = [0]*10

for i in range(10):
	numeros[i] = 10 - i 

print(numeros)

posicao = int(input('Posição: '))
while (posicao < 0 or posicao > len(numeros) - 1):
	posicao = int(input('Posição: '))

valor = int(input('Valor: '))
numeros[posicao] = valor

print(numeros)