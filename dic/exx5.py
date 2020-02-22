from random import randint
lis=[]

while len(lis)<10:
    n=randint(0,9)
    if n not in lis:
        lis.append(n)
print(lis)
lis.sort()
print(lis)