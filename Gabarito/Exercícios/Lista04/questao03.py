qtde = 0
aprovados = 0
final = 0

nome, matricula, nota = input().split()
nota = int(nota)
menor = nota

while (nota >= 0) and (nota <= 100):
	qtde += 1
	if (nota < menor):
		menor = nota
	if (nota >= 70):
		aprovados += 1
	if (nota >= 40) and (nota < 70):
		final += 1
	nome, matricula, nota = input().split()
	nota = int(nota)

print(qtde)
print(menor)
print(aprovados)
print(final)