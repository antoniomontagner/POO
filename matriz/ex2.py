from random import randint

m=[]
for i in range(12):
    x=[]
    for j in range(12):
        b=randint(0,1)
        x.append(b)
    m.append(x)

for l in range (12):
    for c in range (12):

        print(f"[{m[l][c]}]",end='')
    print()

x=input("operacao: ")
soma=0
cont=0
if x=='+':
    for i in range(12):
        for j in range(12):
            if j>i and j<(12-(i+1)):
                soma+=m[i][j]
    print(f"{soma:.2f}")
elif x=='/':
    for i in range(len(m)):
        for j in range(len(m[i])):
            if j>i and j<(12-(i+1)):
                soma+=m[i][j]
                cont+=1
    print(f"{soma/cont:.2f}")