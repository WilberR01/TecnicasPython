from contabancaria import ContaBancaria

class ContaImposto(ContaBancaria):
    def __init__(self, numero_conta, titular, saldo, percentualImposto):
        super().__init__(numero_conta, titular, saldo)
        self.percentualImposto = percentualImposto

    def calcularImposto(self):
        imposto = self.saldo * (self.percentualImposto / 100)
        self.saldo -= imposto
