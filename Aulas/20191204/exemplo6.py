# converter string min -> mai

nome = input("Nome: ")
nome_mai = ''

for letra in nome:
	if (ord(letra) >= 97) and (ord(letra) <= 122):
		nome_mai += chr(ord(letra) - 32)
	else:
		nome_mai += letra

print(nome)
print(nome_mai)