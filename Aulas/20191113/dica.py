lista = []

for i in range(10):
	lista.append(int(input()))

print(lista)
print(sum(lista))
print(max(lista))
print(min(lista))
print(lista.index(6))
print(lista.count(10))