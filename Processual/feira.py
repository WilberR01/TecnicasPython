from os.path import dirname, join

class Cadastro():
    current_dir = dirname(__file__)
    file_path = join(current_dir, "./frutas.txt")
    with open(file_path, "r", encoding="UTF-8") as arquivo:
        frutas = arquivo.readlines()
    def __init__(self, nome):
        self.nome = nome

    def mostraCatalogo(self):
        i = 1
        for fruta in self.frutas:
            print(str(i) + " - " + fruta)
            i += 1 

    def validaEscolha(self, id):
        match id:
            case 1|2|3|4|5:
                return id
            case _:
                return 0

    def escolheFruta(self, id):
        cont = 1
        for fruta in self.frutas:
            if cont == id:
                return fruta
            else:
                cont += 1