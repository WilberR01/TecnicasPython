from os.path import dirname, join

class Cadastro():
    current_dir = dirname(__file__)
    file_path = join(current_dir, "./livros.txt")
    with open(file_path, "r", encoding="UTF-8") as arquivo:
        livros = arquivo.readlines()
    def __init__(self, nome):
        self.nome = nome

    def mostraCatalogo(self):
        i = 1
        for livro in self.livros:
            print(str(i) + " - " + livro)
            i += 1 

    def validaEscolha(self, id):
        match id:
            case 1|2|3|4|5|6|7|8|9|10:
                return id
            case _:
                return 0

    def escolheLivro(self, id):
        cont = 1
        for livro in self.livros:
            if cont == id:
                return livro
            else:
                cont += 1