class Pessoa:
    def __init__ (self,nome,idade,comendo=False,falando=False):
        self.nome=nome
        self.idade=idade
        self.comendo=comendo
        self.falando=falando
    def falar(self,fala):
        if self.falando:
            print(f"a pessoa {self.nome} ja esta falando.  ")
            return
        print(f"a pessoa {self.nome} comecou a falar. {fala}")
        self.falando=True
    def parar_falar(self):
        if not self.falando:
            print(f"a pessoa {self.nome} nao estava falando. ")
            return
        print(f"a pessoa {self.nome} parou de falar. ")
    def imprimir(self):
        print(f" nome: {self.nome} \n idade: {self.idade} \n comendo: {self.comendo} \n falando: {self.falando}")
