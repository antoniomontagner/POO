preco=float(input("Digite o preço do produto."))
valor=float(input("Digite o valor pago."))
if(valor>preco):
	troco=valor-preco
	print("Seu troco é {:.2f}".format(troco))
elif(preco>valor):
	print("Seu dinheiro não é suficiente.")
else:
	print("Não tem troco.")
