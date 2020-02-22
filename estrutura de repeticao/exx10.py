pares=0
impares=0

for i in range(10):
	n=int(input("numero:"))
	if n % 2==0:
		pares=pares+1
	else:
		impares=impares+1
print("quantidade de numeros pares {}, impares{}".format(pares,impares))