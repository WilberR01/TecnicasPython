from funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome, idade, cpf):
        super().__init__(nome, idade, cpf, 5000, "Gerente Geral")
        self.__gerenciaPessoal = None

    @property
    def gerenciaPessoal(self):
        return self.__gerenciaPessoal
    
    @gerenciaPessoal.setter
    def gerenciaPessoal(self, rh):
        self.__gerenciaPessoal = rh


    def designaOrdem(self, colaborador, ordem):
        colaborador.novaOrdem(ordem)

    def registraFuncionario(self, novoF):
        self.gerenciaPessoal.registraFuncionario(novoF)

    def consultarFuncionarios(self):
        self.gerenciaPessoal.mostraFuncionarios()
