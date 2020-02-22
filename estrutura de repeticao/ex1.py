# -*- coding: utf-8 -*-
#Programa para aprovar emprestimo

valor_casa = int(input("Digite o valor da casa:"))
salario = int(input("Digite o valor do salario:"))
anos= int(input("Digite em quantos anos vai pagar:"))
meses = anos * 12
mensalidade=valor_casa / meses
alicota_maxima_do_salario=(salario/100)*30

if(mensalidade>alicota_maxima_do_salario):
	print("Valor da mensalidade é:", mensalidade)
	print("Alícota máxima aceitável do salário:", alicota_maxima_do_salario)
	print("Seu empréstimo foi negado por causa da mensalidade exceder 30% do seu salário .")
else:
	print("Valor da mensalidade é:", mensalidade)
	print("Alícota máxima aceitável do salário:", alicota_maxima_do_salario)
	print("Parabéns, seu empréstimo foi aceito.")
