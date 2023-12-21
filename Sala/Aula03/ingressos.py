class Ingresso:
    def __init__(self, valor):
        self.valor = valor
    def imprimeValor(self):
        print (f'O valor do ingresso é {self.valor}')

class IVip(Ingresso):
    def __init__(self, valor, extra):
        super().__init__(valor+extra)