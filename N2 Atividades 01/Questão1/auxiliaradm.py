from funcionario import Funcionario

class AuxiliarAdministrativo(Funcionario):
    def __init__(self, nome, idade, cpf):
        super().__init__(nome, idade, cpf, 2800, "Auxiliar Administrativo")

    def realizaOrdem(self):
        super().mostraOrdens()
        super().concluiOrdem()

