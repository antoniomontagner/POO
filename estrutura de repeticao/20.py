"""valor=1.99*int(input("numero de produtos: "))
print(valor)"""
"""
19
n=int(input("numero"))
div=0


for i in range(1,n+1):
	
	if n%i==0:
		div+=1



if div <=2:
	print("primo")
elif div>2:
	print("nao primo")
"""
"""n=int(input("numero:"))
for i in range(1,n+1):
	
	div=0

	for j in range(1,n+1):
		
		if i%j==0:
			div+=1
	if div <=2:
		print(i,div)
	else:
		print(i,div)"""
"""n=int(input("numero de produtos: "))
if 0<n<51:
	valor=0.18*n
	print(f"{valor} reais")"""
"""total=0
while True:
	valor=int(input("valor:"))
	if valor !=0:
		total+=valor
	else:
		break
print(total)"""
"""menor1=999
menor2=999
total=0
temp=0
while True:
	t=int(input("temperatura"))
	total+=t
	temp+=1
	if t<menor1:
		menor2=menor1
		menor1=t
	continuar=input("continua s n : ")
	if continuar=='n':
		break
media=total/temp
print(f"menor nota {menor1} 2 menor {menor2} media {media}")
"""
"""alto=0
baixo=999
pesado=0
leve=999
cod1=0
cod2=0
cod3=0
cod4=0
while True:
	cod=int(input("codigo: "))
	a=int(input("altura:"))
	b=int(input("peso: "))
	if a>alto:
		alto=a
		cod1=cod
	elif a<baixo:
		baixo=a
		cod2=cod
	elif b > pesado:
		pesado=b
		cod3=cod
	else:
		leve=b
		cod4=cod
	continua=input("continuar s, n: ")
	if continua == 'n':
		break
print(f"o mais alto {alto} codigo {cod1}, baixo {baixo} codigo {cod2}, pesado {pesado} codigo {cod3}, leve {leve} codigo {cod4}")"""
"""cq=0
bs=0
bco=0
hb=0
ch=0
re=0
while  True:
	print('''ESPECIFICACAO, CODIGO, PRECO
		Cachorro Quente 100     R$ 1,20
		Bauru Simples   101		R$ 1,30
		Bauru com ovo   102     R$ 1,50
		Hambúrguer      103     R$ 1,20
		Cheeseburguer   104     R$ 1,30
		Refrigerante   105     R$ 1,00'''
		)
	cod=int(input("codigo:"))
	if cod ==100:
		cq+=1
	elif cod==101:
		bs+=1
	elif cod==102:
		bco+=1
	elif cod==103:
		hb+=1
	elif cod==104:
		ch+=1
	elif cod==105:
		re+=1
	n=input("continuar s,n:")
	if n=='n':
		break
total=(cq*1.2)+(bs*1.3)+(bco*1.5)+(hb*1.2)+(ch*1.3)+(re*1)
print(total)"""
"""
a=0
b=0
c=0
d=0
e=0
f=0
while True:
	n=int(input(""     #falta ""
		candidatos
		1 -jose
		2 -joao
		3 -jaca
		4 -jacira 

		5 -Voto Nulo
		6 -Voto em Branco""))
	if n==1:
		a+=1
	elif n==2:
		b+=1
	elif n==3:
		c+=1
	elif n==4:
		d+=1
	elif n==5:
		e+=1
	elif n==6:
		f+=1
	encerar=int(input("encerar digite 0 e continuar digite 1: "))
	if encerar==0:
		break
total=a+b+c+d+e+f
print(f"total de votos {total}, voto a{a} b{b} c{c} d{d} e{e} f{f}")
"""
"""a=0
b=0
c=0
d=0
while True:
	n=int(input("numero"))
	if 0<=n<=25:
		a+=1
	elif 26<=n<=50:
		b+=1
	elif 51<=n<=75:
		c+=1
	elif 76<=n<=100:
		d+=1
	if n<0:
		break
print(f"no intervalo de 0-25 {a}, no intervalo de 26-50 {b}, 51-75 {c}, 76-100 {d}")
"""
"""34
s=0
n=int(input("dividendo: "))
for i in range(1,n+1):
	m=(2*i)-1
	s+=(i/m)
print(s)"""
"""
35


a=int(input("valor de a: "))
b=int(input("valor de b: "))
c=int(input("valor de c:"))
delta= (b**2)-(4*a*c)
raiz= delta**0.5
x1=((-b)+(raiz))/(2*a)
x2=((-b)-(raiz))/(2*a)
if a ==0:
	print("equacao do 1 grau.")


elif delta<0:
	print("nao tem raizes reais")
	
elif delta==0:
	print(f"apenas uma raiz real {x1}")
elif delta>=0:
	print(f"duas raizes{x1}, {x2}")
"""

