class ItemPedido:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def calcular_total(self):
        return self.produto.valor * self.quantidade

    def __str__(self):
        return f"{self.produto.descricao} x{self.quantidade} - Total: R${self.calcular_total():.2f}"