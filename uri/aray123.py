n=int(input("NxN"))
while 3>= n >=70:
    n=int(input("NxN"))
m=[]
for i in range(n):
    x=[]
    for j in range(n):
        if i == j:
            x.append(1)
        else:
            x.append(3)
    m.append(x)
cont=0
for j in range(n-1,-1,-1):
    m[cont][j]=2
    cont+=1
for i in m:
    print(i)


def fibonacci(n):                        
    if n<=1:                             
        return n                         
    else:                                
        return fibonacci(n-1)+fibonacci(n-2) 

def fatorial (n):
    if n <= 0:
        return n
    else:
        return n*fatorial(n-1)