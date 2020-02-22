aluno_melhor=''
mediageral=0
mensalidade=int(input("Valor da mensalidade:"))
valormensalidade=0.7*mensalidade
for i in range (5):
	nome=input("Aluno:")
	nota=int(input("Nota:"))
	if nota>mediageral:
		mediageral=nota
		aluno_melhor=nome
print("mensalidade sem desconto", mensalidade)
print("o melhor aluno {}, a melhor nota {}, o valor da mensalidaede {}".format(aluno_melhor,mediageral,valormensalidade)) 