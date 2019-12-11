estados = []
votos = []

for i in range(100):
	estado = input()
	if (estado in estados):
		votos[estados.index(estado)] += 1
	else:
		estados.append(estado)
		votos.append(1)

for i in range(len(estados)):
	print(f"{estados[i]} {votos[i]}")