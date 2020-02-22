s=6*1-2
print(s)
s=6*(1-2)
print(s)

v1=int(input("v1:"))
v2=int(input("v2:"))
v3=int(input("v3:"))
s=v1+v2+v3
print(s)

nome=input("nome:")
print("bem vindo {}.".format(nome))
#4
n=int(input("numero:"))
print("antesessor {} e sucessor {}.".format((n-1),(n+1)))
# 5
n=int(input("numero:"))
print("dobro {}, triplo {} e raiz quadrada {}.".format((2*n), (3*n), (n**0.5)))
# 6
nome=input("nome: ")
n1=float(input("nota 1:"))
n2=float(input("nota 2:"))
m=(n1+n2)/2
print("presado aluno {}, suas notas foram {} e {}, portanto, sua media é {}.".format(nome,n1,n2,m))
# 7
a=float(input("altura: "))
l=float(input("largura: "))
area=a*l
tinta= area/2
print("é necessario {} litros de tinta pois a area é de {} m^2.".format(tinta,area))
#8
preco=int(input("preco do pruduto: "))
print("o novo preco do produto ja com desconto de 5% é de ",(preco*0.95)," reais.")


# 1 if else elif
valor=int(input("Valor da casa: "))
salario=int(input("salario do comprador: "))
anos_para_pagar=int(input("em quantos anos vai pagar: "))
prestacao=valor/(anos_para_pagar*12)
if prestacao>(0.3*salario):
	print("seu imprestimo foi negado, pois, seu salario é {},a mensalidade é {:.2f} e a mensalidade nao pode passar de {}".format(salario,prestacao,(0.3*salario)))
else:
	print("seu imprestimo foi aceito e sua mensalidade é de {} por mes.".format(prestacao))

#2
val=int(input("preco produto: "))
print("""forma de pagamento 
	[1]A vista
	[2]1x cartao
	[3]2x cartao
	[4]ex cartao""")
pagamento=int(input("digite:"))
if pagamento==1:
	print("o valor a vista é: {} reais".format(val*0.90))
elif pagamento==2:
	print("o valor em 1x no cartao é: {} reais".format(0.95*val))
elif pagamento==3:
	print("o valor em 2x no cartao é: {} reais".format(val))

else:
	print("o valor em 3x no cartao é de : {} reais".format(1.2*val))

	#3
peso=float(input("peso:"))
altura=float(input("altura:"))
if 0.1 <= altura <= 10:
	imc=peso/(altura**2)
	if imc<18.5:
		print("abaixo do peso")
	elif 18.5 <= imc <25:
		print("peso ideal")
	elif 25<= imc<30:
		print("sobrepeso")
	elif 30<= imc<40:
		print("obesidade")
	else:
		print("gordo")
else:
	imc=peso/((altura/100)**2)
	if imc<18.5:
		print("abaixo do peso")
	elif 18.5 <= imc <25:
		print("peso ideal")
	elif 25<= imc<30:
		print("sobrepeso")
	elif 30<= imc<40:
		print("obesidade")
	else:
		print("gordo")
#4
n1=float(input("Numero 1: "))
n2=float(input("Numero 2: "))
n3=float(input("Numero 2: "))
m=(n1+n2+n3)/3
if m<5:
	print("reprovado")
elif 5<m<7:
	print("recuperacao")
else:
	print("aprovado")
print("media ",m)
#5
ano=int(input("ano do nascimento:"))
if ano>=2002:
	print("ainda vai se alistar ao serviço militar")
elif ano==2001:
	print("está no momento de se alistar")
else:
	print("passou do tempo do alistamento")
#6
v1=int(input("n1: "))
v2=int(input("n2: "))
if 0<=v1<=1000 and 0<=v2<=1000 and v1!=v2:
	if v1>v2:
		print("valor é {}.".format(3*v1))
	else:
		print("valor é {}.".format(3*v2))
else:
	print("numero invalido")
#10
valor=int(input("valor da compra: "))
if valor >= 5000:
	print("o valor da compra é de {} e o com desconto de 20% vai ficar {}.".format(valor,(0.8*valor)))
else:
	print("o valor da compra é de {} e o com desconto de 15% vai ficar {}.".format(valor,(0.85*valor)))

#1 import
