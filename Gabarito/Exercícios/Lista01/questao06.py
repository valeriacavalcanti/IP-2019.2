fat = 1

num = int(input("Número: "))

for i in range(2, num + 1):
	fat *= i

print(f"{num}! = {fat}")