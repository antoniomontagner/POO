# Antonio S. Montagner / Matricula:19203742

#comentario sobre o exercicio
""" Em particular nao houve grandes dificuldades,
a mais relevante foi em chegar a um meio de verificacao
para decidir se morreu, perdeu vida ou acertou.
"""

def forca(x,y): #imprimir um desenho no terminal
  if x==0:
    print("------------")
    print("|          |")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|")
    print(y)
    print("-="*20)
  elif x==1:
    print("------------")
    print("|          |")
    print("|          0")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|")
    print(y)
    print("-="*20)

  elif x==2:
    print("------------")
    print("|          |")
    print("|          0")
    print("|          |")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|")
    print(y)
    print("-="*20)
  elif x==3:
    print("------------")
    print("|          |")
    print("|          0")
    print("|         -|")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|")
    print(y)
    print("-="*20)
  elif x==4:
    print("------------    ")
    print("|          |    ")
    print("|          0    ")
    print("|         -|-   ")
    print("|               ")
    print("|               ")
    print("|               ")
    print("|")
    print(y)
    print("-="*20)
  elif x==5:
    print("------------    ")
    print("|          |    ")
    print("|          0    ")
    print("|         -|-   ")
    print("|         /      ")
    print("|               ")
    print("|               ")
    print("|")
    print(y)
    print("-="*20)
  elif x==6:
    print("------------    ")
    print("|          |    ")
    print("|          0    ")
    print("|         -|-   ")
    print("|         / \\    ")
    print("|               ")
    print("|    Lamento! Perdeu! ")
    print("|")
    print(y)
    print("-="*20)

def game(str):  # def principal com a longica
    chave = []
    resposta = []
    for i in range(len(palavra)):   #converter a str em uma lista de letras e uma de "_"
        chave.append(palavra[i])
        resposta.append("_")

    vida=0  #contador de vidas, vai ate 6
    win = False     #flag de vitoria
    while win == False:
        flag = False    #flag de erro ou acerto
        letra = input("Letra: ").upper()

        for i in range(len(chave)):     #verifica se o input esta na lista
            if letra == chave[i]:
                resposta[i] = letra
                flag = True

        win = True
        for i in range(0,len(resposta)):    #verifica se ainda falta letras a serem descobertas
            if resposta[i] == "_":
                win = False 

        if win==False:  #verifica se teve um acerto ou um erro para contar uma vida
            if flag == False:
                vida+=1
                if vida == 6: #verificar se morreu
                    print(vida)
                    forca(vida,resposta)
                    break
                else:
                    forca(vida,resposta)
            else:
                forca(vida,resposta)
        elif win==True: #verificar se venceu
            print("PARABENS!! Voce acertou!! ")
            forca(vida,resposta)

opcao = int(input("""
    OPCOES:
            1:jogar com BOT
            2:jogar com o amiguinho
            : """))

if opcao==1:
    import string
    import random
    def generator(s,chars=string.ascii_uppercase):  #gerar uma str aleatoria
        return ''.join(random.choice(chars) for i in range(s))
        
    tamanho = int(input("Digite o numero de caracteres da palavra: "))
    palavra = generator(tamanho)
    game(palavra)

elif opcao == 2:  # o jogo dependo de um input
    palavra = input("Digite a palavra: ").upper().replace(" ","")
    game(palavra)

else:
    pass