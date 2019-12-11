feitos = 0
sofridos = 0
vitorias = 0
empates = 0
derrotas = 0
pontos = 0

for i in range(38):
	resultado = input().split(" - ")
	f, s = resultado[0].split()
	f, s = int(f), int(s)
	feitos += f
	sofridos += s
	if (f > s):
		vitorias += 1
	elif (f == s):
		empates += 1
	else:
		derrotas += 1

print(feitos)
print(sofridos)
print(vitorias)
print(empates)
print(derrotas)
print(vitorias * 3 + empates)