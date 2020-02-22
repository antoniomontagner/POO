competidores=int(input("Digite o número de competidores: "))
numero_folhas=int(input("Digite o número de folhas compradas: "))
folha_por_pessoa=int(input("Digite o número de folhas para cada competidor: "))
if(competidores>=1 and competidores<=1000 and numero_folhas>=1 and numero_folhas<=1000 and folha_por_pessoa>=1 and folha_por_pessoa<=1000):
	s=folha_por_pessoa*competidores
	if(s>numero_folhas):
		print("N")
	else:
		print("S")
else:
	print("Número inválido.")