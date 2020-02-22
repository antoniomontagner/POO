n=int(input("NxN "))
while 0>=n>=100:
    n=int(input("NxN "))
"""
m=[]
for i in range(1,(n+1)):
    if i ==1:
        for j in range(1,(n+1)):
            m.append(j)
            print(f"{j}")

    elif i>1:
        for j in range(i,1,-1):
            print(f"{j}")

            m.append(j)
        for j in range(2,n-i):
            m.append(j)
            print(f"{j}")
for i in m:
    print(m)"""
def matriz(n):
    m=[]

    for i in range(n):
        x=[]
        for j in range(n):
            x.append(0)
        m.append(x)
    return(m)

x=matriz(n)
for i in x:
    print(i)


conti=contj=1
for i in range(n):
    
    for j in range(n):
        
        if contj>1:
            
            x[i][j]=contj
            contj-=1
        else:
            x[i][j]=contj
            contj+=1

print(x)



