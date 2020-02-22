a="jaca"
b="aa a a aaa gay"
concatenar=a+" "+b
print(concatenar)#juntar duas str; palavras

 
tamanho=len(concatenar) # para saber o tamanho de uma string
print(tamanho)


print(a[0])#vai printa J pois comeca a contar do 0,1,2,3(jaca)
print(a[1])
print(a[2])
print(a[3])

seq = "CGATCCTAGCAT"
print (seq [1:3])#print do 1 ao caracter 3 sem incluir o 3
tamanho= len (seq) #para contar o numero de elementos
print(tamanho)
#caso tenha algum caracter especial e nao queira usar usa .strip() 
print(concatenar.lower()) #print() ; e lower() sao metodos/funcoes entao é obrigado ()
print(concatenar.upper())
concatenar=concatenar.upper()
#/n é quebra linha
print(concatenar.split(" ")) #.split()converte em lista
print(concatenar.split("A"))
busca=b.find("gay") #para encontrar a posicao de um elemento
busca2=b.find("izi")
print(busca)
print(busca2)#aparece -1 quando nao encontro nada
#metodo .replace("") substitui partes de uma string
b= b.replace("gay", "q jossa")
print(b)