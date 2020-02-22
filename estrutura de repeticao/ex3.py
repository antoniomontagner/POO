# -*- coding: utf-8 -*-
#Programa para calcular IMC

peso=float(input("Digite seu peso:"))
altura=float(input("Digite sua altura em centímetros:"))
IMC=(peso/altura)*altura
if(IMC<=18.5):
	print("Você está abaico do peso.")
elif(IMC>18.5 and IMC<=25):
	print("Você está com o peso ideal.")
elif(IMC>25 and IMC<=30):
	print("Você está com sobrepeso.")
elif(IMC>30 and IMC<=40):
	print("Você está com obesidade.")
elif(IMC>40):
	print("Você está com obesidade mórbida.")