frase = input('Frase: ')
palavra = input('Palavra: ')

for i in range(len(frase)):
	if (frase[i:i+len(palavra)] == palavra):
		print(frase[i:i+len(palavra)])