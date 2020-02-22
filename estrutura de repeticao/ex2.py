# -*- coding: utf-8 -*-
# programa para calcular valor a ser pago por um produto

preco=float(input("Digite o preço do produto:"))
a_vista=0.90*preco
xcartao=0.95*preco
xxcartao=preco
xxxcartao=(0.2*preco)+preco
print("Para pagamento à vista:1")
print("Para pagamento em 1x no cartão:2")
print("Para pagamento em 2x no cartão:3")
print("Para pagamento em 3x ou mais no cartão:4")
opcao=int(input("Digite a opção de pagamento:"))

if(opcao==1):
	print("O preço a vista é:", a_vista)
elif(opcao==2):
	print("O preço em 1x no cartão é:", xcartao)
elif(opcao==3):
	print("O preço em 2x no cartão é:",xxcartao)
elif(opcao==4):
	print("O preço em 3x ou mais no cartão é:",xxxcartao)