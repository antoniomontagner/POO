# -*- coding: utf-8 -*-
#o python le linearmente
print('hello word! ss')
print ("jacagay")

para printar das frases juntas pode usar ('jaca'+'gay' ou 'jaca','gay' )
se nao colocar #int(input(..)) e colocar so input, depois somar a+b o resultado vai ser uma concatenacao 13 nao 1+2=3
'oi'*5= oioioioioi







#ordem é () ** * / // %
""" comentario 
de muitas 
linhas """   
print("alexpikao")
#comentario 
print (2+2)
print(8/2)
print(8**2)
mensagem="jacagaysss"
print (mensagem)
print(mensagem)
print(mensagem)
var1=1# inteiro
var2=1.1 #float
var3="string"#sting
var4=True#verdade
var5=Fals
perint(var4)
print(var3)
print(var2)
print(var1)
#atribuicao usa = 
""" == igual
!= diferente
> maior
< menor
>= maior igual
<= menor igual
"""
x=3
y=2
print (x==y)
x=y
y=x
print(x==y and y==x)
print (x==y or y==x)

inteiro= x
nome=y
print("nome:")

print(f'nao sei {:20}.')vai printar a palavra em no maximo 20 caracteres e 
se sobrar ele conrinua com expaco o resto 
{:<20} vai comecar na esquerda > na direita ^ centraliza
{:=^20} vai sair =====caralho====== centralizado e o resto vira =
{:.3f} 1.222






dinheiro = 50000

if dinheiro>10000:
  imps = dinheiro * 0.1
  multa = dinheiro * 0.15
print( "Valor do Imposto:", imps, "e da multa:", multa)

#sempre executa o primeiro comando verdadeiro

# while  caso

x=0
while x<10:
	print(x)
	x+=1#x=x+1


lista1 = [1,2,3]
lista2 = [5,6,7]

for i in lista1:
	#para cada elemento da lista 1, para cada execucao do for o valor i vai ser atribuido aos elementos da lista
    #para varrer os elementos do conjunto de elementos

	print(i)

#pode usar a funcao 'range (10)'retorna uma lista com 10 e etc
#(10,20,2)do elemento 10 ate o 20 contando de 2 em 2

for i in range (10,20,2):#do elemento na posição 10 ate o 20 de 2 em 2

	print(i)


"""numero = input("digite")	
print("o numero")
print(numero)

nome=input("digite o nome:")
print("bem-vindo "+nome)	"""
#executar usa python3 ....
#variavel entre aspas é tipo string e sem aspas é tipo numeral
#concatenar junta as duas variaveis string
#+" "+ para dar expaco
#se for numero entre (" ") vira string

a="jaca"
b="aa a a aaa gay"
concatenar=a+" "+b
print(concatenar)#juntar duas str; palavras

 
tamanho=len(concatenar) # para saber o tamanho de uma string
print(tamanho)


print(a[0])#vai printa J pois comeca a contar do 0,1,2,3
print(a[1])
print(a[2])
print(a[3])

seq = "CGATCCTAGCAT"
print (seq [1:3])#print do 1 ao caracter 3 sem incluir o 3
tamanho= len (concatenar) #para contar o numero de elementos
#caso tenha algum caracter especial e nao queira usar usa .strip() 
print(concatenar.lower()) #print() ; e lower() sao metodos/funcoes entao é obrigado ()
print(concatenar.upper())
concatenar=concatenar.upper()
#   \n
print("b menor que a\nb e positivo")
#   /n é quebra linha
#   .strip para tirar caracters especiais

print(concatenar.split(" ")) #.split()converte em lista
print(concatenar.split("A"))
busca=b.find("gay") #para encontrar a posicao de um elemento
busca2=b.find("izi")
print(busca)
print(busca2)#aparece -1 quando nao encontro nada
#metodo .replace("") substitui partes de uma string, uma parlavara por outra
b= b.replace("gay", "q jossa")#entre aspas é string mesmo se for numero

print(b)


"""funcoes em python sao definidas por "def"  def nome(parametros): /n comandos ; so é executado quando é chamado nome(argumento)"""
""" def sao blocos de codigos que so sao executados quando sao chamados
def (parametros..); bloco de parametros; def soma => funcao;"""
def soma(x,y):
	return(x+y)#x so existe nessa linha e na de cima, para usar fora dessas duas
	#linhas tem que usar return
	print(x+y)
def multiplicacao(x,y):
	return(x*y)
#para exibir o resultado fora da funcao coloca return()
s=soma(2,4)
m=multiplicacao(3,5)
print(s)
print(m)