"""
35

a=int(input("valor de a: "))
b=int(input("valor de b: "))
c=int(input("valor de c:"))
delta= (b**2)-(4*a*c)
raiz= delta**0.5
x1=((-b)+(raiz))/(2*a)
x2=((-b)-(raiz))/(2*a)
if a ==0:
	print("equacao do 1 grau.")


elif delta<0:
	print("nao tem raizes reais")
	
elif delta==0:
	print(f"apenas uma raiz real {x1}")
elif delta>=0:
	print(f"duas raizes{x1}, {x2}")



36

n=int(input("numero:"))
centenas=0
dezenas=0
uni=0
while n>=100:
	n=n-100
	centenas+=1
while  n>=10:
	n=n-10
	dezenas+=1
while n>=1:
	n=n-1
	uni+=1


print(f"{centenas} centenas e {dezenas} dezenas e {uni} unidades"),


#37

valor= int(input('Digite o valor do saque: '))
cont1=0
cont5=0
cont10=0
cont50=0
cont100=0

while valor>=100:
    valor=valor-100
    cont100+=1
while valor>=50:
    valor=valor-50
    cont50+=1
while valor>=10:
    valor=valor-10
    cont10+=1
while valor>=5:
    valor=valor-5
    cont5+=1
while valor>=1:
    valor=valor-1
    cont1+=1
print(f'Sao necessarias {cont100} notas de 100, {cont50} notas de 50, {cont10} notas de 10, {cont5} notas de 5, {cont1} notas de 1;')


#38


print('''
    a.Telefonou para a vítima?
    b.Esteve no local do crime?
    c.Mora perto da vítima?
    d.Devia para a vítima?
    e.Já trabalhou com a vítima?
''')
resposta = input('')

s= resposta.count('s')

if s>4:
    print('assasino')
elif s>2:
    print('cumplice')
elif s>1:
    print('suspeito')
else:
    print('inocente')



#39
"""
print("""[Álcool:até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina: até 20 litros, desconto de 4% por litro acima  de  20  litros,  desconto  de  6%  por  litro]""")
"""g=0
a=0
preco=0
coisa=input("o que vai querer g ou a:")
quantos=int(input("quantos litros:"))
if coisa=='g':
	if quantos<=20:
		preco=quantos*2.4
	elif quantos>20:
		preco=quantos*2.35
elif coisa=='a':
	if quantos<=20:
		preco=quantos*1.843
	elif quantos>20:
		preco=quantos*1.805
print("o total deu ",preco)
"""
#41
"""
palavra=input("digita a palavra: ")
vogal=('a', 'e', 'i', 'o', 'u')
contv=0
contc=0

for letra in palavra:
	if letra in vogal:
		contv+=1
	else:
		contc+=1
print(f'vogais {contv}, consoantes{contc}')

"""
"""
#42
s = 0
for a in range(1, 500, 2):
    if a % 3 == 0:
        s += a
print('Soma:', s)

	
#40

frase = input('Diga algo: ')

a=0
b=0
for letra in frase:
    if letra in ['a','e','i','o', 'u']:
        a+=1
    if letra in []
print(f'tantas vogais-> {a}')
"""