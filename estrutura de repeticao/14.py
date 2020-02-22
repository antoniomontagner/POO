def impapar():
	par=0
	impar=0
	for i in range(10):
		n=int(input("numero: "))
		if n%2==0:
			par+=1
		else:
			impar+=1
	print(par,impar)
x=impapar()