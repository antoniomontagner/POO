"""
lista=[]
p=input("paravra: ").upper()
lista.append(p)
soma=0
print(lista)
for i in lista:
    for j in i:
        if j=="Q" or j=="Z":
            soma+=10
        elif j=="J" or j=="X":
            soma+=8
        elif j=="F" or j=="H":
            soma+=4
print(soma)"""
"""
st=[]
st.append(input("palavra: ").upper())
x=st.count('Q')

xx=st.count("JX")*8
xxx=st.count("K")*5
xxxx=st.count("FHVWY")*4
c=st.count("BCMP")
cc=st.count("DG")*2
t=x+xx+xxx+xxxx+c+cc

print(x)"""
lis=[]
for i in range(2):
    dic={}
    dic[i]=input("palavra: ").upper()
    lis.append(dic)
print(dic)
for i in lis:
    for j in i:
        x=0
        if j=="Q":
    
            x+=1
        print(x)