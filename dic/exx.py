""" # MEGA SENA

from random import randint
n=int(input("numero de jogos: "))
lista=[]
for i in range(n):
    for j in range(6):

        x=randint(1,60)
        if x not in lista:
            lista.append(x)
    lista.sort()
    print(f"jogo {i} {lista}")
    lista.clear()
    """
"""
  #4 cara e um dado

from random import randint
from operator import itemgetter

dic={}
lista=[]
for i in range(4):
    x=randint(1,6)
    dic[f"{i}"]=x
print(dic)
for k,v in dic.items():
    print(f"jogador {k} tirou {v}")
ordenar=sorted(dic.items(), key=itemgetter(1), reverse=True)

#ordem=list(dic.items())
#ordem.sort()
#ordem.reverse()
print(ordenar)
"""
"""
    #     jogador e pontos

n=int(input("n de nego: "))
lis=[]
for i in range(n):
    dick={}
    dick['nome']=input("nome: ")
    dick['pontos']=int(input("pontos: "))
    dick['idade']=int(input("idade: "))
    lis.append(dick)
print(lis)
som_pontos=0
for i in lis:
    som_pontos+=i['pontos']
print(som_pontos)
"""
""" 
   #     cadastro

lis=[]
while True:
    dic={}
    dic['nome']=input("nome: ")
    dic['idade']=int(input("idade: "))
    dic['sexo']=input("sexo: F/M").upper()
    lis.append(dic)
    c=input("continuar: S/N").upper()
    if c=="N":
        break
som=0
cont=0
mulher=[]
for i in lis:
    som+=i['idade']
    cont+=1
    if i['sexo']=='F':
        mulher.append(i)
media=som/cont
med=[]
for i in lis:
    if i['idade']>media:
        med.append(i)

print(f"lista{lis} mulheres {mulher} media: {media} acima da media{med}")
x=int(input("numero do nego: "))
print(f"nego: {lis[x]}")
"""
"""
  #      diferenca na sequencia de numeros

while True:
    n=int(input("n de numeros: "))
    while 1>= n>=10**4:
        n=int(input("n de numeros: "))    
    a=[]
    for i in range(n):
        x=int(input("numero: "))
        while -10**5>=x>=10**5:
            x=int(input("numero: "))
        a.append(x)
    cont=1
    maior_sequencia=0
    print(a)
    for i in range(len(a)-1):
        #if i<len(a)-1:
           # if -1==(a[i]-a[i+1]) or (a[i]-a[i+1])==1 or (a[i]-a[i+1])==0:
            
        if -1<=(a[i]-a[i+1])<=1:
            cont+=1
            print(f"a[{i}]+a[{i+1}], numero de repeticoes= {cont}")
         #   if i==((len(a))-2):
          #      break
        else:
            if maior_sequencia<cont:
    
                print(maior_sequencia,cont)
    
                maior_sequencia=cont
    
                print(f"cont{maior_sequencia}")
            cont=1
    
    print(maior_sequencia)
    
    
    c=input("continuar: S/N").upper()
    if c=="N":
        break
"""
"""
 #           jogo de flechas com matriz/dici

while True:
    n=int(input("n de flechas: "))
    while 1>=n>=10:
        n=int(input("n de flechas: "))

    matriz={}
    for i in range(n):
        
        x=int(input("corrdenada eixo X: "))
        while -100>=x>=100:
            x=int(input("corrdenada eixo X: "))
        
        y=int(input("coordenada eixo Y: "))
        while -100>=y>=100:
            y=int(input("coordenada eixo Y: "))

        matriz[f'{x}']=y
    print(matriz)


    c=input("continuas: S/N").upper()
    if c=="N":
        break
"""
    
"""
#            p2 2018 Q1

lis=[]
while True:
    dic={}
    dic['nome']=input("nome: ")
    dic['idade']=int(input("idade: "))
    dic['id']=input("identidade: ")
    lis.append(dic)

    c=input("continuar: S/N ").upper()
    if c == "N":
        break

for i in lis:
    print(f"cliente: {i}")
alterar=input("alterar dados: S/N ").upper()
if alterar=="S":
    nome=input("nome do cliente: ")
    lis[f"{nome}"]=input("novo nome: ")
    lis
"""
"""
        #    p2 2019/1 Q1  "jogo imobiliario"
comp={} #competidores

n=int(input("valor inicial: "))
while 1>n>10000:
    n=int(input("valor inicial: "))
print(n)

comp['D']=n
comp['E']=n
comp['F']=n

print('-='*30)

nop=int(input("numero de operacoes: "))
while 1>nop>10:
    nop=int(input("numero de operacoes: "))

print('-='*30)
print('LEGENDA:\n'
      'Digite C para COMPRA \n'
      'Digite V para VENDA \n'
      'Digite A para ALUGUEL')
print('-='*30)
print('LEGENDA:\n'
      'Digite D para DANIEL \n'
      'Digite E para EDUARDO \n'
      'Digite F para FERNANDO')
print('-='*30)

for i in range(nop):
    op=input("qual operacao: ").upper()
    quem=input("quem realizou a operacao: ").upper()

    if op=='C':
        v_c=int(input("valor da compra: "))
        comp[f"{quem}"]+=v_c

    elif op=='V':
        v_v=int(input("valor da venda: "))
        comp[f"{quem}"]+=v_v

    elif op=='A':
        paraquem=input("para quem alugou: ").upper()
        v_a=int(input("valor do aluguel: "))
        comp[f"{quem}"]+=v_a
        comp[f"{paraquem}"]-=v_a

print(comp)
"""
"""
        #    p2 2019/1 Q3  "cadastro"

lis=[]
while True:
    dic={}
    dic['nome']=input("nome: ")
    dic['idade']=int(input("idade: "))
    dic['id']=int(input(f"identidade de {dic['nome']}: \n '0' para quando nao tiver: "))
    
    if dic['id'] !=0:
        dic['ano']=int(input(f"ano de contratacao de {dic['nome']}"))
        dic['salario']=int(input("salario"))
        dic['aposentadoria']=((dic['ano']+dic['idade'])+35)-2019
    lis.append(dic)

    c=input("continuar: ").upper()
    if c=="N":
        break
print('-='*30)
print('-='*30)
print(lis)
"""