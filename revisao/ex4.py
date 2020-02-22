
a=[]
while True:
    a.append(int(input("numero: ")))
    stop=input("parar: S/N ").upper()
    if stop=="S":
        break
soma=0
for i in a:
    soma+=i
print(soma)

fat=[]
for i in a:
    from math import factorial
    fat.append(factorial(i))
print(fat)

dec=[]
a.sort()
a.reverse()
print(a)
#x=len(a)
#for i in range(x-1,-1,-1):
#    dec.append(a[i])
#print(dec)

