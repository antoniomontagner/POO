"""n=input("nome: ")
s=input("senha: ")
while n==s:
	print("senha invalida.")
	n=input("nome: ")
	s=input("senha: ")
print(f"nome {n} senha {s}.")
"""



def login(x,y):
	if x==y:
		return 'senha invalida'
	else:
		return x,y
n=input("nome: ")
s=input("senha: ")
login1=login(n,s)
print(f"nome {n} senha {s}.")