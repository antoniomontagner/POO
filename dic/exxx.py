while True:
    n=int(input("n de flechas: "))
    while 1>=n>=10:
        n=int(input("n de flechas: "))

    matriz=[]
    for i in range(n):
        lis=[]
        x=int(input("corrdenada eixo X: "))
        while -100>=x>=100:
            x=int(input("corrdenada eixo X: "))
        
        y=int(input("coordenada eixo Y: "))
        while -100>=y>=100:
            y=int(input("coordenada eixo Y: "))
        lis.append(x)
        lis.append(y)
        matriz.append(lis)
    print(matriz)
    """
    hipo=[]

    for i in matriz:
        import math
        tmp= (i[0]**2)+(i[1]**2)
        tmp=math.sqrt(tmp)
        tmp=round(tmp,2)
        hipo.append(tmp)
        print(tmp)
    print(hipo)
    """
    def pitagoras(list):
        hipo=[]

        for i in list:
            import math
            tmp= (i[0]**2)+(i[1]**2)
            tmp=math.sqrt(tmp)
            tmp=round(tmp,2)
            hipo.append(tmp)
        return hipo
    x=pitagoras(matriz)
    cont=0
    for i in range(len(x)-1):
        
        if x[i]<x[i+1]:
            cont+=1
    print(x)
    print(cont)
    c=input("continuas: S/N").upper()
    if c=="N":
        break
