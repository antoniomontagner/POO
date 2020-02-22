"""n=int(input("numero de pessoas: "))
lista=[]
cont=0
soma=0
mulher=[]
idade_velho=[]
dic={}
totalIdade = 0

for i in range(n):
    cont+=1

    dic['nome']=input("nome: ")
    dic['idade']=int(input("idade: "))
    dic['sexo']=input("sexo: ").upper()

    lista.append(dic.copy())
    
    soma+=dic['idade']

#totalIdade
for i in range(0, n):
    totalIdade += lista[i]['idade']

media_idade = totalIdade / n

#mulheres
for j in range(0, n):
    if lista[j]['sexo'] == "F":
        print(lista[j]['nome'])

#printar mais velho do q a media
for k in range(0, n):
    if lista[k]['idade'] > media_idade:
        print(lista[k]['nome'])

print(lista,soma,media_idade,cont)
"""


lis=[]
while True:
    dic={}
    