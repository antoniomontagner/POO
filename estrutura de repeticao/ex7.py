print("Digite sua data de nascimento.")
dia=int(input("Dia: "))
mes=int(input("Mês; "))
ano=int(input("Ano: "))
anos=2019-ano
idade=dia+(mes*30)+(anos*365)#6570,4380
if(idade<=4380):
	print("Você é uma criança.")
elif(idade>=4381 and idade<=6569):
	print("Você é um adolescente.")
elif(idade>=6570):
	print("Você é um adulto.")