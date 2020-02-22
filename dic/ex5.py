n=int(input("n de vezes: "))

negada=[]
for i in range(n):
    gordo={}
    gordo['nego']=input("nome")
    gordo['pow']=int(input("poder: "))
    gordo['morte']=int(input("mortes: "))
    gordo['id']=int(input("idade: "))
    negada.append(gordo)

print('=-'*30)
print(negada)
print('=-'*30)
for i in negada:
    print(i)
print('=-'*30)

escolhido=[]
for j in negada:
    if j==negada[0]:
        escolhido=j        
    elif escolhido['pow']<j['pow']:
        escolhido=j
    elif escolhido['pow']==j['pow']:
        if escolhido['morte']<j['morte']:
            escolhido=j
print(escolhido)

#escolhido=''
#for i in gordo :
 #   print(i[0])
   # for j in gordo:
    #    if i[1]>j[1]:
     #       print(i[1])
     #       print(f"Ó esólhidó é {i}")
"""
for i,j in gordo:
    print(j[1])"""          #deveria funcionar