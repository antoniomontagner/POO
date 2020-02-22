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