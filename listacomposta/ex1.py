lista=[]
cont=0

while True:
    dados=[]

    nome=input("nome: ")
    idade=int(input("idade: "))
    peso=int(input("peso: "))

    dados.append(nome)
    dados.append(idade)
    dados.append(peso)

    lista.append(dados)

    cont+=1

    continuar=input("continuar: S/N").upper()
    if continuar=='S':
        break

pesado=[]
leve=[]

for i in lista:
    if i[2]: 
        pesado.append(i[2])

pesado.sort

leve.append(pesado)

pesado.reverse()

print(f"foran cadastradas {cont} pessoas, a ordem de peso é {pesado} e das leves é {leve}.")