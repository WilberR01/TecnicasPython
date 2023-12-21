class Produto:
    def __init__(self, codigo, descricao, valor):
        self.codigo = codigo
        self.valor = valor
        self.descricao = descricao

    def __str__(self):
        return f'Código: {self.codigo}, Descrição: {self.descricao}, Valor: {self.valor}'