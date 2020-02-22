from random import randint
lista=[]
n=int(input("quantos jogos: "))
for i in range(n):
    jogo=[]
    for i in range(6):
        jogo.append(randint(1,60))
    lista.append(jogo)

print(lista)