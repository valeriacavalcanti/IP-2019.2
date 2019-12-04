# exibe a frequencia da letra a

frase = input('Frase: ')

qtde = 0

for letra in frase:
	if (letra == 'a') or (letra == 'A'):
		qtde += 1

print(qtde)