"""n=int(input(" NxN "))
while (n%2)!=0:
    n=int(input(" NxN "))

matriz=[]
for i in range(n):
    x=[]
    for j in range(n):
       x.append(0)
    matriz.append(x)
for i in matriz:
    print(i)
print()

z=[]
for i in range(2):
    x=[]
    a=int(input("coordenadas figurinha 1: X "))
    b=int(input("coordenadas figurinha 2: Y "))
    x.append(a)
    x.append(b)
    z.append(x)
print(z)

if z[0][0]<n/2 and z[1][0]>n/2:
    print("s")
elif z[0][0]>n/2 and z[1][0]<n/2:
    print("S")
elif z[0][1]<n/2 and z[1][1]>n/2:
    print("S")
elif z[0][1]>n/2 and z[1][1]<n/2:
    print("s")
else:
    print("N")"""
"""
if z[0][0] >=(n/2) and z[1][0]>=(n/2):
    if z[0][1] >=(n/2) and z[1][1]>=(n/2):
        print(z[0][1])
        print("N ")
    else:
        print("S")
elif z[0][0] <=(n/2) and z[1][0]<=(n/2):
    if z[0][1] >=(n/2) and z[1][1]>=(n/2):
        print("N")
    else:
        print("S")
elif z[0][1] >=(n/2) and z[1][1]>=(n/2):
    if z[0][0] >=(n/2) and z[1][0]>=(n/2):
        print("N")
    else:
        print("S")
elif z[0][1] <=(n/2) and z[1][1]<=(n/2):
    if z[0][0] >=(n/2) and z[1][0]>=(n/2):
        print("N")
    else:
        print("S")
"""

n=int(input("NxN "))
x1=int(input("x1"))
y1=int(input("y1"))
x2=int(input("x2"))
y2=int(input("y2"))
if (x1>(n/2) and x2<(n/2)) or (y1>(n/2) and y2<(n/2)) or (x1<(n/2) and x2>(n/2)) or (y1<(n/2) and y2>(n/2)):
    print("S")
else:
    print("N")