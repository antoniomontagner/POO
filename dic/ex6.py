from random import randint
n=int(input("N: "))
m=int(input("M: "))
lista=[]
for i in range(n):
    x=[]
    for j in range(m):
        x.append(randint(0,9))
    lista.append(x)

for i in lista:
    print(i)
lis=[]
for i in lista:
    l=[]
    soma=0
    for j in i:
        soma+=j
    l.append(soma)
    print(l)
    lis.append(l)
print(lis)

maior=''
for i in lis:
    if i==lis[0]:
        maior=i
    elif i>maior:
        maior=i

print(maior)