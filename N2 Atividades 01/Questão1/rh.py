from funcionario import Funcionario

class Rh:
    def __init__(self):
        self.registroFunc = []
    
    def registraFuncionario(self, novoF):
        self.registroFunc.append(novoF)

    def mostraFuncionarios(self):
        for funcionario in self.registroFunc:
            print(funcionario)
                