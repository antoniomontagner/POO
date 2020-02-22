from random import randint
matriz=[[[]],[],[]]
for i in range(3):
    x=[]    
    for j in range(3):
        y=[]
        
        for k in range(3):
            z=[]      
            
            for l in range(3):
                
                a=(randint(0,10))
                z.append(a)

            y.append(z)
            
        x.append(y)

    matriz.append(x)



for i in range(3):
    for j in range(3):
        for k in range(3):
            for l in range(3):
                print(f"[{matriz[i][j][k][l]}]",end='')
            print()
        print()

"""
for i in range(3):
    x=[]
    for j in range(3):
        y=[]
        
        for k in range(3):
            #z=[]
            #for l in range(3):
            #    print(matriz[i][j][k][l])
            #f"[{m[l][c]}]",end=''
            print(f" {matriz[i][j][k]} ",end='')
        print("")
    print("-="*20)
    #print()    """

"""for l in range (9):
    for c in range (9):

        print(f"[{matriz[l][c]}]",end='')
    print()
"""