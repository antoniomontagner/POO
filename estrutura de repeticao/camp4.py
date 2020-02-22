n=int(input("Digite um número: "))
p=int(input("Digite o primeiro número da operação: "))
q=int(input("Digite o segundo número da operação: "))
op=input("Digite a operação + ou *: ")

if(n>=1 and n<=500000 and p>=0 and p<=1000 and q>=0 and q<=1000):
	if(op=="+"):
		conta=p+q
		if(conta>n):
			print("OVERFLOW")
		else:
			print("O resultado da conta é:",conta)
	else:
		conta=p*q
		if(conta>n):
			print("OVERFLOW")
		else:
			print("O resultado da conta é:",conta)

else:
	print("Número inválido.")