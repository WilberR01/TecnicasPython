class Pedido:
    def __init__(self):
        self.itens = []

    def adicionarItem(self, item):
        self.itens.append(item)

    def calcular_total_pedido(self):
        total = 0
        for item in self.itens:
            total += item.calcular_total()
        return total

    def __str__(self):
        return f"Pedido com {len(self.itens)} item(s)\nVALOR TOTAL: R${self.calcular_total_pedido():.2f}"