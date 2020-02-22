from random import randint
"""
op=input("operacao: ")

m=[]
for i in range(12):
    x=[]
    for j in range(12):
        b=randint(0,1)
        x.append(b)
    m.append(x)

if op=='+':
    soma=0
    for i in range(12):
        for j in range(12):
            if j<i:
                soma+=m[i][j]
    print(soma)
elif op=='/':
    soma=0
    cont=0
    for i in range(12):
        for j in range(12):
            if j<i:
                soma+=m[i][j]
                cont+=1
    media=soma/cont
    print(media)

for l in range (12):
    for c in range (12):

        print(f"[{m[l][c]}]",end='')
    print()"""

m=[]
for i in range(12):
    k=[]
    for j in range(12):
        x=randint(0,9)
        k.append(x)
    m.append(k)
print(m)
print()
print()

for i in range(12):
    for j in range(12):
        print(f"[{m[i][j]}]",end='')
    print()


op=input("operacao: |S/M| ").upper()

s=0
cont=0
if op =="S":
    for i in range(12):
        for j in range(12):
            s+=m[i][j]
            cont+=1
    print(f"soma é: {s}")

elif op=="M":
    for i in range(12):
        for j in range(12):
            s+=m[i][j]
            cont+=1
    d=(s/cont)
    print(f"a media é: {d:.2f}")