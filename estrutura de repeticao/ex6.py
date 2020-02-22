# -*- coding: utf-8 -*-

valor1=int(input("Variável 1: "))
valor2=int(input("Variável 2: "))
if(valor1>=0 and valor1<=1000 and valor2>=0 and valor2<=1000):
	x=valor1*3
	y=valor2*3
	if (valor1>valor2):
		print("{}".format(x))
	else:
		print('{}'.format(y))