from pedido import Pedido
from produto import Produto
from itempedido import ItemPedido

produtos = [
    Produto(1, "Pastilhas de Freio", 50.0),
    Produto(2, "Filtro de Óleo", 10.0),
    Produto(3, "Lâmpada de Farol", 5.0),
    Produto(4, "Bateria de Carro", 80.0),
    Produto(5, "Óleo do Motor", 20.0),
    Produto(6, "Pneu aro 17", 100.0),
    Produto(7, "Amortecedor Dianteiro", 60.0),
    Produto(8, "Correia Dentada", 15.0),
    Produto(9, "Kit de Embreagem", 70.0),
    Produto(10, "Sensor de Oxigênio", 30.0)
]

itens_pedidos = [
    ItemPedido(produtos[1], 3),
    ItemPedido(produtos[3], 2),
    ItemPedido(produtos[6], 1),
    ItemPedido(produtos[0], 4),
    ItemPedido(produtos[9], 2),
    ItemPedido(produtos[2], 5)
]

MeuPedido = Pedido()
for item in itens_pedidos:
    MeuPedido.adicionarItem(item)
print(MeuPedido)