print(soma(s,m))#varias funcoes de uma vez, com def e return pode 
#fazer contas direto no print


v1=float(input("digite:"))#float, string
print("o valor é: {}".format(v1+2+(3**3)))


print("Sua nota média é {:.2f}.".format(media))#casa decimal

if(soma<6570):
	print("Você ainda não precisa se alistar no serviço militar.")
elif(soma>=6570 and soma<=6577):
	print("Esta na semada de se alistar no serviço militar.")
elif(soma>6577):
	print("Já passou do tempo de se alistar no serviço militar e está sujeito à multa.")

"""for  comandoderepetiçãomaissimples
para cada elemento no loop
ou em cada elemento na lista """
for i in range (0,5): # ou for i in{[1,2,3,4,] ; pode colocar so valor limite tipo:(10) para i em um intervalo de 0 a 5 (range é limite)
	print("Digite ", i)#ta com tab esta dentro do tab
	#ele executa o algoritmo com um numero i e depois testa com outro numero i e assim por diante
for i in range (0,6,2):
	print(i)#para ir de 0 a 6 de 2 em 2 so que nao inclui 6
print("fora do for",i)

#if/
# (, and='') usa para colocar na mesma linha 
# (\n) usa para pular linha
# (+=) o anterios é igual o seguinte mais ele antigo
#(([S/N]')).upper() para deixar a resposta digitada em maiusculo
# (nome:20) delimita o nome para 20 espaços
# (nome:^20 ) centralisa, ~^20 os espaços sobrados vao ser completados com ~~
# < alinha a esquerda e > a direita
# ( != ) diferente


'''r='S'
while r=='S':
	n=int(input("Digite: "))
	o=int(input("Digite: "))
	s=n+o
	print("Soma = ",s)
	r=str(input("[S/N] ")).upper()
print("fim")
'''

import math
n=int(input("n1: "))
x=math.sqrt(n)
print(x)

"""manipular arquivos
variavel(x)=opne(nome do arquivo,modo)
modo pode ser r(somente leitura),w(escrita)para criar arquivos e caso
ja exita ele apaga e cria outro, a(leitura e escrita)se tem ele apenas 
atualiza,r+ e w+ e a+ so muda que permite leitura e escrita"""
arquivo= open("arquivo.txt")
#.readlines(pega cada linha de algum lugar e joga dentro de uma lista)
for linha in linhas:
	print(linha)#vai imprimir linha por linha

#.read (abre o texto completo e joga de uma vez)
w=open("arquivo.txt", "w")#metodo w pois ja existe um arquivo
#para escrever usa .write("...") e tem que fechar
w.write("hhh")
w.close()


"""lista pode ser [1,2,3] ou de strings["aba", "jaca"]"""
#print(lisra[posicao do elemento 0,1,2])
#for item in lista: para navegar pela lista
#.append adiciona um elemento a lista


"""escolha de numero aleatorio usa "import random" 
n=random.ranint(0,10) para selecionar um numero
random.seed(1)para escolher o numero aleatorio escolhido pela maquina
lista=[2,3,4]
n=random.choice(lista)para escolher automaticamente um numero da lista
"""
try:
	print()#para caso nao tenha certeza que de certo
	#caso deu erro insere uma excessao
except:
	print()#assim caso der erro ele fala o aviso e continua a execucao
	
#para item em uma colecao: == for i in range:
#while true é loop infinito ate eu colocar um break

"""frutas=['maca','banana','goiaba','uva']
contador=0
for fruta in frutas:
	contador+=1
print(contador)
ou
print(len(frutas)) numero de itens em cada item do grupo
exemplo basico

while usa quando nao sabe quantas repeticoes vai ter e for quando sabe


while True:
	n=int(input("numero:"))
	for i in range(1,11):
		print(f'{n} X {i} = {n*i}')
	cont=input("continuar:")
	if cont=='n':
		break
		


from math import factorial
x=factorial(n)
para fazer fatorial de uma vez
"""

for i in range(1,21):
	print(i,end=',')
	#para printar elementos lado a lado
import:
	random= numeros aleadorios (randint= para um aleatorio inteiro)
import math( para importar a biblioteca de matematica)
from math import multiplicacao ( para importar da pasta math apenas multiplicacao)

math:
	ceil=arredonda para cima
	floor= arredonda para baixo
	trunc= elimina tudo que ta da virgula para frente 2.44 ==0.44
	pow= potencia
	sqrt= reais quadrada
	factorial= fatorial
import math
#from math import sqrt

n=2
raiz=math.sqrt(n)
print(raiz, math.ceil(raiz)) #math.ceil(raiz)vai arredondar para cima
