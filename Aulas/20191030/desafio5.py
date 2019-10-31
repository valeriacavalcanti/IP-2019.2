numeros = list(range(10, 101, 10))

posicao = -1
num = int(input())

for i in range(len(numeros)):
	if (numeros[i] == num):
		posicao = i

print(numeros)

if (posicao != -1):
	print(f'tem e está na posicao {posicao}')
else:
	print('não tem')