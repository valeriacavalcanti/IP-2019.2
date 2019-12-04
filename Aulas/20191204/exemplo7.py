# problema "igor"

frase = input("Frase: ")

nova_frase = ''

frase_final = ''

for letra in frase:
	if (ord(letra) >= 65) and (ord(letra) <= 90):
		nova_frase += chr(ord(letra) + 32)
	else:
		nova_frase += letra

if (ord(nova_frase[0]) >= 97) and (ord(nova_frase[0]) <= 122):
	frase_final += chr(ord(nova_frase[0]) - 32)
	frase_final += nova_frase[1:]
else:
	frase_final = nova_frase

#print(frase)
#print(nova_frase)
print(frase_final)