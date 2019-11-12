'''
LISTA 05 - QUESTÃO 05 (1.0v)
'''

num = int(input())
binario = []

while (num != 0):
  binario.append(num % 2)
  num //=2

tam = len(binario)

for i in range(tam//2):
  binario[i], binario[tam-1-i] = binario[tam-1-i], binario[i]

print(binario)
