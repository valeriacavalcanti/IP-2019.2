'''
LISTA 05 - QUESTÃO 06 (1.0v)
'''

numeros = []

for i in range(10):
  numeros.append(int(input()))

troca = True
while(troca == True):
  troca = False
  for i in range(9):
    if (numeros[i] > numeros[i+1]):
      numeros[i], numeros[i+1] = numeros[i+1], numeros[i]
      troca = True

print(numeros)