v1=0
v2=0
op=0
while (op<=3 and op==5):
	n1=(int(input("Digirte um numero:")))
	n2=int(input("Digite um numero:"))
	v1=n1
	v2=n2
	print("Digite a operação:")
	print(''' 
		[1] somar
		[2] multiplicar
		[3] monstrar o maior valor
		[4]digitar novos numeros
		[5]sair''')
	operacao=int(input(''))
	op=operacao
	if operacao=='1':
		v1=n1+n2
	elif operacao=='2':
		v1=n1*n2
	elif operacao=='3':
		if n1>n2:
			print("n1 é maior")
		else: 
			print("n2 é maior")
	
	else:
		break
print("Os valores digitados foram: {} e {} ".format(v1,v2))
