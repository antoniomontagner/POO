valor=int(input("Digite o valor da compra:"))
print("O valor da compra é: ", valor)
if(valor>=5000):
	print("O valor da compra com desconto de 20% é:",0.8*valor)
elif(valor<5000):
	print("O valor da compra com 15% de desconto é: ",0.85*valor)
