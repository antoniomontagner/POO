from random import randrange
num=randrange(11)
cont=1
teclado= int(input("Digite um numero de 0 a 10: "))
while (num != teclado):
	teclado= int(input("Digite novamente: "))
	cont +=1
print("Voce acertou. Numero secreto é {}. \nem {} tentativas.".format(num, cont))
