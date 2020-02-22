n=int(input("n de vezes: "))
for i in range(n):
    m=int(input("quantidade de produtos: "))
    dici={}
    for i in range(m):
        
        dici[f'{input("fruta: ")}']=int(input("preco kg: "))
    print(dici)

    p=int(input("quantidade de frutas compradas: "))
    soma=0
    for i in range(p):
        f=input("fruta: ")
        q=int(input("quantidade: "))
        soma+=(dici[f"{f}"]*q)
    print(f"total {soma}")    
