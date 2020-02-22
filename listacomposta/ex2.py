lista=[]
par=[]
imp=[]

for i in range(7):
    n=int(input("numero: "))
    if n%2==0:
        par.append(n)
    else:
        imp.append(n)

lista.append(par)
lista.append(imp)

print(lista)
