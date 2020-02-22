#deveria funcionar

n=int(input("numero NxN :"))
m=[]
#xxx=0
#cont=0
#cont1=1
for i in range(n):
    x=[]
    for j in range(n):
        cont = 0
        while True:
            if i == cont or j == cont or i == n - (cont + 1) or j == n - (cont + 1):
                a = cont + 1
                x.append(a)
               # print("{:<3}".format(x), end=' ')    
                break
            cont += 1
            
       
    m.append(x)
    #cont+=1
    #cont1+=1
print(m)



print()

for l in range (n):
    for c in range (n):

        print(f"[{m[l][c]}]",end='')
    print()


""" if cont==0:
    if i == 0 or j ==0 or j==(n-1) or i==(n-1):
        x.append(1)
        cont+=1
        
elif cont>=1:
    if (i-cont)==0 or (j-cont)==0 or j==(n-(cont+1)) or i ==(n-(cont+1)):
        x.append(1+cont)
        cont+=1"""

"""while True:
            if cont==0:
                if i == 0 or j ==0 or j==(n-1) or i==(n-1):
                    x.append(1)
                    cont+=1
                    break
                else:
                    break
            elif cont>=1:
                if (i-cont)==0 or (j-cont)==0 or j==(n-(cont+1)) or i ==(n-(cont+1)):
                    x.append(1+cont)
                    cont+=1
                    break
                else:
                    break """


""" if j<(n/2):
            if i == 0 or j ==0 or j==(n-1) or i==(n-1):
                x.append(1)
                #cont+=1
                #cont1+=1
                print(cont,cont1)
        
            elif (i-cont)==0 or (j-cont)==0 or j==(n-(cont1)) or i ==(n-(cont1)):
                x.append(cont)
                #cont+=1
                #cont1+=1      
                print("TA NO ELIF")
        elif j>(n/2):
            if (i-cont)==0 or (j-cont)==0 or j==cont1 or i ==cont1:
                x.append(cont)
                #cont+=1
                #cont1+=1      
                print("TA NO ELIF")"""