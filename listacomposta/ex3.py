lista=[[],[],[]]
for i in lista:
    for j in range(3):
        i.append(int(input("numero: ")))
print(lista)

soma=0
for i in lista:
    for j in i:
        if j%2==0:
            soma+=j
print(soma)

s2=0
for i in lista:
    if i[2]:
        s2+=i[2]
print(s2)

maior=0
for i in lista[1]:
    if i>maior:
        maior=i
print(maior) 