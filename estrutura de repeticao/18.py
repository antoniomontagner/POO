
while True:
	n=int(input("numero: "))
	i=1
	fat1=1
	while i < n:
	
		fat1=fat1+(fat1*i)
		i+=1

	print(fat1)
	continuar=input("continua: ")
	if continuar=='n':
		break