class Veiculo:
    def __init__(self,cor,marca,modelo,cap_tanque):
        self.cor=cor
        self.marca=marca
        self.modelo=modelo
        self.cap_tanque=cap_tanque

    def abastecer(self,litros):
        self.cap_tanque+=litros
    
    def retorno(self):
        return self.__dict__

class Carro(Veiculo):
    def __init__(self,cor, marca, modelo, cap_tanque,ano):
        Veiculo.__init__(self,cor,marca,modelo,cap_tanque)
        self.ano=ano

    def abastecer(self,litros):
        if self.cap_tanque + litros >50:
            print("vai da nao")
        else:
            self.cap_tanque+=litros
    
    def retorno(self):
        return self.__dict__

#main
x=Veiculo("a","m","c",55)
x.abastecer(133)
w=Carro("a","m","c",55,2000)
w.abastecer(999)
print(w.retorno())
print(x.retorno())

carros=[]
while True:
    comando=input(""" 
                    A - registrar carro
                    B - abastecer
                    C - 
                    """).upper()
            
    if comando=="A":
        comand=input("A- veiculo  B- carro").upper()
        if comand=="A":
            a=input("cor")
            b=input("Marca")
            c=input("modelo")
            d=input("tanque")
            x=Veiculo(a,b,c,d)
            carros.append(x)
            print(carros)

        elif comand=="B":
            a=input("cor")
            b=input("Marca")
            c=input("modelo")
            d=input("tanque")
            e=input("ano")
            x=Carro(a,b,c,d,e)
            carros.append(x)
            print(carros)

    elif comando =="C":
        break