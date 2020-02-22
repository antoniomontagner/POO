n=int(input("numero de algaritmos: "))
while 1>n>10:
    n=int(input("numero de algaritmos de m: "))

m=int(input("numero m: "))
while 1>m>10000000000:
    m=int(input("numero m: "))
x=str(m)
soma=0
for i in range(n):
    soma+=int(x[i])
if soma%3==0:
    print("sim")
else:
    print("nao")
