# verificar se existe letra a

frase = input('Frase: ')

existe = False

for letra in frase:
	if (letra == 'a') or (letra == 'A'):
		existe = True
		break

print(existe)