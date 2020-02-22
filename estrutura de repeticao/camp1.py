Av=int(input("Digite o número de vitórias do time A: "))
Ae=int(input("Digite o número de empates do time A: "))
As=int(input("Digite o saldo de gols do time A: "))
Bv=int(input("Digite o número de vitórias do time B: "))
Be=int(input("Digite o número de empates do time B: "))
Bs=int(input("Digite o saldo de gols do time B:"))

if(0<=Av and 0<=Ae and 0<=Bv and Be<=100 and -1000<=As and Be<=1000):

	pontosA=(Av*3)+(Ae*1)
	pontosB=(Bv*3)+(Be*1)
	print("Pontos do time B: ", pontosB, "Pontos do time A: " ,pontosA)
	if(pontosA>pontosB):
		print("Time A é melhor classificado")
	elif(pontosB>pontosA):
		print("Time B é melhor classificado")
	elif(pontosA==pontosB and As>Bs):
		print("Time A é melhor classificado")
	elif(pontosA==pontosB and Bs>As):
		print("Time B é melhor classificado")
	elif(pontosA==pontosB and Bs==As)
		print("Empates")
else:
	print("Número não aceito.")
