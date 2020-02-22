"""n=input("nome: ")
caracter=len(n)
idade=int(input("idade: "))
salario=int(input("salario: "))
sexo=input("sexo: f/m ")
estado=input("estado civil: s/c/v/d ")
while caracter<3 or 0>idade>150 or salario<0 or sexo!= 'f'and'm' or estado!='s'and'c'and'v'and'd':
	n=input("nome: ")
	caracter=len(n)
	idade=int(input("idade: "))
	salario=int(input("salario: "))
	sexo=input("sexo: f/m ")
	estado=input("estado civil: s/c/v/d ")
print(f"nome {n}, idade {idade}, salario {salario}, sexo {sexo}, estado civil {estado}.")
"""
def login(n,c,i,s,sex,e):
	while c<3 or 0>i>150 or s<0 or sex!= 'f'and'm' or e!='s'and'c'and'v'and'd':
		n=input("nome: ")
		c=len(n)
		i=int(input("idade: "))
		s=int(input("salario: "))
		sex=input("sexo: f/m ")
		e=input("estado civil: s/c/v/d ")
		return n,c,i,s,sex,e
n=input("nome: ")
caracter=len(n)
idade=int(input("idade: "))
salario=int(input("salario: "))
sexo=input("sexo: f/m ")
estado=input("estado civil: s/c/v/d ")

cadastro=login(n,caracter,idade,salario,sexo,estado)

print(f"nome {n}, idade {idade}, salario {salario}, sexo {sexo}, estado civil {estado}.")
