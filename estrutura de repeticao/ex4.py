# -*- coding: utf-8 -*-
#programa para ler nota e fazer média

nota1=int(input("Digite a sua primeira nota:"))
nota2=int(input("Digite a sua segunda nota:"))
nota3=int(input("Digite a sua terceira nota:"))
media=(nota1+nota2+nota3)/3
print("Sua nota média é {:.2f}.".format(media))
if(media<5):
	print("Parabens, você foi reprovado.")
elif(media>=5 and media<7):
	print("Parabens, voce vai para a recuperação.")
elif(media>=7):
	print("Parabens, você foi aprovado.")
