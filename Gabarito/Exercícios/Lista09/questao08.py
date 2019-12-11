frase = input()
deslocamento = int(input())
nova_frase = ''

for letra in frase:
	if (letra != ' '):
		nova_letra = ord(letra) + deslocamento
		if (nova_letra > ord('Z')):
			nova_letra = 64 + nova_letra - ord('Z')
		nova_frase += chr(nova_letra)
	else:
		nova_frase += letra

print(nova_frase)