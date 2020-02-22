n=int(input("casos: "))
for i in range(n):
    s1=input("str 1: ")
    s2=input("str 2: ")
    if len(s1)<len(s2):
        p=[]
        for i in range(len(s1)):
            p.append(s1[i])
            p.append(s2[i])
            x=len(s2)-len(s1)
        """for j in range (x):
            z=len(s2)-(j-1)
            p.append(s2[z])"""
        print(p)
    else:
        p=[]
        for i in range(len(s2)):
            p.append(s1[i])
            p.append(s2[i])
            x=len(s1)-len(s2)
        """for j in range (x):
            z=len(s1)-(j-1)
            p.append(s1[z])"""
        print(p)