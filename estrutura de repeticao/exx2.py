maior_nota=0
numero_alunos=int(input("Digite o numero de alunos: "))
nome_maior_nota=input("nome da maior nota:")
for i in range(numero_alunos):
	nome=input("Digite nome:")
	nota=int(input("Digite nota:"))
	if nota > maior_nota:
		nome_maior_nota=nome
		maior_nota=nota
print(nome_maiot_nota)
