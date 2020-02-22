n1=int(input("Primeiro numero:"))
n2=int(input("Segundo numero:"))
soma=0
for i in range(n1+1,n2,n1):
	soma +=i
print(soma)