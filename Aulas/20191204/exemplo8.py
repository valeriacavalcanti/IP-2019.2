# remover a letra a

frase = input('Frase: ')
nova_frase = ''

for letra in frase:
	if (letra != 'a') and (letra != 'A'):
		nova_frase += letra

print(nova_frase)