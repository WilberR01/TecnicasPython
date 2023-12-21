class CadastroViagem():
    def __init__(self, nome, destino):
        self.nome = nome
        self.destino = destino
    def RegistraDestino(self):
        match self.destino:
            case 1:
                return "Marrocos"
            case 2:
                return "Paris"
            case 3:
                return "Nova Zelândia"
            case _:
                return "Opção inválida."
