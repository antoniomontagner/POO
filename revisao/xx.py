"""c=int(input("casos: "))

for i in range(c):
    n=int(input("numero de bolas: "))
    x=int(input("bola branca: X"))
    y=int(input("bola branca: Y"))
    proxima=0
    xp=0
    yp=0
    for i in range(1,n+1):
        x1=int(input("bola: X1"))
        y1=int(input("bola: Y1"))
        if i==1:
            xp=x1
            yp=y1
            proxima=i
        elif (((x1**2)+(y1**2))**(1/2))<(((xp**2)+(yp**2))**(1/2)):
            xp=x1
            yp=y1
            proxima=i
    print(proxima)"""
n=int(input("n de seres: "))
lis=[]
for i in range(n):
    dic={}
    dic["nome"]=input("nome: ")
    dic["pow"]=int(input("pow: "))
    dic["mortes"]=int(input("mortes: "))
    lis.append(dic)
print(lis)
fort=[]
for i in range(n):
    if i ==0:
        fort.append(lis[0])
    elif lis[i]["pow"]>fort[0]["pow"]:
        fort.clear()
        fort.append(lis[i])

for i in lis:
    print(i)
print(fort)