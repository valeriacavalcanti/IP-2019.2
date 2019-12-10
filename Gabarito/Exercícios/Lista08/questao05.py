frase = input()
palavra = input()
nova_frase = ''

for p in frase.split(palavra):
	nova_frase += p
	nova_frase += '*'

nova_frase = nova_frase[:len(nova_frase)-1]
print(nova_frase)