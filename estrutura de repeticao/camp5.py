x1=float(input("Digite o valor de X1: "))
x2=float(input("Digite o valor de X2: "))
y1=float(input("Digite o valor de Y1: "))
y2=float(input("Digite o valor de Y2: "))
print(x1, x2, y1, y2)
varX=(x1-x2)**2
varY=(y1-y2)**2
distancia=(varX+varY)**0.5
print("A distância é {: .4f}".format(distancia))