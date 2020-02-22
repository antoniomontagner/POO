# Antonio S. Montagner / 19203742 / 1208A / CCO-UFSC

n=int(input("numero de participantes: "))
m=int(input("numero de problemas: "))

matriz=[]

for i in range(n):
    x=[]                    #matriz     
    for j in range(m):
        
        ij=int(input("{}X{} [1/0] ".format(i,j)))
    
        x.append(ij)
    matriz.append(x)

for l in range (n):
    for c in range (m):

        print(f"[{matriz[l][c]}]",end='')
    print()

sl=[]
sc=[]

for i in range(n):
    soma=0
    for j in range(m):
        soma+=matriz[i][j]
    sl.append(soma)

for i in range(n):
    soma1 = 0
    for p in matriz:
        soma1 += p[i]
    sc.append(soma1)
print(sl,sc)

t=0

for i in sc:
    if i<m:
        t+=1
    elif i>=1:
        t+=1
    elif i<m:
        t+=1
t+=1
for i in sc:
    
    if i==0:
        t-=1
print(t)
