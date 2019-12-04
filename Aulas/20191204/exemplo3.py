# verificar se existe letra a e exibir a posição

frase = input('Frase: ')

existe = False

for i in range(len(frase)):
	if (frase[i] == 'a') or (frase[i] == 'A'):
		existe = True
		posicao = i
		break

if (existe):
	print(existe, posicao)
else:
	print(existe)