lis=[]
while True:
    
    
    print("-="*40)
    comando=input("""
                    A - Inserir dados dos clientes. (cadastrar)\n
                    B – Alterar alguma informação do cliente.\n
                    C - Consultar as informações do cliente (pesquisar pelo nome).\n
                    D - Verificar o cliente mais jovem, imprimir seus dados na tela.\n
                    E - Sair 
{}
                    resposta:  """.format("-="*40)).upper()
    print("-="*40)
    if comando=="A":
        dic={}
    
        dic["nome"]=input("nome: ")
        dic["idade"]=int(input("idade: "))
        dic["sexo"]=input("sexo: F/M ").upper()
        lis.append(dic)
        print("-="*40)
        print()
        print(lis)
        print()
    elif comando=="B":
        cliente=input("nome do cliente: ")
        for i in lis:
            if i["nome"]==cliente:
                alt_n=input("alterar nome: S/N").upper()
                if alt_n=="S":
                    i["nome"]=input("nome: ")
                alt_id=input("alterar idade: S/N").upper()
                if alt_id=="S":
                    i["idade"]=int(input("idade: "))
                alt_sex=input("alterar sexo: S/N ").upper()
                if alt_sex=="S":
                    i["sexo"]=input("sexo: ").upper()
                print("-="*30)
                print()
                print(i)
                print()
            else:
                print("ERRO!! Nome nao esta na lista")
    elif comando=="C":
        qual=input("qual cliente: ")
        for i in lis:
            if i["nome"]==qual:
                print("-="*30)
                print()
                print(i)
                print()
    elif comando=="D":
        jovem=[]
        for i in lis:
            if i==lis[0]:
                jovem.append(i)
            else:
                if i["idade"]<=jovem[0]["idade"]:
                    jovem.clear()
                    jovem.append(i)
        print(jovem)
    elif comando=="E":
        break
print(lis)

