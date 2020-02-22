class Historico():
    def __init__(self,transacao):
        self.transacoes=transacao
    def transa(self):
        transacoes=[]
    
class Conta():
    def __init__(self,numero,cliente,saldo,limite):
        self.numero=numero
        self.cliente=cliente
        self.saldo=saldo
        self.limite=limite
        self.historico=Historico()
    def deposito(self,valor):
        self.saldo+=valor
        self.historico.transacoes.append(f"deposito de {valor}.")
    def retira(self,valor):
        if self.saldo<valor:
            print("Saldo insuficiente")
        else:
            self.saldo-=valor
            self.historico.transacoes.append(f" saque de {self.saldo}")
    def extrato(self):
        print(f"conta {self.numero} saldo {self.saldo}")
    def transfere(self,destino,valor):
        if self.saldo>valor:
            self.saldo-=valor
            destino.saldo+=valor
            self.historico.transacoes.append(f"transferencia de {valor} para{destino}")

while True:
    contas=[]
    comando=input("""
            1. Criar conta
            2. Operação de saque
            3. Operação de depósito
            4. Operação de transferência
            5. Extrato
            6. Cadastrar cliente
            7. Sair
    
    resposta: """)
    if comando=="1":
        x=onta